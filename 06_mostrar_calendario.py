#!/usr/bin/python3
import subprocess, sys


def main():
    limpiar_pantalla()

    # compruebo los argumentos
    argumentos = sys.argv[1:]
    if not son_argumentos_correctos(argumentos):
        print('El mes introducido no existe.')
        sys.exit()

    # preparo los argumentos y muestro el calendario
    mes = argumentos[0]
    mes = str(convertir_mes(mes))
    año = argumentos[1]
    mostrar_calendario(mes, año)

    # print(son_argumentos_correctos(['junio']))
    # print(son_argumentos_correctos(['junio', '1956', 'hola']))
    # print(son_argumentos_correctos(['adios', '1956']))
    # print(son_argumentos_correctos(['junio', 'hola']))
    # print(son_argumentos_correctos(['junio', '1956']))


    # mostrar_calendario()

    # print(convertir_mes('enero'))
    # print(convertir_mes('febrero'))
    # print(convertir_mes('marzo'))
    # print(convertir_mes('abril'))
    # print(convertir_mes('mayo'))
    # print(convertir_mes('junio'))
    # print(convertir_mes('julio'))
    # print(convertir_mes('agosto'))
    # print(convertir_mes('septiembre'))
    # print(convertir_mes('octubre'))
    # print(convertir_mes('noviembre'))
    # print(convertir_mes('diciembre'))
    # print(convertir_mes('error'))


def son_argumentos_correctos(argumentos):
    if len(argumentos) != 2:
        return False

    mes_letra = argumentos[0]
    mes = convertir_mes(mes_letra)
    if mes == None:
        return False

    año = argumentos[1]
    if not año.isnumeric():
        return False
    
    return True


def limpiar_pantalla():
    subprocess.run('clear')


def mostrar_calendario(mes, año):
    subprocess.run(['cal', mes, año])


def convertir_mes(mes):
    match mes: # switch
        case 'enero':
            return 1
        case 'febrero':
            return 2
        case 'marzo':
            return 3
        case 'abril':
            return 4
        case 'mayo':
            return 5
        case 'junio':
            return 6
        case 'julio':
            return 7
        case 'agosto':
            return 8
        case 'septiembre':
            return 9
        case 'octubre':
            return 10
        case 'noviembre':
            return 11
        case 'diciembre':
            return 12
        case _: # default
            return None


if __name__ == '__main__':
    main()