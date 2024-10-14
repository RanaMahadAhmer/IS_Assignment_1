def decrypt(cipher_text, key):
    decrypted_text = ""
    keyword_repeated = (key * (len(cipher_text) // len(key) + 1))[:len(cipher_text)]
    for i in range(len(cipher_text)):
        if cipher_text[i] == " ":
            decrypted_text += cipher_text[i]

        else:
            char_base = ord('a') if cipher_text[i].islower() else ord('A')
            key_base = ord('a') if keyword_repeated[i].islower() else ord('A')
            letter_shift = (ord(cipher_text[i]) - char_base - (ord(keyword_repeated[i]) - key_base)) % 26
            decrypted_text += str(chr(letter_shift + char_base))

    return decrypted_text


cipher_text = "Usojcmqglc ce vpqtvixztnzc uull deayia mx khkzbemi uel qwgwlzbr"
key = "SECURITY"

decrypted_text = decrypt(cipher_text, key)
print("\n-------------------VIGENERE DECRYPTION-------------------\n")
print(f"CipherText: {cipher_text}")
print(f"DecrypText: {decrypted_text}\n")
