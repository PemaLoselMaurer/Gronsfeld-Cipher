def gronsfeld_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    key_digits = [int(d) for d in str(key)]
    for i, char in enumerate(plaintext.upper()):
        if char in alphabet:
            shift = key_digits[i % len(key_digits)]
            idx = (alphabet.index(char) + shift) % 26
            ciphertext += alphabet[idx]
        else:
            ciphertext += char
    return ciphertext

def gronsfeld_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""
    key_digits = [int(d) for d in str(key)]
    for i, char in enumerate(ciphertext.upper()):
        if char in alphabet:
            shift = key_digits[i % len(key_digits)]
            idx = (alphabet.index(char) - shift) % 26
            plaintext += alphabet[idx]
        else:
            plaintext += char
    return plaintext

# Example usage:
# encrypted = gronsfeld_encrypt("HELLO WORLD", 31415)
# decrypted = gronsfeld_decrypt(encrypted, 31415)

