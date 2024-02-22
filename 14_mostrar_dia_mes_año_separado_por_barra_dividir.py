#!/usr/bin/python3
import subprocess


def main():
    limpiar_pantalla()
    fecha = obtener_fecha()
    print(fecha)


def convertir_mes_a_numero(mes):
    match mes:
        case 'Jan':
            mes = '01'
        case 'Feb':
            mes = '02'
        case 'Mar':
            mes = '03'
        case 'Apr':
            mes = '04'
        case 'May':
            mes = '05'
        case 'Jun':
            mes = '06'
        case 'Jul':
            mes = '07'
        case 'Aug':
            mes = '08'
        case 'Sep':
            mes = '09'
        case 'Oct':
            mes = '10'
        case 'Nov':
            mes = '11'
        case 'Dec':
            mes = '12'
    
    return mes


def obtener_fecha():
    resultado = subprocess.run(['date'], capture_output=True, text=True)
    dia = resultado.stdout.strip().split(' ')[2]
    mes = resultado.stdout.strip().split(' ')[1]
    mes = convertir_mes_a_numero(mes)
    año = resultado.stdout.strip().split(' ')[5]
    return f'{dia}/{mes}/{año}'


def limpiar_pantalla():
    subprocess.run(['clear'])


if __name__ == '__main__':
    main()