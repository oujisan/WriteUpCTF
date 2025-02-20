# Rotation
[Link Challenge](https://play.picoctf.org/practice/challenge/373)

You will find the flag after decrypting this file Download the encrypted flag [here](https://artifacts.picoctf.net/c/386/encrypted.txt).

#cryptography #wu
___
```
┌──(kali㉿oujisan)-[/PicoCTF 2024 Below/Cryptography/373 - rotation/chall]
└─$ cat encrypted.txt
xqkwKBN{z0bib1wv_l3kzgxb3l_4k71n5j0}
```
Kemungkinan ini adalah ROT Chiper, jadi untuk bantuan gunakan [dcode.fr](https://www.dcode.fr/rot-cipher) untuk brute force decrypt.

Hasilnya didapat flag pada `[A-Z]+8 ` atau ROT 8 tetapi dengan rotasi ke kanan, jadi pada CyberChef tidak menemukan karena defaultnya adalah rotasi ke kiri.
```
picoCTF{r0tat1on_d3crypt3d_4c71f5b0}
```
