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


def decrypt(cipher_text, key):
    decrypted_text = ""
    keyword_repeated = (key * (len(cipher_text) // len(key) + 1))[:len(cipher_text)]
    for i in range(len(cipher_text)):
        if cipher_text[i] == " ":
            decrypted_text += cipher_text[i]
        elif cipher_text[i].islower():
            letter_shift = (ord(cipher_text[i]) - ord('a') - (ord(keyword_repeated[i]) - ord('a'))) % 26
            decrypted_text += str(chr(letter_shift + ord('a')))
        elif cipher_text[i].isupper():
            letter_shift = (ord(cipher_text[i]) - ord('A') - (ord(keyword_repeated[i]) - ord('A'))) % 26
            decrypted_text += str(chr(letter_shift + ord('A')))

    return decrypted_text


plain_text = ""
# ""Complexity in cryptography adds layers of intrigue and security"
key = ""
# ""SECURITY"

print("\n-------------------VIGENERE ENCRYPTION & DECRYPTION (VALID CHARS)-------------------\n")
while (True):
    plain_text = input("Enter Plain Text : ")
    if plain_text.replace(" ", "").isalpha():
        break
    else:
        print("Enter only alphabets\n")
        continue

while (True):
    key = input("Enter Key : ")
    if key.isalpha():
        break
    else:
        print("Enter only alphabets\n")
        continue
print(f"\n\nEnteredKey: {key}")
print(f"Plain Text: {plain_text}")
cipher_text = encrypt(plain_text, key)
print(f"CipherText: {cipher_text}")
decrypted_text = decrypt(cipher_text, key)
print(f"DecrypText: {decrypted_text}\n")
