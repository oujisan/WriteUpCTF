# ReadMyCert
[Link Challenge](https://play.picoctf.org/practice/challenge/367)

How about we take you on an adventure on exploring certificate signing requestsTake a look at this CSR file [here](https://artifacts.picoctf.net/c/422/readmycert.csr).

#cryptography #wu
___
```
┌──(kali㉿oujisan)-[PicoCTF 2024 Below/Cryptography/367 - ReadMyCert/chall]
└─$ ls
readmycert.csr

┌──(kali㉿oujisan)-[PicoCTF 2024 Below/Cryptography/367 - ReadMyCert/chall]
└─$ file readmycert.csr
readmycert.csr: PEM certificate request
```

Untuk mengakses file CSR, kita bisa gunakan `openssl` berdasarkan temuan pada stack overflow ["How to decode a CSR File"](https://stackoverflow.com/questions/201070/how-to-decode-a-csr-file).
```
┌──(kali㉿oujisan)-[PicoCTF 2024 Below/Cryptography/367 - ReadMyCert/chall]
└─$ openssl req -text -in readmycert.csr
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN=picoCTF{read_mycert_373b4ab0}, name=ctfPlayer
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
```

```
picoCTF{read_mycert_373b4ab0}
```
