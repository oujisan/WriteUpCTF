# subtitution0
[Link Challenge](https://play.picoctf.org/practice/challenge/307)

A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?Download the message [here](https://artifacts.picoctf.net/c/154/message.txt).

#cryptography #wu
___
```
┌──(kali㉿oujisan)-[307 - subtitution0]
└─$ cat message.txt
ZGSOCXPQUYHMILERVTBWNAFJDK

Qctcnrel Mcptzlo ztebc, fuwq z ptzac zlo bwzwcmd zut, zlo gtenpqw ic wqc gccwmc
xtei z pmzbb szbc ul fqusq uw fzb clsmebco. Uw fzb z gcznwuxnm bsztzgzcnb, zlo, zw
wqzw wuic, nlhlefl we lzwntzmubwb—ex sentbc z ptczw rtukc ul z bsuclwuxus reulw
ex aucf. Wqctc fctc wfe tenlo gmzsh brewb lczt elc cjwtciuwd ex wqc gzsh, zlo z
melp elc lczt wqc ewqct. Wqc bszmcb fctc cjsccoulpmd qzto zlo pmebbd, fuwq zmm wqc
zrrcztzlsc ex gntlubqco pemo. Wqc fcupqw ex wqc ulbcsw fzb actd tcizthzgmc, zlo,
wzhulp zmm wqulpb ulwe selbuoctzwuel, U senmo qztomd gmzic Ynruwct xet qub eruluel
tcbrcswulp uw.

Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX}
```

Disini kita gunakan web [dcode.fr](https://www.dcode.fr/monoalphabetic-substitution) subsitution cipher untuk decrypt pesan dengan knowing subtitution alphabet yaitu `ZGSOCXPQUYHMILERVTBWNAFJDK`.

dan begitulah
```
Hereupon Legrand arose, with a grave and stately air, and brought me the beetle  
from a glass case in which it was enclosed. It was a beautiful scarabaeus, and, at  
that time, unknown to naturalists--of course a great prize in a scientific point  
of view. There were two round black spots near one extremity of the back, and a  
long one near the other. The scales were exceedingly hard and glossy, with all the  
appearance of burnished gold. The weight of the insect was very remarkable, and,  
taking all things into consideration, I could hardly blame Jupiter for his opinion  
respecting it.  
  
The flag is: picoCTF{5UB5717U710N_3V0LU710N_357BF9FF}
```