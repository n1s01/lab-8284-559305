#!/usr/bin/env python3

import traceback
import sys

def main():
    print("Hello, World!")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
