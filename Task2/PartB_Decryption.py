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


cipher_text = "Umidwgkafw wy pjknpcrtnhtw ooff xyuscu gr ebetvygc oyf kqaqftvl"
key = "SECURITY"

decrypted_text = decrypt(cipher_text, key)
print("\n-------------------VIGENERE DECRYPTION-------------------\n")
print(f"CipherText: {cipher_text}")
print(f"DecrypText: {decrypted_text}\n")
