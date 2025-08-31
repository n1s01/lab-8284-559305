#!/usr/bin/env python3# Lazy load heavy module\nimport importlib\nheavy_module = None\n\ndef get_heavy_module():\n    global heavy_module\n    if heavy_module is None:\n        heavy_module = importlib.import_module(\"heavy_module\")\n    return heavy_module

print("Hello, World!")
