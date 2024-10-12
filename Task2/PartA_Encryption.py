def encrypt(plain_text, key):
    cipher_text = ""
    keyword_repeated = (key * (len(plain_text) // len(key) + 1))[:len(plain_text)]
    for i in range(len(plain_text)):
        if plain_text[i] == " ":
            cipher_text += plain_text[i]
        elif plain_text[i].islower():
            letter_shift = (ord(plain_text[i]) - ord('a') + ord(keyword_repeated[i]) - ord('a')) % 26
            cipher_text += str(chr(letter_shift + ord('a')))
        elif plain_text[i].isupper():
            letter_shift = (ord(plain_text[i]) - ord('A') + ord(keyword_repeated[i]) - ord('A')) % 26
            cipher_text += str(chr(letter_shift + ord('A')))

    return cipher_text


plain_text = "Complexity in cryptography adds layers of intrigue and security"
key = "SECURITY"

cipher_text = encrypt(plain_text, key)
print("\n-------------------BIFID ENCRYPTION-------------------\n")
print(f"Plain Text: {plain_text}")
print(f"CipherText: {cipher_text}")
