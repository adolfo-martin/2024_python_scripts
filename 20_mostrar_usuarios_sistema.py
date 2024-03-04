#!/usr/bin/python3
import subprocess, sys

EXITO = 0
ERROR_COMANDO_CAT = 1
ERROR_COMANDO_DATE = 2


def main():
    limpiar_pantalla()
    try:
        usuarios = obtener_usuarios()
    except Exception as error:
        print(error)
        sys.exit(ERROR_COMANDO_CAT)

    usuarios_ordenados = ordenar_usuarios(usuarios)
    try:
        fecha = obtener_fecha()
    except Exception as error:
        print(error)
        sys.exit(ERROR_COMANDO_DATE)

    mostrar_usuarios(usuarios_ordenados, fecha)


def mostrar_usuarios(usuarios, fecha):
    print(f'En la fecha {fecha} hay {len(usuarios)} usuarios en el sistema, y son:')
    for i in range(0, len(usuarios)):
        print(f'{i+1}) {usuarios[i]}')


def obtener_fecha():
    resultado = subprocess.run(['date', '+%d/%m/%Y'], text=True, capture_output=True)
    if resultado.returncode != 0:
        raise Exception('Hay un problema al ejecutar el comando date')
    
    return resultado.stdout.strip()


def ordenar_usuarios(usuarios):
    usuarios_ordenados = sorted(usuarios)
    return usuarios_ordenados


def obtener_usuarios():
    POSICION_NOMBRE = 0
    resultado = subprocess.run(['cat', '/etc/passwd'], text=True, capture_output=True)
    if resultado.returncode != 0:
        raise Exception('Hay un problema al ejecutar el comando cat')
    
    lineas = resultado.stdout.strip().split('\n')

    usuarios = []
    for linea in lineas:
        usuarios.append(linea.split(':')[POSICION_NOMBRE])

    return usuarios


def limpiar_pantalla():
    subprocess.run(['clear'])


if __name__ == '__main__':
    main()