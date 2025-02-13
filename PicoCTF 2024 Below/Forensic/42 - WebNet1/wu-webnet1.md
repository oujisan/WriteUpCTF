# WebNet1
[Link Challenge](https://play.picoctf.org/practice/challenge/42)

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/picopico.key). Recover the flag.

#DigitalForensic #pcap 
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/pico]
└─$ ls
capture.pcap  picopico.key
```

Ini adalah soal lanjutan dari WebNet0, jadi pembahasan lengkapnya tentang RSA Key bisa baca atau kunjungi writeup tersebut terlebih dahulu.

Lakukan analisa pada `TLS Stream`. Disini pada header `Pico-Flag` sudah berubah
```
HTTP/1.1 200 OK
Date: Fri, 23 Aug 2019 16:27:04 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Mon, 12 Aug 2019 16:47:05 GMT
ETag: "62-58fee462bf227-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Encoding: gzip
Pico-Flag: picoCTF{this.is.not.your.flag.anymore}
Content-Length: 100
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/css
```

Dan terdapat beberapa file image baru. ketika dicek, terdapat teks yang nampaknya adalah flag pada bagian awal stringnya.
```
......JFIF..............Exif..MM.*.................J...........R.(...........;.........Z................................picoCTF{honey.roasted.peanuts}......ICC_PROFILE.......lcms....mntrRGB XYZ .........).9acspAPPL...................................-lcms...............................................
```

Dan ternyata itu bukanlah dummy flag.
```
picoCTF{honey.roasted.peanuts}
```
