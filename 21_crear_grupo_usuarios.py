#!/usr/bin/python3
import subprocess, sys

ERROR_NUMERO_ARGUMENTOS_INCORRECTO = 1
ERROR_CANTIDAD_USUARIOS_INCORRECTA = 2


def main():    
    limpiar_pantalla()

    try:
        argumentos = sys.argv[1:]
        grupo, cantidad, contraseña = obtener_grupo_cantidad_contraseña(argumentos)
    except Exception as error:
        print(error)

    contraseña_encriptada = encriptar_contraseña(contraseña)

    try:
        crear_usuarios(grupo, cantidad, contraseña_encriptada)
    except Exception as error:
        print(error)


    # finally:
    #     print('FIN 🏁')


def obtener_año_actual():
    resultado = subprocess.run(['date', '+%Y'], text=True, capture_output=True)
    if resultado.returncode != 0:
        raise Exception('No se puede obtener el año actual.')
    
    return resultado.stdout.strip()


def encriptar_contraseña(contraseña):
    resultado = subprocess.run(['mkpasswd', contraseña], text=True, capture_output=True)
    if resultado.returncode != 0:
        raise Exception('No se ha podido encriptar la contraseña')
    
    return resultado.stdout.strip()


def crear_usuarios(grupo, cantidad, contraseña):
    for i in range(1, cantidad+1):
        prefijo = '0' if i < 10 else ''

        nombre = f'{grupo}_{prefijo}{i}'
        try:
            crear_usuario(nombre, grupo, contraseña)
        except Exception as error:
            raise Exception(f'No se han podido crear los usurios.\n(ERROR) {error}')


def crear_usuario(nombre, grupo, contraseña):
    año = obtener_año_actual()
    fecha_caducidad = f'{año}-06-30'

    resultado = subprocess.run(
        ['sudo', 'useradd', '--create-home', '--base-dir', f'/home/{grupo}' ,'--password', contraseña, '--expiredate', fecha_caducidad, nombre], 
        text=True, 
        capture_output=True
    )

    if resultado.returncode != 0:
        match (resultado.returncode):
            case 1:
                mensaje = 'No se puede actualizar el ficheros de contraseñas.'
            case 2:
                mensaje = 'Sintaxis inválida.'
            case 3:
                mensaje = 'Argumento en opción inválido.'
            case 4:
                mensaje = 'Identificador de usuario ya usado.'
            case 6:
                mensaje = 'El grupo especificado no existe.'
            case 9:
                mensaje = 'Nombre de usuario ya usado.'
            case 10:
                mensaje = 'No se puede actualizar el fichero de grupos.'
            case 12:
                mensaje = 'No se puede crear el directorio home.'
            case 14:
                mensaje = 'No se puede actualizar el mapeo de usuarios.'
            case default:
                mensaje = 'Error sin especificar.' 

        mensaje_error = resultado.stderr
        raise Exception(f'No se ha podido crear el usuario {nombre}.\n(ERROR) {mensaje} {mensaje_error}')


def obtener_grupo_cantidad_contraseña(argumentos):
    if len(argumentos) != 3:
        raise Exception('El número de argumentos no es correcto.')
        sys.exit(ERROR_NUMERO_ARGUMENTOS_INCORRECTO)
    
    grupo = argumentos[0]
    cantidad = argumentos[1]
    contraseña = argumentos[2]

    if not cantidad.isnumeric():
        raise Exception('La cantidad no es un número.')
        sys.exit(ERROR_CANTIDAD_USUARIOS_INCORRECTA)
    
    return grupo, int(cantidad), contraseña


def limpiar_pantalla():
    subprocess.run(['clear'])


if __name__ == '__main__':
    main()



# Desarrollar un script que reciba como argumentos: 
# - un nombre para el grupo de usuarios,
# - la cantidad de usuarios a crear,
# - la contraseña por defecto para dichos usuarios
# sudo python3 crear_grupo_usuarios.py ayf2 25 
# crearía 25 usuarios llamados ayf2_01, ayf2_02, ..., ayf2_25
# También hay que crear los distintos directorios personales en /home. El directorio personal se llamará igual que el usuario.
# Los códigos de error serán:
# 1 - Número de argumentos incorrecto.
# 2 - El argumento cantidad no es correcto.

