#!/usr/bin/python3

import subprocess, sys

EXITO = 0
ERROR_CON_LA_FECHA_DE_NACIMIENTO = 1
ERROR_CON_LA_FECHA_ACTUAL = 2


def main():
    limpiar_pantalla()

    argumentos = sys.argv[1:]
    try:
        fecha_nacimiento = obtener_fecha_nacimiento(argumentos)
    except Exception as error:
        print(error)
        sys.exit(ERROR_CON_LA_FECHA_DE_NACIMIENTO)

    try:
        fecha_actual = obtener_fecha_actual()
    except Exception as error:
        print(error)
        sys.exit(ERROR_CON_LA_FECHA_ACTUAL)

    print(calcular_edad(fecha_nacimiento, fecha_actual))


def obtener_fecha_actual():
    resultado = subprocess.run(["date"], text=True, capture_output=True)
    if resultado.returncode != 0:
        raise Exception('Ha habido un problema con el comando date.')
    
    dia = resultado.stdout.strip().split(' ')[2]
    mes_como_texto = resultado.stdout.strip().split(' ')[1]
    año = resultado.stdout.strip().split(' ')[5]

    meses = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    mes = meses[mes_como_texto]

    return f'{dia}/{mes}/{año}'


def obtener_fecha_nacimiento(argumentos):
    if len(argumentos) != 1:
        raise Exception('El número de argumentos es erróneo.')
    
    fecha_troceada = argumentos[0].split('/')
    if len(fecha_troceada) != 3:
        raise Exception('La fecha tiene un número de partes incorrecto.')
    
    for item in fecha_troceada:
        if not item.isnumeric():
            raise Exception('La fecha incluye un elemento no numérico.')
    
    fecha_nacimiento = argumentos[0]
    dia = int(fecha_nacimiento.split('/')[0])
    mes = int(fecha_nacimiento.split('/')[1])
    año = int(fecha_nacimiento.split('/')[2])

    return f"{dia}/{mes}/{año}"

    # que me pasen solo un valor
    # formato de la fecha
        # que sea tres numeros
        # que esten separados por barras


# fecha_nacimiento: "dd/mm/aaaa"
# fecha_actual: "dd/mm/aaaa"
def calcular_edad(fecha_nacimiento, fecha_actual):
    dia_nacimiento = int(fecha_nacimiento.split('/')[0])
    mes_nacimiento = int(fecha_nacimiento.split('/')[1])
    año_nacimiento = int(fecha_nacimiento.split('/')[2])

    dia_actual = int(fecha_actual.split('/')[0])
    mes_actual = int(fecha_actual.split('/')[1])
    año_actual = int(fecha_actual.split('/')[2])

    edad = año_actual - año_nacimiento
    if mes_actual < mes_nacimiento:
        edad -= 1
    elif mes_actual == mes_nacimiento and dia_actual < dia_nacimiento: 
        edad -= 1

    return edad


def limpiar_pantalla():
    subprocess.run(['clear'])


if __name__ == '__main__':
    main()

# Desarrolla un script que reciba como argumento por la línea de comandos el día de nacimiento
# en la forma 18/11/1998, y muestre por pantalla la edad del día de hoy (que es el día en el
# que se ejecuta el script)