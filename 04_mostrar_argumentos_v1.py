#!/usr/bin/python3

import sys
print('Los elementos de la línea de comandos son: ', sys.argv)
print('El primer elemento es: ', sys.argv[0])
print('El segundo elemento es: ', sys.argv[1])
print('El tercer elemento es: ', sys.argv[2])
print('El cuarto elemento es: ', sys.argv[3])
print('Los argumentos reales son: ', sys.argv[1:])
print(sys.argv[1:3])
print(sys.argv[:3])