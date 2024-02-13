#!/usr/bin/python3

import subprocess
import sys


def main():
    limpiar_pantalla()
    if son_argumentos_correctos():
        mostrar_mensaje()
    else:
        print('Hay un problema con los argumentos.')


def son_argumentos_correctos():
    argumentos = sys.argv[1:]
    if len(argumentos) != 4:
        return False
    
    edad = argumentos[2]
    if not edad.isnumeric():
        return False
    
    return True


def mostrar_mensaje():
    nombre = sys.argv[1]
    apellido = sys.argv[2]
    edad = sys.argv[3]
    modulo = sys.argv[4]

    print(f'Hola, soy {nombre} {apellido}, tengo {edad} años y el módulo que más me gusta es {modulo}')


def limpiar_pantalla():
    subprocess.run('clear')


if __name__ == '__main__':
    main()