#CTF #MonthlyCTF24 #WriteUp #WebExploitation #TypeJuggling

>**Flag:** `PC24{comparison_bug_is_very_easy_and_common_in_ctf_jungle}`
### Write Up:
Disini kita diberi source code yang bisa menjadi petunjuk
```php
<?php  
ini_set("error_reporting", 1);  
include "flag.php";  
  
if(isset($_GET['source'])){    highlight_file(__FILE__);  
    exit();  
}  
  
if(isset($_GET['inputsecret']))
	{$sec = $_GET['inputsecret'];
	// Secret is float number.   
	if($sec == $secret){  
        echo "<h2>Correct! Here's your flag: $flag</h2>";  
    } else {  
        echo "<h2>Incorrect secret.</h2>";  
    }  
}  
?>
```

Apabila kita perhatikan, pada code `if($sec == $secret)` menggunakan `==` yang merupakan kerentanan Type Juggling.

Gunakan [payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Type%20Juggling) untuk mempermudah pengerjaan. Coba satu-satu Magic hash dan masukkan ke dalam input.
