#!/usr/bin/python3

import sys

COMUNIDADES = [
    'andalucia',
    'aragon',
    'asturias',
    'cantabria',
    'castilla-mancha',
    'castilla-leon',
    'cataluna',
    'extremadura',
    'galicia',
    'islas-baleares',
    'islas-canarias',
    'la-rioja',
    'madrid',
    'murcia',
    'navarra',
    'pais-vasco',
    'valencia',
]


def main():
    argumentos = sys.argv[1:]
    print(es_argumento_correcto(argumentos))


def es_argumento_correcto(argumentos):
    if len(argumentos) != 1:
        return False

    comunidad = argumentos[0]
    if comunidad not in COMUNIDADES:
        return False

    return True


if __name__ == '__main__':
    main()