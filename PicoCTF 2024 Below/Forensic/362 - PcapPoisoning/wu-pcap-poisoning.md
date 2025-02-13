# Pcap Poisoning
[Link Challenge](https://play.picoctf.org/practice/challenge/362)

How about some hide and seek heh?Download this [file](https://artifacts.picoctf.net/c/371/trace.pcap) and find the flag.

#Forensic #Strings #pcap #wu 
___
Cara paling mudah untuk menganalisa file pcap tanpa perlu membuka wireshark adalah menggunakan strings.
Karena format flag pico CTF adalah `picoCTF{}` maka akan langsung difilter untuk mempermudah
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ strings trace.pcap | grep "pico"
picoCTF{P64P_4N4L7S1S_SU55355FUL_fc4e803f}3~
```

```
picoCTF{P64P_4N4L7S1S_SU55355FUL_fc4e803f}3~
```