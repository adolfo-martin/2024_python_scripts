nombres = ['Luisa', 'Manuel', 'Jimena', 'Lucia', 'Raul']
apellidos = ['Sánchez', 'Giménez', 'Pérez', 'Martínez', 'Jiménez']

def concatenar_nombres_apellidos(nombres, apellidos):
    resultado = []
    if len(nombres) != len(apellidos):
        raise Exception('No coinciden las cantidades de nombres y apellidos.')

    for i in range(0, len(nombres)):
        resultado.append(f'{nombres[i]} {apellidos[i]}')
    return resultado


try:
    resultado = concatenar_nombres_apellidos(nombres, apellidos)
    print(resultado)
except Exception as error:
    print(error)


try:
    nombres.append('Juan')
    concatenar_nombres_apellidos(nombres, apellidos)
except Exception as error:
    print(error)