# Diego Perea Leon - A01708350
# Operaciones internas de AES: SubBytes, ShiftRows, MixColumns y sus inversas.

from tablas import SBOX, RSBOX, M2, M3, M9, M11, M13, M14


# XOR del bloque con la llave de ronda correspondiente
def add_round_key(state, expanded_key, round_num):
    new = []
    start = round_num * 16
    for i in range(16):
        new.append(state[i] ^ expanded_key[start + i])
    return new


# Sustituye cada byte usando la SBOX
def sub_bytes(state):
    new = []
    for i in range(16):
        new.append(SBOX[state[i]])
    return new


def inv_sub_bytes(state):
    new = []
    for i in range(16):
        new.append(RSBOX[state[i]])
    return new


# Recorre las filas del bloque hacia la izquierda
def shift_rows(s):
    return [s[0],  s[5],  s[10], s[15],
            s[4],  s[9],  s[14], s[3],
            s[8],  s[13], s[2],  s[7],
            s[12], s[1],  s[6],  s[11]]


def inv_shift_rows(s):
    return [s[0],  s[13], s[10], s[7],
            s[4],  s[1],  s[14], s[11],
            s[8],  s[5],  s[2],  s[15],
            s[12], s[9],  s[6],  s[3]]


# Mezcla las columnas usando las tablas M2 y M3
def mix_columns(s):
    out = [0] * 16
    for i in range(0, 16, 4):
        a = s[i]
        b = s[i+1]
        c = s[i+2]
        d = s[i+3]
        out[i]   = M2[a] ^ M3[b] ^ c ^ d
        out[i+1] = a ^ M2[b] ^ M3[c] ^ d
        out[i+2] = a ^ b ^ M2[c] ^ M3[d]
        out[i+3] = M3[a] ^ b ^ c ^ M2[d]
    return out


def inv_mix_columns(s):
    out = [0] * 16
    for i in range(0, 16, 4):
        a = s[i]
        b = s[i+1]
        c = s[i+2]
        d = s[i+3]
        out[i]   = M14[a] ^ M11[b] ^ M13[c] ^ M9[d]
        out[i+1] = M9[a]  ^ M14[b] ^ M11[c] ^ M13[d]
        out[i+2] = M13[a] ^ M9[b]  ^ M14[c] ^ M11[d]
        out[i+3] = M11[a] ^ M13[b] ^ M9[c]  ^ M14[d]
    return out
