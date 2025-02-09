# Sleuthkit Apprentice
[Link Challenge](https://play.picoctf.org/practice/challenge/300)

Download this disk image and find the flag.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/138/disk.flag.img.gz)

#DigitalForensic  #wu #ImageForensic #ftk-imager 
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall/disk.flag.img]
└─$ ls
disk.flag.img
```

Gunakan tools seperti FTK Imager atau sejenisnya untuk memudahkan menganalisa.

Diberikan 3 Partisi dengan nama `Partition 1`, `Partition 2`, `Partition 3`
- Partition 1 merupakan boot partition
- Partition 2 merupakan swap partition
- Partition 3 merupakan root partition

langsung aja untuk megarah pada partition 3, jika soal seperti ini coba untuk mengecek directory `home` atau `root` terlebih dahulu.

Pada directory root terdapat directory lain yang bernama my_folder dan didalamnya ada `flag.uni.txt`. Yang ternyata isinya adalah real flag.

```
picoCTF{by73_5urf3r_2f22df38}
```
