# What Lies Within
[Link Challenge](https://play.picoctf.org/practice/challenge/74)

There's something in the [building](https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png). Can you retrieve the flag?

#Forensic #MSB-LSB #png #steganography 
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
buildings.png
```

dilakukan analisa file dengan `file`, `binwalk`, `exiftool` dan `strings` tetapi tidak menemukan sesuatu.

Kemungkinan adalah di dalam bits. Karena gambar tidak mengalami banyak perubahan warna bisa diasumsikan jika ini Less Significant Bits atau LSB.

Gunakan tools web seperti [Steganography Online](https://stylesuxx.github.io/steganography/) atau [sigBits](https://github.com/Pulho/sigBits) yang menggunakan CLI.

Disini akan menggunakan sigBits (lebih nyaman aja pake terminal :v)
```
python sigBits.py -t=lsb ..\..\..\Downloads\chall\buildings.png
Done, check the output file!
```

tinggal cek aja hasil output dari sigBits.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ cat ../../Desktop/cli-tools/sigBits/outputSB.txt
picoCTF{h1d1ng_1n_th3_b1t5}
```

```
picoCTF{h1d1ng_1n_th3_b1t5}
```
