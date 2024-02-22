import subprocess

# resultado = subprocess.run(["whoami"])
# print(resultado.returncode)


resultado = subprocess.run(["mkdir", "hola"], text=True, capture_output=True)
# print(resultado.returncode)
if resultado.returncode == 0:
    print('El directorio se ha creado con éxito')
else:
    print('No se ha podido crear el directorio')

resultado = subprocess.run(["mkdir", "hola"], text=True, capture_output=True)
# print(resultado.returncode)
if resultado.returncode == 0:
    print('El directorio se ha creado con éxito')
else:
    print('No se ha podido crear el directorio')