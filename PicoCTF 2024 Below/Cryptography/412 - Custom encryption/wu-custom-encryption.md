# Custom Encryption
[Link Challenge](https://play.picoctf.org/practice/challenge/412)

Can you get sense of this code file and write the function that will decode the given encrypted file content.Find the encrypted file here [flag_info](https://artifacts.picoctf.net/c_titan/93/enc_flag) and [code file](https://artifacts.picoctf.net/c_titan/93/custom_encryption.py) might be good to analyze and get the flag.

#cryptography #wu #xor 
___
```
┌──(kali㉿oujisan)-[/mnt/d/PicoCTF/Cryptography/customEncryption]
└─$ ls
custom_encryption.py  enc_flag
```

Isi dari file `enc_flag`.
```
┌──(kali㉿oujisan)-[/mnt/d/PicoCTF/Cryptography/customEncryption]
└─$ cat enc_flag
a = 88
b = 26
cipher is: [97965, 185045, 740180, 946995, 1012305, 21770, 827260, 751065, 718410, 457170, 0, 903455, 228585, 54425, 740180, 0, 239470, 936110, 10885, 674870, 261240, 293895, 65310, 65310, 185045, 65310, 283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]
```

dalam `custom_encryption.py` berisi enkripsi kustom yang memanfaatkan XOR cipher.

Ketika dianalisa kita dapat menyimpulkan proses enkripsinya sebagai berikut:
`plaintext -> generate key -> xor cipher -> custom cipher -> ciphertext`

Langkah pertama yang harus kita lakukan adalah menemukan key yang cocok atau sama digunakan untuk enkripsi flag.

Untuk menemukan key, kita memerlukan nilai `p, g` yang diketahui pada file python dan `a, b` yang ada pada file `enc_flag` yang akan dioperasikan pada function `generator()` yang berisi `pow(g,x) % p`

```python
def generator(g,x,p):
    return pow(g,x) % p
    # pow() berarti g pangkat x, lalu di modulus p

# Generate key
p, g = 97, 31
a, b = 88, 26

u = generator(g,a,p)
v = generator(g,b,p)
key = generator(v,a,p)
b_key = generator(u,b,p)
```

```
key = 35
```

Apabila di print, kita mendapatkan nilai key adalah 35.

Setelah itu terdapat pengecekan hasil dari `key` dan `b_key` dimana jika value dari kedua variabel sama maka hasil key adalah valid, jika tidak maka tidak valid. Pastikan nilai dari pengecekan tersebut `True` atau sama.

Selanjutnya membuat algoritma decrypt pada method `encrypt()`
```python
def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key * 311)))
    return cipher
```

- `ord()`, merupakan method untuk mengembalikan string menjadi nilai Unicode.
	Karena ciphertext yang kita terima adalah berupa angka jadi kita tidak perlu mengembalikannya ke dalam bentuk stringnya terlebih dahulu.
- Kebalikan dari operasi `(ord(char) * key*311)` adalah `char // (key * 311)`
	bayangkan jika persamaan diatas seperti berikut `x = a * b * c` dimana nilai `x` hasil, `ord(char)` adalah `a`, key adalah `b` dan 311 adalah `c`.
	Tujuan kita adalah mengetahui nilai `a`, jadi lebih kurang operasinya akan menjadi seperti berikut:
	`a = x / b / c` atau dapat ditulis `a = x / (b * c)`.
	lalu kita gunakan floor division (`//`) agar nilai nya berupa integer dengan dibulatkan ke bawah.
- Lalu yang terakhir kita ubah nilai Unicode menjadi sebuah karakter atau string menggunakan `chr()`. Nilai dari `chr()` harus berupa integer maka dari itu kita gunakan floor division.


Berikut adalah algoritma decrypt dari method diatas
```python
def decrpyt(ciphertext, key):
    semi_cipher = []
    for char in ciphertext:
        semi_cipher.append(chr(char // (key * 311)))
    return semi_cipher
```

```
['\t', '\x11', 'D', 'W', ']', '\x02', 'L', 'E', 'B', '*', '\x00', 'S', '\x15', '\x05', 'D', '\x00', '\x16', 'V', '\x01', '>', '\x18', '\x1b', '\x06', '\x06', '\x11', '\x06', '\x1a', '3', ' ', '1', '\x1a', '\x07', '\x0c', '\x11']
```

Langkah berikutnya adalah melakukan decrypt pada `dynamic_xor_decrypt`. Karena sifat dari XOR itu sendiri kita tidak perlu mengubah apapun dalam XOR ini. karena `a ^ b = c` itu sama aja dengan `b ^ a = c`, `c ^ b = a`, `c ^ a = b`. Kita hanya perlu menyesuaikan variabelnya saja.

Untuk `key` pada XOR, menggunakan key character yang berada pada bawah code yang ada yaitu `trudeau`.

Pada line `for i, char in enumerate(semi_ciphertext[::-1]):` ubah `-1` menjadi `1`. Karena pada enkripsi menggunakan urutan dari belakang, jadi pada decrypt kita gunakan urutan dari depan.

```python
def dynamic_xor_decrypt(semi_ciphertext,text_key):
    plaintext = ''
    key_length = len(text_key)
    
    for i, char in enumerate(semi_ciphertext[::1]):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plaintext += decrypted_char
    return plaintext
```

```
PS D:\PicoCTF\Cryptography\customEncryption> py .\solver\solver.py
}c138c910_d6tp0rc2d_motsuc{FTCocip
```

Pola dari flag sudah terlihat, susun `plaintext` agar berjalan dari belakang `plaintext[::-1]`
```
PS D:\PicoCTF\Cryptography\customEncryption> py .\solver\solver.py
picoCTF{custom_d2cr0pt6d_019c831c}
```