# Like1000
[Link Challenge](https://play.picoctf.org/practice/challenge/81)

This [.tar file](https://jupiter.challenges.picoctf.org/static/52084b5ad360b25f9af83933114324e0/1000.tar) got tarred a lot.

#DigitalForensic #wu 
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
1000.tar
```

Coba ekstrak tar diatas menggunakan `tar -xvf`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
999.tar filler.txt
```

Dan apabila dilanjutkan akan trus berkurang 1 angkanya. Kemungkinan sampai 1.tar. Gunakan script loop untuk mempercepat waktu.
```
for i in $(seq 1000 -1 1); do tar -xf "$i.tar"; done
```

Ketika sudah mencapai `1.tar` kita akan mendapatkan file bernama `flag.png`. 

```
picoCTF{l0t5_0f_TAR5}
```
