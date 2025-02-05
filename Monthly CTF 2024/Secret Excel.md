#CTF #MonthlyCTF24 #Forensic #WriteUp #john

> **Flag:** `PC24{3xc3l_l33t_h4cks}`
> 
![secret_excel01.png](./img/secret_excel01.png)
### Write Up:
Lakukan brute force untuk menemukan password pada file. 
Extract hash file menuju ke `hash.txt`
```
office2john output-pymu.xlsx > hash.txt
```

Lakukan brute force menggunakan wordlist bawaan dari john
```
john hash.txt
```

![secret_excel00.png](./img/secret_excel00.png)
Setelah menunggu cukup lama password berhasil ditemukan.

Buka `output-pymu.xlsx` menggunakan Excel atau software lainnya dan masukkan password `active`.
![secret_excel02.png](./img/secret_excel02.png)

Ketika dicari menggunakan `CTRL + F` dengan keyword `PC24`.
![secret_excel03.png](./img/secret_excel03.png)
 Walaupun teks dari flag diwarnai putih, kita tetap bisa mencari dan melihatnya.
 Flag telah ditemukan.