# Santiago Saldana Subias - A01708446
# Expansion de llave AES-128: pasa de 16 bytes a 176 bytes.

from tablas import SBOX, RCON


def expand_key(key):
    exp = list(key)
    n = 16
    round_num = 1

    while n < 176:
        # Tomamos los ultimos 4 bytes
        t0 = exp[n - 4]
        t1 = exp[n - 3]
        t2 = exp[n - 2]
        t3 = exp[n - 1]

        # Cada 16 bytes se aplica rotacion + sbox + rcon
        if n % 16 == 0:
            # Rotacion a la izquierda
            r0 = t1
            r1 = t2
            r2 = t3
            r3 = t0

            # Sustitucion por SBOX
            t0 = SBOX[r0]
            t1 = SBOX[r1]
            t2 = SBOX[r2]
            t3 = SBOX[r3]

            # XOR con RCON
            t0 = t0 ^ RCON[round_num]
            round_num = round_num + 1

        # Generar los 4 bytes nuevos
        exp.append(exp[n - 16] ^ t0)
        exp.append(exp[n - 15] ^ t1)
        exp.append(exp[n - 14] ^ t2)
        exp.append(exp[n - 13] ^ t3)
        n = n + 4

    return exp
