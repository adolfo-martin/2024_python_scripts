import subprocess, os


def main():
    limpiar_pantalla()
    mostrar_path_como_lista_numerada()


def limpiar_pantalla():
    subprocess.run(['clear'])


def mostrar_path_como_lista_numerada():
    resultado = subprocess.run(['echo', os.environ['PATH']], capture_output=True, text=True,)
    if resultado.returncode == 0:
        linea = resultado.stdout.strip()
        linea_troceada = linea.split(':')
        i=1
        for directorio in linea_troceada:
            print(f'{i}) {directorio}')
            i+=1 # i++ # i = i + 1
    else:
        print('No se puede mostrar el PATH.')



if __name__ == '__main__':
    main()