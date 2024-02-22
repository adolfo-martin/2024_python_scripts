import subprocess, os

resultado = subprocess.run(['echo', os.environ['PATH']], capture_output=True, text=True,)
print(resultado.stdout)