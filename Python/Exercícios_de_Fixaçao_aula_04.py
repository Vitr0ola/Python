#Criei um dicionario e coloquei valores;
meu_dict = {'nome':'Vitor','idade': 19}

print(meu_dict['nome'])

#------------------------------------------------------------------------------------
#Usando o .get// o get serve para monstrar algo que talvez nao tenha valor atribuido;

profissao = meu_dict.get('profissao','Nao especificado')
print(profissao)

#------------------------------------------------------------------------------------

#Colocando novos elementos;

meu_dict ['profissao'] = 'programador'
print(meu_dict)


#-----------------------------------------------------------------------------------
#Adicionando mais um valor e uma chave;
meu_dict['Curso'] = 'ADS'

#----------------------------------------------------------------------------------
#QUAIS SAO AS CHAVES QUE EU CRIEI NO MEU DICIONARIO? METODO .keys()

print(meu_dict.keys())

#----------------------------------------------------------------------------------

#SE EU QUISER SABER OS VALORES? METODO .values()
print(meu_dict.values())

#----------------------------------------------------------------------------------

#ITERAÇAO EM DICIONARIOS
#Voce pode iterar sobre um dicionario usando um loop for. isso é util para acessar cada par chave-valor
#Exemplo

for chave, valor in meu_dict.items():
  print(f'{chave} : {valor}')


#----------------------------------------------------------------------------------

#DICIONARIOS ANINHADOS;
familia = {
    'pai' : {'nome': 'Carlos','idade':59},
    'mae' : {'nome': 'Joselia','idade':52}
}

#----------------------------------------------------------------------------------

#Achando apenas o nome do pai;
familia.keys()
print(familia['pai']['nome'])


#---------------------------------------------------------------------------------

#ADICIONANDO FILHOS A VARIAVEL FAMILIA;
familia ['Filhos'] = {'nome': 'Anderson','idade':30}
print(familia)
