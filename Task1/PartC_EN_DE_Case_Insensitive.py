polybius_square = {
    'B': (1, 1), 'G': (1, 2), 'W': (1, 3), 'K': (1, 4), 'Z': (1, 5),
    'Q': (2, 1), 'P': (2, 2), 'N': (2, 3), 'D': (2, 4), 'S': (2, 5),
    'I': (3, 1), 'O': (3, 2), 'A': (3, 3), 'X': (3, 4), 'E': (3, 5),
    'F': (4, 1), 'C': (4, 2), 'L': (4, 3), 'U': (4, 4), 'M': (4, 5),
    'T': (5, 1), 'H': (5, 2), 'Y': (5, 3), 'V': (5, 4), 'R': (5, 5)
}

reverse_square = {v: k for k, v in polybius_square.items()}


def encrypt(plain_text):
    plain_text = plain_text.replace("J", "I").upper().replace(" ", "")
    coordinates = []

    for char in plain_text:
        if char in polybius_square:
            coordinates.append(polybius_square[char])
    rows = [row for row, col in coordinates]
    cols = [col for row, col in coordinates]
    merged = rows + cols
    produced_cipher_text = ""
    for i in range(0, len(merged), 2):
        pair = (merged[i], merged[i + 1])
        produced_cipher_text += reverse_square[pair]

    return produced_cipher_text


def decrypt(ciphertext):
    coords = []

    for char in ciphertext:
        if char in polybius_square:
            row, col = polybius_square[char]
            coords.append(row)
            coords.append(col)

    center = len(coords) // 2
    row_coords = coords[:center]
    col_coords = coords[center:]

    plain_text = ""
    for i in range(center):
        row = row_coords[i]
        col = col_coords[i]
        for key, value in polybius_square.items():
            if value == (row, col):
                plain_text += key
                break
    return plain_text


print("\n-------------------CASE INSENSITIVE BIFID ENCRYPTION & DECRYTPTION-------------------\n")
plain_text = "Even the strongest encryption can be undone by the faintest error"
cipher_text = encrypt(plain_text.upper())

print(f"Plain Text: {plain_text}")
print(f"CipherText: {cipher_text}")

decrypted_text = decrypt(cipher_text)
print(f"DecrytText: {decrypted_text}\n")
