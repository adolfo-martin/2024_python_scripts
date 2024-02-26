import subprocess

resultado = subprocess.run(['date'], text=True, capture_output=True)

if resultado.returncode == 0:
    texto_fecha = resultado.stdout.strip()
    dia = texto_fecha.split(' ')[2]
    mes = texto_fecha.split(' ')[1]
    año = texto_fecha.split(' ')[5]
    print(f'{dia}/{mes}/{año}')
else:
    print('El comando date no ha funcionado')
