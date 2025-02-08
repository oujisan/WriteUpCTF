# TITLE
[Link Challenge](https://play.picoctf.org/practice/challenge/130)

I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/3944a59474f9f676942282c50b9c3675/Forensics%20is%20fun.pptm)

#Forensic #wu 
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
'Forensics is fun.pptm'
```

Setelah dilakukan analisa menggunakan binwalk, terdapat file zip di dalamnya. Esktrak aja
```
binwalk --dd=".*" Forensics\ is\ fun.pptm
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall/_Forensics is fun.pptm.extracted]
└─$ ll
total 100
-rwxrwxrwx 1 kali kali 100093 Feb  8 08:54 0
-rwxrwxrwx 1 kali kali     22 Feb  8 08:54 186E7
```

di dalamnya terdapat file `0` yang merupakan ppt dan `186E7` zip tapi empty.
Ternyata pada ppt masih terdapat file zip didalamnya, coba ekstrak lagi

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall/_Forensics is fun.pptm.extracted]
└─$ binwalk -e 0
```

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall/_Forensics is fun.pptm.extracted/_0.extracted]
└─$ ls
 0.zip  '[Content_Types].xml'   docProps   ppt   _rels
```

terdapat banyak beberapa folder yang dibuka ada banyak file. Untuk mempersingkat pencarian gunakan `tree` untuk melihat seluruh isi dari folder ekstrak.

```
├── slideMasters
│   │   ├── hidden
│   │   ├── _rels
│   │   │   └── slideMaster1.xml.rels
│   │   └── slideMaster1.xml
```

Pada slideMasters ditemukan file hidden, langsung cek aja
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall/_Forensics is fun.pptm.extracted/_0.extracted/ppt/slideMasters]
└─$ cat hidden
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
```

Nampaknya ini adalah `base64`, coba lakukan decode serta hilangkan space
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall/_Forensics is fun.pptm.extracted/_0.extracted/ppt/slideMasters]
└─$ cat hidden | tr -d "  " | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}
```

```
picoCTF{D1d_u_kn0w_ppts_r_z1p5}
```
