# 444 - Scan Suprise
[Link Challenge](https://play.picoctf.org/practice/challenge/444)

I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?You can download the challenge files here:
- [challenge.zip](https://artifacts.picoctf.net/c_atlas/16/challenge.zip)
Additional details will be available after launching your challenge instance.

#PicoCTF2024 #Forensic #Easy #qr-code #wu
___
Ekstrak file `challenge.zip` dan buka sampai menemukan file `flag.png`.
Diberi gambar QR-Code dimana judul soal adalah "Scan" jadi kita coba untuk scan QR-Code tersebut menggunakan `zbarimg`[^1]

Install zbarimg terlebih dahulu.
```
┌──(kali㉿oujisan)-[/mnt/d/PicoCTF/Forensic/Scan Surprise/challenge/home/ctf-player/drop-in]
└─$ sudo apt-get install zbar-tools
```

Scan `flag.png`
```
zbarimg flag.png
```

```
┌──(kali㉿oujisan)-[/mnt/d/PicoCTF/Forensic/ScanSurprise/challenge/home/ctf-player/drop-in]
└─$ zbarimg flag.png
Connection Error (Failed to connect to socket /run/dbus/system_bus_socket: No such file or directory)
Connection Null
QR-Code:picoCTF{p33k_@_b00_7843f77c}
scanned 1 barcode symbols from 1 images in 0.01 seconds
```

[^1]: https://medium.com/@sumitdhattarwal4444/creating-and-reading-qr-code-in-linux-5cfeb2d65063
