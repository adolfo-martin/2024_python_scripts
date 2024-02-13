#!/usr/bin/python3

import subprocess


def main():
    limpiar_pantalla()
    

def limpiar_pantalla():
    subprocess.run("clear")


# esto es como el main de Java, es donde empieza el programa
if __name__ == "__main__":
    main()