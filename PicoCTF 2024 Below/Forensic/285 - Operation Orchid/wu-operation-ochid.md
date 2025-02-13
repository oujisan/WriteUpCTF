# Operation Ochid
[Link Challenge](https://play.picoctf.org/practice/challenge/285)

Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
- [Download compressed disk image](https://artifacts.picoctf.net/c/212/disk.flag.img.gz)

#DigitalForensic #ImageForensic #wu 
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/pico/disk.flag.img]
└─$ ls
disk.flag.img
```

Gunakan FTK Imager atau Autopsy untuk menganalisa disk image.

Pada bagian root, terdapat file `.ash_history` dan `flag.txt.enc`
Berikut isi dari `.ash_history`
```
touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
```

Kesimpulannya ia membuat file `flag.txt` dan mengenkripsi menggunakan AES256 dengan password `unbreakablepassword1234567` menggunakan `openssl`.

Jadi yang harus dilakukan adalah decrypt file diatas menggunakan password diatas.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/pico/disk.flag.img]
└─$ openssl aes256 -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
4017C6BE057F0000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:../providers/implementations/ciphers/ciphercommon_block.c:107:
```

Yea, bad decrypt but works!

cat aja
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/pico/disk.flag.img]
└─$ cat flag.txt
picoCTF{h4un71ng_p457_0a710765}
```

```
picoCTF{h4un71ng_p457_0a710765}
```