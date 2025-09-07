#!/usr/bin/env python3

import base64
import hashlib

def _derive_key(key: str, length: int = 32) -> bytes:
    """Derive a fixed‑length key from the given string using SHA‑256."""
    digest = hashlib.sha256(key.encode()).digest()
    return digest[:length]

def encrypt(plaintext: bytes, key: str) -> str:
    """Encrypt bytes with a symmetric key and return a URL‑safe Base64 string.

    This uses a simple XOR operation with a derived key. It is NOT suitable for
    production use but demonstrates basic encryption/decryption logic without
    external dependencies.
    """
    key_bytes = _derive_key(key)
    ciphertext = bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(plaintext))
    return base64.urlsafe_b64encode(ciphertext).decode()

def decrypt(ciphertext_b64: str, key: str) -> bytes:
    """Decrypt a Base64‑encoded ciphertext using the same symmetric key.

    Returns the original plaintext bytes.
    """
    key_bytes = _derive_key(key)
    ciphertext = base64.urlsafe_b64decode(ciphertext_b64.encode())
    plaintext = bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(ciphertext))
    return plaintext

if __name__ == "__main__":
    # Simple demonstration
    secret_key = "my-secret-key"
    message = b"Hello, Encryption!"
    enc = encrypt(message, secret_key)
    print(f"Encrypted: {enc}")
    dec = decrypt(enc, secret_key)
    print(f"Decrypted: {dec.decode()}")
