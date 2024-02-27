import math, os

def calcular_area(radio):
    if radio < 0:
        raise Exception('No existen círculos con radio negativo.')
    area = math.pi * math.pow(radio, 2)
    return area


def calcular_perimetro(radio):
    if radio < 0:
        raise Exception('No existen círculos con radio negativo.')
    perimetro = 2 * math.pi * radio
    return perimetro


os.system('cls')

try:
    print(calcular_area(1))
    print(calcular_area(-1))
    print(calcular_area(2.5))
    print(calcular_area('hola'))

except Exception as error:
    print(error)