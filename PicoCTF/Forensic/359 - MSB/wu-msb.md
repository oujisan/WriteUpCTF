# MSB
[Link Challenge](https://play.picoctf.org/practice/challenge/359)

This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...Download the image [here](https://artifacts.picoctf.net/c/301/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)

#Forensic #png #steganography
___

Petunjuk pada soal terdapat pada judul yaitu, MSB atau Most Significant Bit. 

MSB atau Most Significant Bit adalah metode dalam Steganography untuk menyembunyikan pesan rahasia melalui bit awal pada Hex RGB.

Kemungkinan flag disembunyikan dengan metode tersebut. Gunakan script [sigBits](https://github.com/Pulho/sigBits) untuk ekstrak pesan tersembunyi.

Install modul yang diperlukan pada `requirement.txt` 
```
pip install Pillow
```

Jalankan stegBits
```
python sigBits.py -t=msb ..\..\Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
```

ouput  `.txt` akan berada pada `sigBits/`. Gunakan grep untuk mencari flag.
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Desktop/cli-tools/sigBits]
└─$ cat outputSB.txt | tr " " "\n" |grep -o "picoCTF{.*}"
picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_3a219174}
```

```
picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_3a219174}
```
