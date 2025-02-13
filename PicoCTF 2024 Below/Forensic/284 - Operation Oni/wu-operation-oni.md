# Operation Oni
[Link Challenge](https://play.picoctf.org/practice/challenge/284)

Download this disk image, find the key and log into the remote machine.Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
- [Download disk image](https://artifacts.picoctf.net/c/71/disk.img.gz)
- Remote machine: `ssh -i key_file -p xxxxx ctf-player@saturn.picoctf.net`

#DigitalForensic #wu #ImageForensic 
___
```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/pico/disk.img]
└─$ ls
disk.img
```

Analisa disk menggunakan Autopsy atau FTK Imager.

pada directory root, terdapat directori dan file yang bisa dianalisa yaitu, `.ssh` dan `.ash_history` yang berisi history commandline yang digunakan user.

dalam directtory `.ssh` terdapat openSSH private key. Ekstrak key file dan jalankan pada instace remote machine.

```
┌──(kali㉿oujisan)-[/mnt/c/Users/Ouji/Downloads/pico/disk.img]
└─$ ssh -i id_ed25519 -p 52876 ctf-player@saturn.picoctf.net
The authenticity of host '[saturn.picoctf.net]:52876 ([13.59.203.175]:52876)' can't be established.
ED25519 key fingerprint is SHA256:XBSvB1lk28EctsAVdKJtsl0A7C5bonqPrvHCYH8aEy4.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:6: [hashed name]
    ~/.ssh/known_hosts:7: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[saturn.picoctf.net]:52876' (ED25519) to the list of known hosts.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0777 for 'id_ed25519' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "id_ed25519": bad permissions
ctf-player@saturn.picoctf.net's password:
```

OK, disini gagal untuk masuk menggunakan private key dikarenakan permission dari file key terlalu terbuka atau `777`. 

Karena disini aku menggunakan WSL, maka file akan dipindahkan terlebih dahulu ke dalam directory home untuk memudahkan mengganti permission.

Ubah permission menjadi `600`. 
```
sudo chmod 600 id_ed25519
```

dan jalankan kembali instance.
```
┌──(kali㉿oujisan)-[~]
└─$ ssh -i id_ed25519 -p 56723 ctf-player@saturn.picoctf.net
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.5.0-1023-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$
```

Kita berhasil masuk dan terdapat `flag.txt` didalamnya, bukak aja
```
ctf-player@challenge:~$ cat flag.txt
picoCTF{k3y_5l3u7h_af277f77}
```

```
picoCTF{k3y_5l3u7h_af277f77}
```