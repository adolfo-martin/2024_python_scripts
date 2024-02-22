import subprocess, sys

# subprocess.run(['clear'])

# resultado = subprocess.run(
#     ['ping', '-c', '1', '8.8.8.8'], 
#     text=True, 
#     capture_output=True
# )

# if resultado.returncode == 0:
#     print('Ha funcionado bien.')
# else:
#     print('Ha funcionado mal.')

# resultado = subprocess.run(
#     ['ping', '-c', '1', '8.8.8.7'], 
#     text=True, 
#     capture_output=True
# )

# if resultado.returncode == 0:
#     print('Ha funcionado bien.')
# else:
#     print('Ha funcionado mal.')

# texto = '  hola  '
# print(len(texto))
# print(len(texto.strip()))
# sys.exit(1)


resultado = subprocess.run(['date'], text=True, capture_output=True)
if resultado.returncode != 0:
    print('Ha habido un problema con date')
    sys.exit(1)

# texto_date = resultado.stdout.strip()
# # print(f'Lo se se ha capturado es: {texto_date}')
# print(texto_date.split(' ')[5])
    
año = resultado.stdout.strip().split(' ')[5]
print(año)