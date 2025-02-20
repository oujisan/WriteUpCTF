# HideToSee
[Link Challenge](https://play.picoctf.org/practice/challenge/315)

How about some hide and seek heh?Look at this image [here](https://artifacts.picoctf.net/c/240/atbash.jpg).

#cryptography #wu
___
Soal kriptografi diberi gambar? baik, setelah dicek pada binwalk tidak ada apa-apa. Tapi...
Setelah dianalisa pada steghide, terdapat file bernama `encrypted.txt`
```
┌──(kali㉿oujisan)-[PicoCTF 2024 Below/Cryptography/315 - HideToSee/chall]
└─$ steghide info atbash.jpg
"atbash.jpg":
  format: jpeg
  capacity: 2.4 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "encrypted.txt":
    size: 31.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

Extract dah
```
┌──(kali㉿oujisan)-[PicoCTF 2024 Below/Cryptography/315 - HideToSee/chall]
└─$ steghide extract -sf atbash.jpg
Enter passphrase:
wrote extracted data to "encrypted.txt".
```

Sesuai pada gambar, kita decrypt atbash cipher ini dengan bantuan web [dcode.fr](https://www.dcode.fr/atbash-cipher)
```
picoCTF{atbash_crack_ca00558b}
```
