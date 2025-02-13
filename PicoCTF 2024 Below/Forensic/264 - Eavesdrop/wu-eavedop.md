# Eavedrop
[Link Challenge](https://play.picoctf.org/practice/challenge/264)

Download this packet capture and find the flag.

- [Download packet capture](https://artifacts.picoctf.net/c/135/capture.flag.pcap)

#DigitalForensic #pcap #openssl
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
capture.flag.pcap
```

Gunakan wireshark untuk menganalisa file pcap.

Setelah dianalisa, ditemukan percakapan pada jaringan dengan follow `TCP Stream`
```
Hey, how do you decrypt this file again?

You're serious?

Yeah, I'm serious

*sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123

Ok, great, thanks.

Let's use Discord next time, it's more secure.

C'mon, no one knows we use this program like this!

Whatever.

Hey.

Yeah?

Could you transfer the file to me again?

Oh great. Ok, over 9002?

Yeah, listening.

Sent it

Got it.

You're unbelievable
```

Informasi penting yang bisa didapatkan adalah
```
openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
```

Syntax diatas bertujuan untuk dekripsi `file.des3` dengan key `supersecretpassword123`

Kemungkinan kita harus mencari file tersebut untuk mendapatkan flag. Pertanyaanya dimanakah file tersebut berada.

Setelah mencari pada wireshark, tidak ditemukan clue apa-apa lagi. Lalu berfikir, "Apakah mungkin pcap bisa menyimpan file?"

dari situ, aku mencoba menggunakan binwalk untuk mengecek.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ binwalk capture.flag.pcap

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Libpcap capture file, little-endian, version 2.4, Ethernet, snaplen: 262144
5882          0x16FA          OpenSSL encryption, salted, salt: 0x3C4B26E8B8F91E2C
```

Ekstrak aja
```
binwalk --dd=".*" capture.flag.pcap
```

gunakan syntax openssl diatas untuk decode file dengan mengganti nama file menjadi `16FA`
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall/_capture.flag.pcap.extracted]
└─$ openssl des3 -d -salt -in 16FA -out file.txt -k supersecretpassword123
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
40E796BA327F0000:error:1C80006B:Provider routines:ossl_cipher_generic_block_final:wrong final block length:../providers/implementations/ciphers/ciphercommon.c:443:
```

Buka `file.txt`  untuk mendapatkan flag
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall/_capture.flag.pcap.extracted]
└─$ cat file.txt
picoCTF{nc_73115_411_0ee7267a}...
```

```
picoCTF{nc_73115_411_0ee7267a}
```