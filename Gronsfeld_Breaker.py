import itertools

def break_gronsfeld(ciphertext, key_length, wordlist=None):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    possible_keys = itertools.product(range(10), repeat=key_length)
    for key_tuple in possible_keys:
        key_digits = list(key_tuple)
        plaintext = ""
        for i, char in enumerate(ciphertext.upper()):
            if char in alphabet:
                shift = key_digits[i % key_length]
                idx = (alphabet.index(char) - shift) % 26
                plaintext += alphabet[idx]
            else:
                plaintext += char
        if wordlist:
            if any(word in plaintext for word in wordlist):
                print(f"Possible key: {''.join(map(str, key_digits))} => {plaintext}")
        else:
            print(f"Key: {''.join(map(str, key_digits))} => {plaintext}")

# Example usage:
# break_gronsfeld("KHOOR ZRUOG", 5, wordlist=["HELLO"])
