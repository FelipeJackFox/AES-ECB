# Regina Franco Gutierrez - A01352605
# Padding y modo ECB.

from expansion_llave import expand_key
from bloque import encrypt_block, decrypt_block


# Agrega un 0x01 al final y rellena con 0x00 hasta completar 16 bytes
def apply_padding(data):
    missing = 16 - (len(data) % 16)
    data = data + bytes([0x01])
    for i in range(missing - 1):
        data = data + bytes([0x00])
    return data


# Quita los 0x00 finales y el 0x01 marcador
def remove_padding(data):
    i = len(data) - 1
    while i >= 0 and data[i] == 0x00:
        i = i - 1
    if i >= 0 and data[i] == 0x01:
        return data[:i]
    return data


# Cifrado ECB: bloque por bloque, sin encadenamiento
def encrypt_ecb(data, key):
    expanded_key = expand_key(key)
    data = apply_padding(data)
    result = bytes()
    for i in range(0, len(data), 16):
        block = data[i:i+16]
        result = result + encrypt_block(block, expanded_key)
    return result


# Descifrado ECB
def decrypt_ecb(data, key):
    expanded_key = expand_key(key)
    result = bytes()
    for i in range(0, len(data), 16):
        block = data[i:i+16]
        result = result + decrypt_block(block, expanded_key)
    return remove_padding(result)
