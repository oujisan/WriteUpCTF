# extensions
[Link Challenge](https://play.picoctf.org/practice/challenge/52)

This is a really weird text file [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)? Can you find the flag?

#png #Forensic #wu
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
flag.txt
```

Ketika dianalisa dengan `file` didapatkan jika sebenarnya file tersebut adalah png. ABSOULUTE CINEMA
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file flag.txt
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```

rename ekstensi menjadi png
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ cp flag.txt flag.png
```

lalu buka gambarnya
![PicoCTF/Forensic/52 - extensions/img/flag.png](.img/flag.png)

Karen aku mala menulis, pakai `tesseract` untuk mendapatkan tulisan secara langsung
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ tesseract flag.png stdout
picoCTF{now_you_know_about_extensions}
```

```
picoCTF{now_you_know_about_extensions}
```
