# Pitter, Patter, Platters
[Link Challenge](https://play.picoctf.org/practice/challenge/87)

'Suspicious' is written all over this disk image. Download [suspicious.dd.sda1](https://jupiter.challenges.picoctf.org/static/0d39390cff1ab51699596b6e650e7cba/suspicious.dd.sda1)

#DigitalForensic #wu #ImageForensic 
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
suspicious.dd.sda1
```

Analisis menggunakan tools seperti FTK Imager atau Autopsy akan memudahkan untuk manganalisa disk. Namun, kali ini akan menggunakan CLI

Install Sleuth Kit pada terminal
```
sudo apt install sleuthkit
```

Gunakan `fls` untuk menampilkan list directory dan file pada image.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ fls suspicious.dd.sda1
d/d 11: lost+found
d/d 2009:       boot
d/d 4017:       tce
r/r 12: suspicious-file.txt
V/V 8033:       $OrphanFiles
```

Terdapat file sus, coba tampilkan aja
```
V/V 8033:       $OrphanFiles

┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ icat suspicious.dd.sda1 12
Nothing to see here! But you may want to look here -->
```

Sepertinya itu terpotong, gunakan `-s` untuk **mengabaikan alamat blok yang tidak valid** saat membaca file dari inode
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ icat -s suspicious.dd.sda1 12
Nothing to see here! But you may want to look here -->
}83460cae_3<_|Lm_111t5_3b{FTCocip
```

Wow, balik aja
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ icat -s suspicious.dd.sda1 12 | rev
>-- ereh kool ot tnaw yam uoy tuB !ereh ees ot gnihtoN
picoCTF{b3_5t111_mL|_<3_eac06438}
```

```
picoCTF{b3_5t111_mL|_<3_eac06438}
```