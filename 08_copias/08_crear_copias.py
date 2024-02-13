#!/usr/bin/python3
import sys, subprocess

def main():
    argumentos = sys.argv[1:]
    
    if not son_argumentos_correctos(argumentos):
        print('Los argumentos no son correctos.')
        return

    cantidad = int(argumentos[0])
    fichero_a_copiar = argumentos[1]
    nuevo_nombre = argumentos[2]
    copiar_ficheros(cantidad, fichero_a_copiar, nuevo_nombre)



def son_argumentos_correctos(argumentos):
    if len(argumentos) != 3:
        return False
    
    cantidad = argumentos[0]

    if not cantidad.isnumeric():
        return False
    
    return True


def copiar_ficheros(cantidad, fichero_a_copiar, nuevo_nombre):
    # cp fichero_a_copiar nuevo_nombre
    for i in range(1, cantidad+1):
        if i < 10:
            resultado = subprocess.run(['cp', fichero_a_copiar, f'{nuevo_nombre}0{i}'])            
        else:
            resultado = subprocess.run(['cp', fichero_a_copiar, f'{nuevo_nombre}{i}'])

        if resultado.returncode != 0:
            print('Ha habido un problema durante la copia.')
            # break
            return
            # sys.exit()


if __name__ == '__main__':
    main()


# subprocess.run(['cp', 'plantilla', 'salida'])


