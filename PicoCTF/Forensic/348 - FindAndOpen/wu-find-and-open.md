# FindAndOpen
[Link Challenge](https://play.picoctf.org/practice/challenge/348)

Someone might have hidden the password in the trace file.Find the key to unlock [this file](https://artifacts.picoctf.net/c/493/flag.zip). [This tracefile](https://artifacts.picoctf.net/c/493/dump.pcap) might be good to analyze.

#Forensic #wu #steganography #pcap
___
Diberi 2 file 
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ ls
dump.pcap  flag.zip
```

Pertama, analisa file pacp untuk mendapatkan password membuka zip.

Terdapat beberapa clue pada info `ethernet II` seperti
- "Flying on Ethernet secret: Is this the flag"
- "Could the flag have been splitted?"
- "Maybe try checking the other file"

Serta kita diberi potongan base64 dibawah
- iBwaWNvQ1RGe
- PBwaWUvQ1RGe1
- AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
- PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS

rakit potongan base64 dengan akhiran bagian `AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=` 
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ echo "iBwaWNvQ1RGePBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJSPBwaWUvQ1RGe1AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=" | base64 -d
�␦X����<␦YK������m�䍠(��TR
                          4�I �(�IH�pie/CTF{P�<���This is the secret: picoCTF{R34DING_LOKd_
```

Terdapat potongan dari flag.

Selanjutnya adalah membuka file zip, dimana setelah mencari dan mencoba-coba password dari zip tersebut adalah potongan flag yang didapat dari pcap. `picoCTF{R34DING_LOKd_`

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ unzip -P "picoCTF{R34DING_LOKd_" flag.zip
Archive:  flag.zip
 extracting: flag
```

Buka dah
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/chall]
└─$ cat flag
picoCTF{R34DING_LOKd_fil56_succ3ss_419835ef}
```

```
picoCTF{R34DING_LOKd_fil56_succ3ss_419835ef}
```