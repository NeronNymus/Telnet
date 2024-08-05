#!/usr/bin/env python3

import sys

if len(sys.argv) != 1:
    print("Usage: ./bytes.py")
    sys.exit(0)

print("[!] Write encoded data. Finish using Ctrl+D")
text = str(sys.stdin.read())

encoding_text = text.encode('ascii')

print(f"[!] Encoded text: {encoding_text}")

# From a list of integers (0-255)
#var = bytes([104, 101, 108, 108, 111])
#print(var)