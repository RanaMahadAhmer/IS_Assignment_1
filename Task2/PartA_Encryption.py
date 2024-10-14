def encrypt(plain_text, key):
    cipher_text = ""
    keyword_repeated = (key * (len(plain_text) // len(key) + 1))[:len(plain_text)]
    for i in range(len(plain_text)):
        if plain_text[i] == " ":
            cipher_text += plain_text[i]
        else:
            char_base = ord('a') if plain_text[i].islower() else ord('A')
            key_base = ord('a') if keyword_repeated[i].islower() else ord('A')
            letter_shift = (ord(plain_text[i]) - char_base + ord(keyword_repeated[i]) - key_base) % 26
            cipher_text += str(chr(letter_shift + char_base))

    return cipher_text


plain_text = "Complexity in cryptography adds layers of intrigue and security"
key = "SECURITY"

cipher_text = encrypt(plain_text, key)
print("\n-------------------VIGENERE ENCRYPTION-------------------\n")
print(f"Plain Text: {plain_text}")
print(f"CipherText: {cipher_text}\n")
