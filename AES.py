# Felipe Pacheco Zamorano - A01713238
#
# Santiago Saldana Subias  - A01708446
# Diego Perea Leon         - A01708350
# Regina Franco Gutierrez  - A01352605
#
# Programa principal: menu, lectura/escritura de archivos.

import os
from cifrado import encrypt_ecb, decrypt_ecb


# Pide un numero entero al usuario hasta que lo de bien
def force_answer_int(options, question):
    while True:
        print(options, end='')
        answer = input("\n" + question + ": ")
        try:
            if '.' in answer:
                print("\nError. Usa un numero entero (sin decimales).")
                continue
            answer = int(answer.replace(' ', ''))
            return answer
        except ValueError:
            print("\nError. Selecciona un numero.")


# Pide un nombre de archivo valido y verifica que exista
def force_valid_file(question):
    while True:
        file_name = input("\n" + question + ": ").strip()
        if os.path.exists(file_name):
            return file_name
        print("\nError. No se encontro el archivo. Revisa nombre y extension.")


# Pide la llave en hex o usa la default si se aprieta Enter
def force_valid_key(question):
    while True:
        print("\n" + question)
        print("O presiona Enter para usar la llave por defecto (FF 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F).")
        text = input("Llave: ")

        if text.strip() == "":
            print("\nUsando llave por defecto...")
            return bytes.fromhex("FF0102030405060708090A0B0C0D0E0F")

        clean = text.replace(" ", "")

        if len(clean) != 32:
            print("\nError. La llave debe tener exactamente 32 caracteres (16 bytes).")
            continue

        try:
            return bytes.fromhex(clean)
        except ValueError:
            print("\nError. La llave solo puede contener caracteres hexadecimales (0-9, A-F).")


def main():
    print(r"""
                         /$$$$$$  /$$$$$$$$  /$$$$$$        /$$$$$$$$  /$$$$$$  /$$$$$$$
                        /$$__  $$| $$_____/ /$$__  $$      | $$_____/ /$$__  $$| $$__  $$
 /$$$$ /$$$$ /$$$$      | $$  \ $$| $$      | $$  \__/      | $$      | $$  \__/| $$  \ $$       /$$$$ /$$$$ /$$$$
|____/|____/|____/      | $$$$$$$$| $$$$$   |  $$$$$$       | $$$$$   | $$      | $$$$$$$       |____/|____/|____/
 /$$$$ /$$$$ /$$$$      | $$__  $$| $$__/    \____  $$      | $$__/   | $$      | $$__  $$       /$$$$ /$$$$ /$$$$
|____/|____/|____/      | $$  | $$| $$       /$$  \ $$      | $$      | $$    $$| $$  \ $$      |____/|____/|____/
                        | $$  | $$| $$$$$$$$|  $$$$$$/      | $$$$$$$$|  $$$$$$/| $$$$$$$/
                        |__/  |__/|________/ \______/       |________/ \______/ |_______/
""")

    while True:
        print("\n\nSelecciona el tipo de operacion.")
        option = force_answer_int("\n1) Cifrar un archivo.\n2) Descifrar un archivo.\n3) Salir\n", "Opcion (1-3)")

        if option == 1 or option == 2:
            file_name = force_valid_file("Escribe el nombre del archivo (con su extension)")
            key = force_valid_key("Escribe la llave de 16 bytes (en hex, se permiten espacios)")

            f = open(file_name, "rb")
            data = f.read()
            f.close()

            base, ext = os.path.splitext(file_name)

            if option == 1:
                print("\nCifrando... espera un momento.")
                result = encrypt_ecb(data, key)
                output_name = base + "_cifrado" + ext
            else:
                print("\nDescifrando... espera un momento.")
                result = decrypt_ecb(data, key)
                output_name = base + "_descifrado" + ext

            new_file = open(output_name, "wb")
            new_file.write(result)
            new_file.close()

            print("\nEl archivo se guardo como:", output_name)
            input("\nPresiona Enter para continuar...")

        elif option == 3:
            print("\nGracias por usar el programa.")
            break

        else:
            print("\nError. Selecciona una opcion valida.")


if __name__ == "__main__":
    main()
