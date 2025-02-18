# Interencdec
[Link Challenge](https://play.picoctf.org/practice/challenge/418)

Can you get the real meaning from this file.Download the file [here](https://artifacts.picoctf.net/c_titan/109/enc_flag).

#cryptography #rot #base64 #wu
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads]
└─$ ls
enc_flag 
```

Diberi file yang berisi `base64` chiper.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads]
└─$ cat enc_flag
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyMHdNakV5TnpVNGZRPT0nCg==
```

Gunakan perintah terminal `base64 -d`  atau web [CyberCheff](https://gchq.github.io/CyberChef/) untuk decrypt tulisan diatas.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads]
└─$ cat enc_flag | base64 -d
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX20wMjEyNzU4fQ=='
```

Terdapat enkripsi base64 lagi dalam bentuk bytes
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads]
└─$ python3 -c "print(b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX20wMjEyNzU4fQ=='.decode('utf-8'))" | base64 -d
wpjvJAM{jhlzhy_k3jy9wa3k_m0212758}
```

kayaknya ini ROT 13. Ternyata bukan, gunakan [CyberCheff](https://gchq.github.io/CyberChef/) untuk brute force ROT
```
Amount = 10: gztfTKW{trvjri_u3ti9gk3u_w0212758}
Amount = 11: haugULX{uswksj_v3uj9hl3v_x0212758}
Amount = 12: ibvhVMY{vtxltk_w3vk9im3w_y0212758}
Amount = 13: jcwiWNZ{wuymul_x3wl9jn3x_z0212758}
Amount = 14: kdxjXOA{xvznvm_y3xm9ko3y_a0212758}
Amount = 15: leykYPB{ywaown_z3yn9lp3z_b0212758}
Amount = 16: mfzlZQC{zxbpxo_a3zo9mq3a_c0212758}
Amount = 17: ngamARD{aycqyp_b3ap9nr3b_d0212758}
Amount = 18: ohbnBSE{bzdrzq_c3bq9os3c_e0212758}
Amount = 19: picoCTF{caesar_d3cr9pt3d_f0212758}
Amount = 20: qjdpDUG{dbftbs_e3ds9qu3e_g0212758}
```

Ketemu dah
```
picoCTF{caesar_d3cr9pt3d_f0212758}
```
