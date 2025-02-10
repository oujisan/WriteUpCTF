# Shark on Wire 1
[Link Challenge](https://play.picoctf.org/practice/challenge/30)

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap). Recover the flag.

#DigitalForensic #wu #pcap 
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
capture.pcap
```

Analisa pada wireshark. Coba untuk analisa port UDP dengan melakukan stream UDP untuk mendapatkan hint.

Terdapat banyak dummy text sebagai pengecoh seperti picopico, dll. Seperti dibawah ini juga
```
picoCTF{N0t_a_fLag}
```
yang berasal dari `10.0.0.2	10.0.0.13	UDP	60	5000 → 8888`

Namun, diatas terdapat `10.0.0.2	10.0.0.12	UDP	60	5000 → 8888`, aku coba untuk melakukan UDP Stream sepertinya kita menemukan flag
```
picoCTF{StaT31355_636f6e6e}
```

Ternyata ini adalah real flag.