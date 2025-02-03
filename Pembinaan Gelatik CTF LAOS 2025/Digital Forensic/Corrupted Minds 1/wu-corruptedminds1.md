# Corrupted Minds 1
For the rest of Corrupted Minds series, please download and use this file:

[Link Challenges](https://binusianorg-my.sharepoint.com/personal/felix_alexander_binus_ac_id/_layouts/15/guestaccess.aspx?share=EqgEMqMso1VIjqms9NiwmzABR-OEP8LKCCB-YpGCKtn-kg&e=BbQa2w)

What's the partition table format used for this image?

Flag format: LAOS{nameofpartitiontableformat}

Example: LAOS{MBR}

#DigitalForensic #dd #imageForensic #ftk-imager #wu
___
Dalam zip terdapat file dengan format `.dd`
```
┌──(kali㉿oujisan)-[/mnt/d/PembinaanCTFGelatik25/DigitalForensic/CorruptedMinds1/Corrupted Minds]
└─$ ls
corrupted.dd
```

Untuk mendapatkan format tabel partisi yang digunakan, pakai `Exterro FTK Imager` untuk analisa lebih lanjut.
![gpt](Pembinaan%20Gelatik%20CTF%20LAOS%202025/Digital%20Forensic/Corrupted%20Minds%201/img/gpt.png)
Seperti yang dapat terlihat jika format tabel partisi dari image tersebut adalah `GPT`

> **LAOS{GPT}**