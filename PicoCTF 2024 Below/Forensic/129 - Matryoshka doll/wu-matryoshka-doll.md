# Matryoshka Doll
[Link Challenge](https://play.picoctf.org/practice/challenge/129)

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg)

#Forensic #steganography #wu #zip #png
___
Diberi file bernama `dolls.jpg` seperti biasa jika menemukan file foto lakukan analisa mulai dari `file`, `exiftool`, `strings`, `binwalk`.

Ketika dianalisa menggunakan binwalk, terdapat zip tersembunyi di dalam `dolls.png`.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ binwalk dolls.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378955, uncompressed size: 383936, name: base_images/2_c.jpg
651613        0x9F15D         End of Zip archive, footer length: 22
```

Singkatnya challenge ini menyembunyikan zip yang berisi gambar dalam gambar utama dan ditumpuk hingga 4 kali `-_-`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall/_dolls.jpg.extracted/]
└─$ tree
/mnt/c/Users/Ouji/Downloads/chall/_dolls.jpg.extracted/
├── 0
├── 4286C
├── 9F15D
├── base_images
│   ├── 2_c.jpg
│   └── _2_c.jpg.extracted
│       ├── 0
│       ├── 2DD3B
│       ├── 5DB3B
│       ├── 5DBAA
│       ├── base_images
│       │   ├── 3_c.jpg
│       │   └── _3_c.jpg.extracted
│       │       ├── 0
│       │       ├── 1E2D6
│       │       ├── 312CD
│       │       ├── base_images
│       │       │   ├── 4_c.jpg
│       │       │   └── _4_c.jpg.extracted
│       │       │       ├── 0
│       │       │       ├── 136DA
│       │       │       ├── 137A8
│       │       │       ├── C9A
│       │       │       └── flag.txt
│       │       └── C9A
│       └── C9A
└── C9A

7 directories, 21 files
```

Jadi, ekstrak zip tersembunyi menggunakan binwalk, unzip file zip yang ada hingga memunculkan foto baru dan ulangi lagi mulai ekstrak binwalk sampai unzip file zip terakhir yang berisi `flag.txt` yang berada di dalam `4_c.jpg`.

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ cat flag.txt
picoCTF{ac0072c423ee13bfc0b166af72e25b61}
```

```
picoCTF{ac0072c423ee13bfc0b166af72e25b61}
```