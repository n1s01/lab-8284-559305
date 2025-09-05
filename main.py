#!/usr/bin/env python3

import traceback
import sys
import secrets
import mimetypes
import os
import logging

# Configure audit logger
logger = logging.getLogger('audit')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('audit.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
if not logger.handlers:
    logger.addHandler(handler)

MAX_UPLOAD_SIZE = 5 * 1024 * 1024  # 5 MB
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.pdf'}

def generate_token(length=32):
    """Generate a secure random token of the given byte length and return it as a hex string."""
    token = secrets.token_hex(length)
    logger.info(f"Generated token of length {length}")
    return token

def validate_file_upload(file_path):
    """Validate uploaded file based on size and allowed extensions.

    Raises:
        ValueError: If the file does not exist, has a disallowed extension, or exceeds size limit.
    Returns:
        bool: True if validation passes.
    """
    if not os.path.isfile(file_path):
        raise ValueError("File does not exist.")
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Extension '{ext}' is not allowed.")
    size = os.path.getsize(file_path)
    if size > MAX_UPLOAD_SIZE:
        raise ValueError(f"File size {size} exceeds maximum allowed {MAX_UPLOAD_SIZE} bytes.")
    logger.info(f"File validated successfully: {file_path}")
    return True

def main():
    token = generate_token()
    print(f"Generated token: {token}")
    # Example placeholder for file validation:
    # validate_file_upload('path/to/uploaded_file.ext')

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
