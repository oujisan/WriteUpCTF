# CanYouSee
[Link Challenge](https://play.picoctf.org/practice/challenge/408)
How about some hide and seek?

#Forensic #wu #png #exiftool
___

Unzip file yang telah didownload
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ file unknown.zip
unknown.zip: Zip archive data, at least v2.0 to extract, compression method=deflate

┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
ukn_reality.jpg  unknown.zip
```

Analisa file `ukn_relity.png`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ exiftool ukn_reality.jpg
ExifTool Version Number         : 13.00
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2024:02:16 05:40:17+07:00
File Access Date/Time           : 2025:02:05 14:07:02+07:00
File Inode Change Date/Time     : 2025:02:05 14:06:55+07:00
File Permissions                : -rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fNGRhYmRkY2J9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
```

Sudah terlihat hal yang sus pada AttributionURL, dimana value dienkripsi base64.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ exiftool -AttributionURL -b ukn_reality.jpg | base64 -d
picoCTF{ME74D47A_HIDD3N_4dabddcb}
```

```
picoCTF{ME74D47A_HIDD3N_4dabddcb}
```