#CTF #MonthlyCTF24 #WriteUp #WebExploitation #SSRF

>**Flag:** `P2CTF{SSRF_Broo}`
### Soal:
![webkagebunshin0.png](./img/webkagebunshin0.png)
### Write Up:
Hint dalam soal yaitu, SSRF atau [[-Server Side Request Forgery (SSRF)]]. gunakan [payload](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery) untuk mempermudah.
![webkagebunshin1.png](./img/webkagebunshin1.png)
coba gunakan `http://127.0.0.1:80` atau `http://localhost:80`.
![webkagebunshin2.png](./img/webkagebunshin2.png)
Maka web akan terduplikasidan apabila mencoba memasukkan hal yang sama maka tidak terjadi apa-apa. Coba masukkan ``http://127.0.0.1:80/index.php`` maka akan muncul web yang sama.

Coba dengan `http://127.0.0.1:80/flag.txt` dan **FLAG HAS BEEN FOUND!!**
![webkagebunshin3.png](./img/webkagebunshin2.png)