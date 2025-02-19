# Transposition-trial
[Link Challenge](https://play.picoctf.org/practice/challenge/312)

Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.Download the corrupted message [here](https://artifacts.picoctf.net/c/192/message.txt).

#cryptography #wu
___
```
┌──(kali㉿oujisan)-[../PicoCTF 2024 Below/Cryptography/312 - transposition-trial/chall]
└─$ ls
message.txt
```

Diberikan file `message.txt` yang memiliki pesan sebagai berikut:
```
heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2
```

Tulisan diatas berisi susunan flag yang berantakan.

Dalam deskripsi terdapat keterangan bahwa kata pertama terdiri atas 3 kata, dari kata `heT` yang memungkinkan adalah `The` dan pada pola berikutnya `fl g as` kemungkinan adalah `flag`.

Dari pola diatas didapat bahwa setiap 3 kata, urutan ketiga akan dipindah ke depan.
Kita bikin script untuk memperbaiki flag diatas.
```
fix_flag = ''.join(flag[i+2] + flag[i:i+2] for i in range(0,len(flag),3))
```

Agar lebih mudah dilihat, kita jabarkan aja
```python
flag = 'heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2'

for i in range(0,len(flag),3):
	fix_flag = ''
	char = flag[i + 2] + flag[i, i +2]
	fix_flag += char
```

pertama kita ambil setiap 3 karakter diatas dengan `range(0,len(flag),3)` sebagai loncatan atau langkah index dan `flag[i+3]` untuk mengambil setiap 3 karakter.

Contohnya sebagai berikut
```python
x = 'aaAbbBccBddDeeEffFggG'
print([x[i:i+3] for i in range(0,len(x),3)])
```

Berhasil memecah setiap nilai abjad yang berisi 3 karakter dengan `x[i:i+3]`
```
PS C:\Users\Ouji\Desktop\code> py main.py
['aaA', 'bbB', 'ccB', 'ddD', 'eeE', 'ffF', 'ggG']
```

Disini kita pindahkan kapital A sebagai karakter ketiga menuju paling depan dengan mengganti `x[i:i+2]` menjadi `x[i+2] + x[i:i +2]`.
```
['Aaa', 'Bbb', 'Bcc', 'Ddd', 'Eee', 'Fff', 'Ggg']
```

Apabila diimplementasikan pada soal memiliki hasil seperti diatas
```
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_109AB02E}
```
