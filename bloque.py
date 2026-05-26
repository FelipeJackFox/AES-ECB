# Diego Perea Leon - A01708350
# Cifrado y descifrado de un bloque de 16 bytes.

from operaciones import (
    add_round_key,
    sub_bytes, inv_sub_bytes,
    shift_rows, inv_shift_rows,
    mix_columns, inv_mix_columns
)


# Cifra un bloque de 16 bytes con la llave ya expandida
def encrypt_block(block, expanded_key):
    state = list(block)

    # Ronda inicial
    state = add_round_key(state, expanded_key, 0)

    # 9 rondas principales
    for r in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, expanded_key, r)

    # Ronda final (sin MixColumns)
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, expanded_key, 10)

    return bytes(state)


# Descifra un bloque de 16 bytes con la llave ya expandida
def decrypt_block(block, expanded_key):
    state = list(block)

    # Ronda inicial inversa
    state = add_round_key(state, expanded_key, 10)

    # 9 rondas en orden inverso
    for r in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, expanded_key, r)
        state = inv_mix_columns(state)

    # Ronda final inversa
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, expanded_key, 0)

    return bytes(state)
