# St3g0
[Link Challenge](https://play.picoctf.org/practice/challenge/305)

Download this image and find the flag.
- [Download image](https://artifacts.picoctf.net/c/217/pico.flag.png)

#MSB-LSB #steganography #Forensic #wu
___
Jika menemukan file `png` maka langsung saja melakukan pengecekan
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
pico.flag.png
```

Dilakukan pengecekan menggunakan `file`, `strings`, `exiftool` dan `binwalk` tidak ada hasil atau petunjuk.

Setelah dibawa pada [StegOnline](https://georgeom.net/StegOnline/upload) dan dilakukan perubahan warna untuk mengecek  apakah ada pesan tersembunyi pada visual gambar namun nihil.

Iseng untuk mengekstrak gambar dengan tipe LSB untuk menemukan flag dan berbuah manis.
Gunakan tool [stigBits](https://github.com/Pulho/sigBits), install dulu requirement dan sempatkan baca dokumentasi.

LSB atau Less Significant Bit adalah metode steganography dimana seseorang menyembunyikan atau menyisipkan pesan pada bit terakhir setiap pixel atau RGB

```
python sigBits.py -t=lsb ..\..\..\Downloads\chall\pico.flag.png
```

File output akan berada default pada directory `sigBits` jika tidak menerapkan tujuan output.
Setelah dibuka terdapat flag didalamnya. 

Gunakan grep untuk mengambil string flagnya saja
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Desktop/cli-tools/sigBits]
└─$ cat outputSB.txt | tr " " "\n" | grep -o "picoCTF{.*}"
picoCTF{7h3r3_15_n0_5p00n_a9a181eb}
```

```
picoCTF{7h3r3_15_n0_5p00n_a9a181eb}
```
