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
hex_priv = "YOUR_HEX_PRIV_KEY"
hex_priv = hex_priv.rjust(64, '0')  # pad with zeros to full 32 bytes
wif = private_key_to_wif(hex_priv)
print(wif)
