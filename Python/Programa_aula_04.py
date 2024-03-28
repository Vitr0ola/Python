
# Utilizando o site viacep.com.br criei um codigo que quando voce informa seu cep ele te entrega valores(dados) de acordo.
#API REST 
#Dicionario

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

