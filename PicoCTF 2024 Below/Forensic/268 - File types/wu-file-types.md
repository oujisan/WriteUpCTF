# File types
[Link Challenge](https://play.picoctf.org/practice/challenge/268)

This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.You can download the file from [here](https://artifacts.picoctf.net/c/81/Flag.pdf).

#Forensic #wu #decode
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
Flag.pdf
```

Ketika di cek menggunakan `file`, ternyata file tersebut bukanlah pdf melainkan shell archive text. Yang berati file tersebut dapat dieksekusi.

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file Flag.pdf
Flag.pdf: shell archive text
```

Sebelum melakukan eksekusi pastikan sudah memberikan izin `execute` pada file.
```
sudo chmod +x Flag.pdf
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ll
total 8
-rwxrwxrwx 1 kali kali 5161 Feb  6 06:09 Flag.pdf
```

Jalankan `Flag.pdf` layaknya executable file
```
./Flag.pdf
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ./Flag.pdf
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
```

Jika gagal atau mengeluarkan hasil seperti dibawah ini:
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ./Flag.pdf
119: uudecode: not found 
restore of flag failed 
flag: MD5 check failed
```
Hal ini disebabkan `uudecode` tidak ditemukan, install terlebih dahulu `sharutils`

```
sudo apt install sharutils -y
```
Coba jalankan kembali file diatas.

Setelah dijalankan muncul file baru bernama `flag` yang setelah dicek memliki format ar archive.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file flag
flag: current ar archive
```

Pilihan opsional, tambahkan format nama file `flag`  sesuai dengan keterangan di file
```
mv flag flag.ar
```

Ekstrak file `ar` archive
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ar xc flag.ar
```

Muncul lagi file baru dengan format `cpio` archive
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file flag
flag: cpio archive; device 234, inode 37426, mode 100644, uid 0, gid 0, modified Thu Mar 16 01:40:17 2023, 510 bytes "flag"
```

Lakukan hal yang sama dengan diatas, yaitu menambahkan spesifik ekstensi (opsional)  dan ekstrak.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ mv flag flag.cpio

┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ cpio -i < flag.cpio
2 blocks
```

Dan terjadi lagi, kali ini `bzip2`.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file flag
flag.bz2: bzip2 compressed data, block size = 900k
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ mv flag flag.bz2

┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ bzip2 -dc flag.bz2 > flag
```

lanjut `gzip`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file flag
flag: gzip compressed data, was "flag", last modified: Thu Mar 16 01:40:17 2023, from Unix, original size modulo 2^32 327
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ mv flag flag.gz

┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ gzip -dc flag.gz > flag
```

`lzip`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file flag
flag: lzip compressed data, version: 1
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ mv flag flag.lz

┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ lzip -dc flag.lz > flag
```

`lz4`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file flag
flag: LZ4 compressed data (v1.4+)
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ mv flag flag.lz4

┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ lz4 -d flag.lz4 flag
flag.lz4             : decoded 265 bytes
```

`LZMA`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file flag
flag: LZMA compressed data, non-streamed, size 254
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ xz -d flag.lzma -c > flag
```

`lzop`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file flag
flag: lzop compressed data - version 1.040, LZO1X-1, os: Unix
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ mv flag flag.lzop

┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ lzop -d -c flag.lzop > flag
```

`lzip` again
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file flag
flag: lzip compressed data, version: 1
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ lzip -dc flagg.lz > flag
```

`xz`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file flag
flag: XZ compressed data, checksum CRC64
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ mv flag flag.xz

┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ xz -d -c flag.xz > flag
```

dan akhirnya mencapai ASCII text, untuk mengubah ke string biasa gunakan `xxd -r -p`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ cat flag | xxd -r -p
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}
```

Untuk menemukan flag kita harus extract sampai segini
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
flag  flag.ar  flag.bz2  flag.cpio  flagg.lz  flag.gz  flag.lz  flag.lz4  flag.lzma  flag.lzop  Flag.pdf  flag.xz
```

```
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}
```
