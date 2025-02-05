# Glory of The Garden
[Link Challenge](https://play.picoctf.org/practice/challenge/44)

This [garden](https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg) contains more than it seems.

#Forensic #wu #png #Strings #steganography 
___

Setelah melakukan analisa pada `exiftool`, `file`, dan `binwalk` tidak menemukan keanehan apapun. Maka, coba untuk melihat pada strings gambar. Karena format flag di pico ialah `picoCTF{}`, untuk mempersingkat pencarian maka langsung difiler yang memiliki kata tersebut.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ strings garden.jpg | grep "pico"
Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}"
```

```
picoCTF{more_than_m33ts_the_3y3eBdBd2cc}
```

