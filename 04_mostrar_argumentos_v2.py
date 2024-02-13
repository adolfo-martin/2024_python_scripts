#!/usr/bin/python3

import sys

def main():
    mostrar_argumentos()


def mostrar_argumentos():
    fichero = sys.argv[0]
    argumentos = sys.argv[1:]

    print('El script ejecutado es', fichero)

    if len(argumentos) == 0:
        print('El script no ha recibido argumentos')
    else:
        # print('Los argumentos son', argumentos)
        print('Los argumentos son:')
        for i in range(0, len(argumentos)):
            # print(f'\t{i+1}) {argumentos[i]}')
            if i == 0 or i == 2:
                print(f'\t{i+1}\u1d49\u02b3 argumento: {argumentos[i]}')
            else:
                print(f'\t{i+1}\u1d52 argumento: {argumentos[i]}')


if __name__ == "__main__":
    main()