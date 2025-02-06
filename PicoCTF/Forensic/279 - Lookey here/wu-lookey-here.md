# Lookey Here
[Link Challenge](https://play.picoctf.org/practice/challenge/279)

Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.Download the data [here](https://artifacts.picoctf.net/c/124/anthem.flag.txt).

#Forensic #wu #grep
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
anthem.flag.txt
```

File tersebut berisi teks yang sangat panjang, coba untuk filter atau cari format file didalamnya
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ cat anthem.flag.txt | grep -o "picoCTF{.*}"
picoCTF{gr3p_15_@w3s0m3_4c479940}
```

```
picoCTF{gr3p_15_@w3s0m3_4c479940}
```
