# 🔐 BTC HEX to WIF Private Key Converter

This simple Python script converts a **Bitcoin private key in hexadecimal (HEX)** format into **WIF (Wallet Import Format)**. It supports both **compressed** and **uncompressed** formats.

## 📜 What It Does

- Takes a private key in HEX format (e.g., `730FC235C1942C1AE`)
- Pads it to 32 bytes if necessary
- Converts it to the WIF format
- Prints the WIF private key string

## 🧪 Example

```python
import hashlib
import base58

def private_key_to_wif(hex_key, compressed=True):
    prefix = b'\x80'
    key_bytes = bytes.fromhex(hex_key)
    if compressed:
        key_bytes += b'\x01'
    extended_key = prefix + key_bytes
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    wif = base58.b58encode(extended_key + checksum)
    return wif.decode()

# Example usage:
hex_priv = "730FC235C1942C1AE"
hex_priv = hex_priv.rjust(64, '0')  # pad with zeros to full 32 bytes
wif = private_key_to_wif(hex_priv)
print(wif)
```

## 🧾 Output
```
L4RjWUyUf1Gc...  (your WIF key will vary)
```

## ⚙️ Requirements
No external dependencies! Just Python's standard library:
-hashlib
-base58 (make sure to install this with pip)

```
pip install base58
```
## 🔧 Options
Set compressed=False to generate an uncompressed WIF key.

Ensure your private key is exactly 64 hex characters (32 bytes). The script automatically pads it if it's shorter.

## 📂 Use Cases
- Brute-force or puzzle-solving workflows
- Key conversions during wallet development
- Educational purposes

## 🔒 Disclaimer
This script is for educational and research purposes only. Use responsibly. Do not use on live/private wallets unless you understand what you're doing.
