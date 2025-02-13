# Disk, disk, Sleuth!
[Link Challenge](https://play.picoctf.org/practice/challenge/113)

Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/626ea9c275fbd02dd3451b81f9c5e249/dds1-alpine.flag.img.gz)

#DigitalForensic #wu #ImageForensic 
___

Pada hint soal menggunakan `srch_strings`. Jadi kita coba untuk tembak langsung mencari flag 

Install sleuthkit
```
sudo apt install sleuthkit
```

Lalu gunakan `srch_strings` 
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall/dds1-alpine.flag.img]
└─$ srch_strings -td dds1-alpine.flag.img | grep "pico"
  11415345 ffffffff81399ccf t pirq_pico_get
  11415378 ffffffff81399cee t pirq_pico_set
  13818980 ffffffff820adb46 t pico_router_probe
 105923644   SAY picoCTF{f0r3ns1c4t0r_n30phyt3_a6f4cab5}
```

Apabila menggunakan GUI Autopsy, tekan Keyword Search lalu ketik "picoCTF" maka akan muncul file `syslinux.cfg` yang terletak pada `/boot/syslinux.cfg`
```
[syslinux.cfg, DEFAULT linux
  SAY Now booting the kernel from SYSLINUX...
  SAY 
picoCTF{f0r3ns1c4t0r_n30phyt3_a6f4cab5}
 LABEL linux
  KERNEL /boot/vmlinuz-virt
  APPEND ro root=/dev/sda1 rootfstype=ext3 initrd=/boot/initramfs-virt
```

```
picoCTF{f0r3ns1c4t0r_n30phyt3_a6f4cab5}
```