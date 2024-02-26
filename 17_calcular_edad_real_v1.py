#!/usr/bin/python3

import subprocess, sys


def main():
    limpiar_pantalla()
    argumentos = sys.argv[1:]
    if not es_argumento_correcto(argumentos):
        print('malo')

    fecha_nacimiento = argumentos[0]
    fecha_actual = obtener_fecha_actual()
    print(calcular_edad(fecha_nacimiento, fecha_actual))


def obtener_fecha_actual():
    resultado = subprocess.run(["date"], text=True, capture_output=True)
    if resultado.returncode != 0:
        print('La fecha ha ido mal')
        return None
    
    dia = resultado.stdout.strip().split(' ')[2]
    mes_como_texto = resultado.stdout.strip().split(' ')[1]
    año = resultado.stdout.strip().split(' ')[5]

    meses = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    mes = meses[mes_como_texto]

    return f'{dia}/{mes}/{año}'


def es_argumento_correcto(argumentos):
    if len(argumentos) != 1:
        return False
    
    fecha_troceada = argumentos[0].split('/')
    if len(fecha_troceada) != 3:
        return False
    
    for item in fecha_troceada:
        if not item.isnumeric():
            return False
        
    return True

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
    # print(calcular_edad('01/01/2000', '26/02/2024'), 24)
    # print(calcular_edad('26/02/2000', '26/02/2024'), 24)
    # print(calcular_edad('27/02/2000', '26/02/2024'), 23)
    # print(calcular_edad('27/03/2000', '26/02/2024'), 23)





def limpiar_pantalla():
    subprocess.run(['clear'])



if __name__ == '__main__':
    main()



# Desarrolla un script que reciba como argumento por la línea de comandos el día de nacimiento
# en la forma 18/11/1998, y muestre por pantalla la edad del día de hoy (que es el día en el
# que se ejecuta el script)
