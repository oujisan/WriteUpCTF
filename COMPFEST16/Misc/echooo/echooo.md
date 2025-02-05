#CTF #COMPFEST16 #COMPFESTHackingClass #Miscellaneous #WriteUp 

>**Flag**: `flag`
### Write Up:
Pada deskripsi soal kita telah diberi hint jika karakter `?` mewakili satu karakter string. 
`/???/???` mewakili direktori dengan 3 kata. Tujuan kita adalah menemukan `/bin/cat` dan menjalankannya untuk menampilkan `flag.txt` yang diwakili oleh `????.???`.

simbol `;` mewakili `exec()`, untuk menemukan flag kita cukup dengan syntax berikut
```
; /???/??? ????.???
```

(Server soal di tutup, jadi tidak ada gambar)