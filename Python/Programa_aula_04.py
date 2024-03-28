
# https://viacep.com.br/ws/09180-330/json/

import requests
import warnings
warnings.filterwarnings("ignore")

cep = input("Informe o seu CEP")
url = f'https://viacep.com.br/ws/{cep}/json/'

ret = requests.get(url,verify = False).json()
dados = ret
print('-'*80)

print(f"Rua {dados['logradouro']}")
print(f"Bairro {dados['bairro']}")
print(f"Cidade {dados['localidade']}")

print('-'*80)

