# DarkComet 1
For the rest of DarkComet series challenge, you can download from the following file: `https://binusianorg-my.sharepoint.com/personal/felix_alexander_binus_ac_id/_layouts/15/guestaccess.aspx?share=EiA_PvWflgxHq8daNfsiT88B0Pdj28WlAEB-APgyIByK8Q&e=AHS1bJ`

I think a DarkComet malware infects my device!

This malware is pretty sus since it uses a legit services and spawns a malicious child process and creates a folder. What's the name of that folder?

Flag format: LAOS{nameoffolder}
Example: LAOS{DeeskTop}

#DigitalForensic #pml #dmp
___
Terdapat 2 file dengan ekstensi `.dmp` dan `.pml` pada file `Zeno.zip` yang diberikan
```
┌──(kali㉿oujisan)-[/mnt/d/PembinaanCTFGelatik25/DigitalForensic/DarkComet1/Zeno]
└─$ ls
sample.dmp  sample.PML
```

Cari terlebih dahulu informasi mengenai malware Dark Comet yang telah disebut dalam deskripsi soal dan memahami bagaimana cara kerjanya.
>[!NOTE]
>Dark Comet adalah Aplikasi *Remote Access Trojan (RAT)* yang memungkinkan berjalan di latar belakang dan secara diam-diam mengambil informasi tentang sistem, informasi kredensial user, dan aktivitas network[^1].

Biasanya malware Dark Comet menyalin dirinya ke dalam target sistem dalam bentuk `exe` atau executable program. 
> [!NOTE]
> `.dmp` atau *dump file* - menyimpan *snapshot* atau rekaman kondisi sistem atau aplikasi
> `.pml` atau *Performance Monitor Log*  - menyimpan data kinerja sistem.
> Kedua file diatas biasanya digunakan untuk menganalisis masalah dan memperbaikinya.

>[!TIP]
> Analisa `.dmp` dapat menggunakan software yang bernama `WinDbg` dari Microsoft[^2]
> Analisa - `.pml` dapat menggunakan `ProcMon` dari Microsoft[^3]

Lakukan analisa terhadap kedua file yang telah ada.

[^1]: https://www.malwarebytes.com/blog/detections/backdoor-darkcomet
[^2]: https://www.xda-developers.com/how-to-open-dmp-files/
[^3]: https://filext.com/file-extension/PML