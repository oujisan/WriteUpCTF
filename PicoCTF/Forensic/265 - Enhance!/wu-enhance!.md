	# Enhance!
[Link Challenge](https://play.picoctf.org/practice/challenge/265)

Download this image file and find the flag.
- [Download image file](https://artifacts.picoctf.net/c/102/drawing.flag.svg)

#Forensic #wu #Strings 
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
drawing.flag.svg
```

Setelah dicek pada `file`, `xxd`, `exiftool`, `binwalk` aman saja. Waktu menggunakan `strings` langsung digrep "pico" juga tidak ada. Jadi, untuk memastikan langsung dibuka saja.

```
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3748">p </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08942"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3754">i </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09383"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3756">c </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09824"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3758">o </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10265"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3760">C </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10706"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3762">T </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11147"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3764">F { 3 n h 4 n </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11588"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3752">c 3 d _ d 0 a 7 5 7 b f }</tspan></text>
```

Ternyata pada bagian bawah terdapat potongan flag yang disusun kebawah. satukan aja pakai terminal
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ strings drawing.flag.svg | grep 'id="tspan.*">' | awk -F '[><]' '{print $2}' | tr -d "\n "
picoCTF{3nh4nc3d_d0a757bf}
```

```
picoCTF{3nh4nc3d_d0a757bf}
```
