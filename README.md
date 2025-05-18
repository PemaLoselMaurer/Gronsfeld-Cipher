# Gronsfeld Cipher

Python implementation of the Gronsfeld cipher, including encryption, decryption, and a brute-force breaker.

## Features

- **Encrypt** plaintext using the Gronsfeld cipher.
- **Decrypt** ciphertext using the Gronsfeld cipher.
- **Break** Gronsfeld cipher ciphertext by brute-forcing possible keys.

## Usage

### Encryption & Decryption

Use `Gronsfeld_cipher.py` to encrypt or decrypt messages from the command line:

```sh
python Gronsfeld_cipher.py encrypt "HELLO WORLD" 31415
python Gronsfeld_cipher.py decrypt "KHOOR ZRUOG" 31415
```

Or use the functions in your Python code:

```python
from Gronsfeld_cipher import gronsfeld_encrypt, gronsfeld_decrypt

encrypted = gronsfeld_encrypt("HELLO WORLD", 31415)
decrypted = gronsfeld_decrypt(encrypted, 31415)
```

### Breaking the Cipher

Use `gronsfeld_breaker.py` to brute-force possible keys:

```python
from gronsfeld_breaker import break_gronsfeld

# Try all 5-digit keys and print results containing "HELLO"
break_gronsfeld("KHOOR ZRUOG", 5, wordlist=["HELLO"])
```

## Files

- `Gronsfeld_cipher.py` — Encryption and decryption functions.
- `gronsfeld_breaker.py` — Brute-force breaker for the cipher.


