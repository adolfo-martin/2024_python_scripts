#!/usr/bin/python3

import subprocess
import sys


def main():
    limpiar_pantalla()

    while True:
        mostrar_menu()
        opcion = int(input('Selecciona una opción: '))

        match opcion:
            case 1:
                mostrar_fecha()
            case 2:
                mostrar_quien_soy()
            case 3:
                mostrar_quien_esta_conectado()
            case 4:
                mostrar_calendario()
            case 5: 
                cambiar_contraseña()
            case 6:
                cerrar_aplicacion()
            case _:
                print("Debe introducir una opción correcta.")


def limpiar_pantalla():
    subprocess.run("clear")


def mostrar_fecha():
    subprocess.run(['date', '+%d/%m/%Y'])


def mostrar_quien_soy():
    subprocess.run(['whoami'])


def mostrar_quien_esta_conectado():
    subprocess.run(['who'])


def mostrar_calendario():
    subprocess.run(['cal'])


def cambiar_contraseña():
    subprocess.run(["passwd"])


def cerrar_aplicacion():
    sys.exit()


def mostrar_menu():
    print('----------------- Menú ------------------')
    print('1) Mostrar fecha.')
    print('2) Mostrar quién soy.')
    print('3) Mostrar quién está conectado.')
    print('4) Mostrar el calendario.')
    print('5) Cambiar la contraseña.')
    print('6) Cerrar la aplicación.')


if __name__ == "__main__":
    main()