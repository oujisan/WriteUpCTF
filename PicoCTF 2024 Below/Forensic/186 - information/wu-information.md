# information
[Link Challenge](https://play.picoctf.org/practice/challenge/186)

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/7cf6a33f90deeeac5c73407a1bdc99b6/cat.jpg)

#Forensic #wu #png #exiftool #steganography 
___
Analisa file `cat.jpg`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ exiftool cat.jpg
ExifTool Version Number         : 13.00
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2025:02:05 14:15:33+07:00
File Access Date/Time           : 2025:02:05 14:16:24+07:00
File Inode Change Date/Time     : 2025:02:05 14:16:17+07:00
File Permissions                : -rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

Terlihat jelas pada License nilainya berbentuk base64. decrypyt aja
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ exiftool -License -b cat.jpg | base64 -d
picoCTF{the_m3tadata_1s_modified}
```

```
picoCTF{the_m3tadata_1s_modified}
```