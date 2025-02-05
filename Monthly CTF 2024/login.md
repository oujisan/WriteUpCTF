#CTF #MonthlyCTF24 #Forensic #john #WriteUp 

>**Flag:** `PC24{paten_kali_kau_bang}`

![monthlyctf-login00.png](./img/monthlyctf-login00.png)
### Write Up:
File `congrats.zip` dilindungi dengan password serta dalam `hint.txt` kita tidak menemukan informasi yang berguna. 
![monthlyctf-login01.png](./img/monthlyctf-login01.png)
Jadi kita akan brute force zip menggunakan `john`.

Extract hash dari `congrats.zip` ke dalam `congrats_hash.txt`
```
zip2john congrats.zip > congrats_hash.txt
```
![monthlyctf-login02.png](./img/monthlyctf-login02.png)

Brute Force password menggunakan wordlist bawaan dari `john`
```
john congrats_hash.txt
```
![monthlyctf-login03.png](./img/monthlyctf-login03.png)
Ditemukan password dari file zip tersebut adalah `imissyou`.

Extract file zip menggunakan `unzip` dengan password diatas (`-P`) dan dalam folder baru (`-d`) untuk memudahkan melihat hasil unzip.
![monthlyctf-login04.png](./img/monthlyctf-login04.png)

Cek `flag.txt`
![monthlyctf-login05.png](./img/monthlyctf-login05.png)
```
cat flag.txt
```

Ternyata ini adalah flag palsu. Kita cek `sadboy.jpg`
![monthlyctf-login06.png](./img/monthlyctf-login06.png)

Gunakan `display` untuk menampilkan gambar menggunakan `ImageMagick`.
```
display sadboy.jpg
```

![monthlyctf-login08.png](./img/monthlyctf-login08.png)

Flag telah ditemukan