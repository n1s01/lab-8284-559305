#!/usr/bin/env python3

import traceback
import sys
import secrets

def generate_token(length=32):
    """Generate a secure random token of the given byte length and return it as a hex string."""
    return secrets.token_hex(length)

def main():
    token = generate_token()
    print(f"Generated token: {token}")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
