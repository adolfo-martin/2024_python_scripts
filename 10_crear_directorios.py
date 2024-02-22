#!/usr/bin/python3
import subprocess

USUARIOS = ['juan', 'cristina', 'maria', 'nicolas', 'fernando']

def main():
    crear_directorios(USUARIOS)


def crear_directorios(directorios):
    for directorio in directorios:
        resultado = subprocess.run(["mkdir", directorio], text=True, capture_output=True)
        if resultado.returncode == 0:
            print(f'Se ha creado con éxito el directorio {directorio}.')
        else:
            print(f'No se ha creado el directorio {directorio}.')


if __name__ == "__main__":
    main()