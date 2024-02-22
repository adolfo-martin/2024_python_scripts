#!/usr/bin/python3

import subprocess, sys

EXITO = 0
ERROR_ARGUMENTOS_ERRONEOS = 1
ERROR_NO_ES_POSIBLE_LA_COMUNICACION = 2


def main():
    limpiar_pantalla()
    argumentos = sys.argv[1:]
    if not es_argumento_correcto(argumentos):
        print('Los argumentos suministrados no son correctos.')
        print('Debe suministrar una dirección IP.')
        sys.exit(ERROR_ARGUMENTOS_ERRONEOS)

    direccion_ip = argumentos[0]
    comprobar_comunicacion(direccion_ip)


def es_argumento_correcto(argumentos):
    if len(argumentos) != 1:
        return False
    
    direccion = argumentos[0]
    if not es_direccion_correcta(direccion):
        return False
    
    return True


def es_direccion_correcta(direccion):
    direccion_troceada = direccion.split('.') # "10.32.155.28" --split--> ["10", "32", "155", "28"]
    if len(direccion_troceada) != 4:
        return False
    
    for elemento in direccion_troceada:
        if not elemento.isnumeric():
            return False
        
        numero = int(elemento)
        if numero < 0 or numero > 255:
            return False
        
    return True
            

def comprobar_comunicacion(direccion_ip):
    resultado = subprocess.run(["ping", "-c", "1", direccion_ip], text=True, capture_output=True)
    if resultado.returncode == 0:
        print(f"Existe comunicación con el equipo {direccion_ip}")
        sys.exit(EXITO)
    else:
        print(f"No existe comunicación con el equipo {direccion_ip}")
        sys.exit(ERROR_NO_ES_POSIBLE_LA_COMUNICACION)


def limpiar_pantalla():
    subprocess.run(["clear"])


if __name__ == "__main__":
    main()