# 450 - Verify
[Link Challenge](https://play.picoctf.org/practice/challenge/450?)

#PicoCTF2024 #Forensic #Easy #wu
___

Setelah masuk di dalam instance yang telah disediakan, terdapat list directory content berikut
```
ctf-player@pico-chall$ ls
checksum.txt  decrypt.sh  files
```

Dalam deskripsi soal, dijelaskan bahwa mereka menggunakan SHA-256 hash dengan checksum sebagai berikut:
```
ctf-player@pico-chall$ cat checksum.txt
b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2
```

> [!TIP]
> Cari tahu SHA-256 Hash dan Checksum.

Dalam directory `files`, terdapat 301 file dengan nilai unik
```
ctf-player@pico-chall$ cat files/0QFPjDGl
NyZbmzOjRRVev7keI8ndR4qRriMAxFynXefeMikB7mKgv3xBIhzbLOwo65uL8GC
```

Karena checksum sudah diketahui, cari file dalam directory `files` yang memiliki nilai hash sama dengan file `checksum.txt` menggunakan `sha256sum`[^1].
```
sha256sum files/* | grep -f checksum.txt
```

> [!NOTE]
> Checksum adalah nilai unik hasil SHA-256 Hash dari suatu file.

```
ctf-player@pico-chall$ sha256sum files/* | grep -f checksum.txt
b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2  files/451fd69b
```

Didapatkan file `451fd69b` memiliki nilai hash yang sama dengan `checksum.txt`. Jalankan `decrypt.sh` untuk melakukan dekripsi dan mendapatkan flag.
```
ctf-player@pico-chall$ ./decrypt.sh files/451fd69b
picoCTF{trust_but_verify_451fd69b}
```

[^1]: [sha256sum](https://sha256sum.com/).
