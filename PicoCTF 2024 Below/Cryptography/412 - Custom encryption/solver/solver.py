enc_flag = [97965, 185045, 740180, 946995, 1012305, 21770, 827260, 751065, 718410, 457170, 0, 903455, 228585, 54425, 740180, 0, 239470, 936110, 10885, 674870, 261240, 293895, 65310, 65310, 185045, 65310, 283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]

# generator
def generator(g,x,p):
    return pow(g,x) % p
    # pow() berarti g pangkat x, lalu di modulus p 

# Decrypt shifting
def decrpyt(ciphertext, key):
    semi_cipher = []
    for char in ciphertext:
        semi_cipher.append(chr(char // (key * 311)))
    return semi_cipher

# Decrypt XOR
def dynamic_xor_decrypt(semi_ciphertext,text_key):
    plaintext = ''
    key_length = len(text_key)
    for i, char in enumerate(semi_ciphertext[::1]):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plaintext += decrypted_char
    return plaintext[::-1]

# Generate key
p, g = 97, 31
a, b= 88, 26 # diketahui nilai dari file enc_flag

u = generator(g,a,p)
v = generator(g,b,p)
key = generator(v,a,p)
# b_key = generator(u,b,p)

# if key == b_key:
#     print(True)
# else:
#     print(False)

# Decrypt
text_key = 'trudeau'
semi_cipher = decrpyt(ciphertext=enc_flag, key=key)
flag = dynamic_xor_decrypt(semi_ciphertext=semi_cipher,text_key=text_key)
print(flag)