#CTF #MonthlyCTF24 #WriteUp #Forensic #ImageForensic

>**Flag:** `PC24{Exiftool_Reverse_C0mm4nd}`
### Write Up:
![kado_ultah01.png](./img/kado_ultah01.png)
karena kita diberi file photo, kita cek metadata dari photo tersebut.
![kado_ultah00.png](./img/kado_ultah00.png)

Variabel comment pada photo ini terlihat seperti base64. Kita coba decode string tersebut.
```
echo "fWRuNG1tMENfZXNyZXZlUl9sb290Zml4RXs0MkNQ" | base64 --decode
```

![kado_ultah02.png](./img/kado_ultah02.png)
 Flag terlihat terbalik, gunakan `rev` untuk membalik string tersebut.
```
echo "fWRuNG1tMENfZXNyZXZlUl9sb290Zml4RXs0MkNQ" | base64 --decode | rev
```

![kado_ultah03.png](./img/kado_ultah02.png)
