

# zadanie 6 i 7

def Cesar_cipher(key):
    alfabet = "a, ą, b, c, ć, d, e, ę, f, g, h, i, j, k, l, ł, m, n, ń, o, ó, p, r, s, ś, t, u, w, y, z, ź, ż"
    alfabet_arr = alfabet.split(", ")
    CESAR_CIPHER = {}
    for i in range(len(alfabet_arr)):
        if i < len(alfabet_arr) - key:
            CESAR_CIPHER[alfabet_arr[i]] = alfabet_arr[i + key]
        else:
            CESAR_CIPHER[alfabet_arr[i]] = alfabet_arr[(i + key) % 32]
    return CESAR_CIPHER

def encrypt(dict, message):
    encrypted = ""
    message = message.lower()
    for letter in message:
        if letter in [" ", ","]:
            encrypted = encrypted + letter
            continue
        else:
           encrypted = encrypted + dict[letter]

    return encrypted

def decrypt(dict, encrypted):
    decrypted = ""
    for letter in encrypted:
        if letter in [" ", ","]:
            decrypted = decrypted + letter
            continue
        else:
            for key, value in dict.items():
                if value == letter:
                    decrypted = decrypted + key

    return decrypted


message = "MĘŻNY BĄDŹ, CHROŃ PUŁK TWÓJ I SZCZEŚĆ FLAG"

encrypted = encrypt(Cesar_cipher(3), message)
print(encrypted)
# print(encrypt(Cesar_cipher(-3), encrypted))
decrypted = decrypt(Cesar_cipher(3), encrypted)
print(decrypted)










