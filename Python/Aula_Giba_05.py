#PROGRAMAÇAO OO (Orientado a Objeto)

#Os objetos possuem PROPRIEDADES, caracteristicas;
#Os objetos possuem METODOS, açoes;

#Classe de objetos = definiçao do objeto, qual a cor? se vai pular?

#InstÂnciamento na memoria, assim criando uma referencia baseada na classe;
#-------------------------------------------------------------------------------

#Função:
# Um bloco de código reutilizavél; (não precisa escrever o mesmo código várias vezes)

# Pode ser estático ou dinÂmico; (DinÂmico = algo que age em tempo constante/ Estático = Não faz nenhum tipo de tratamento)


#def = significa função

#---------------------------------------------------------------------------------

def mensagem():
  print('Olá, tudo bem?')


mensagem() # para executar a fuçao (mensagem)

#---------------------------------------------------------------------------------

def msg():
  texto = 'Boa noite'
  return texto #utilizando o return 

print(msg())

#---------------------------------------------------------------------------------

def msg(quem, periodo): #PARÂMETROS
  texto = f'Bom {periodo} {quem.upper()}' #UTILIZEI AS F-STRINGS PARA COLOCAR OS PARÂMETROS
  return texto

print(msg('Vitor','Dia')) #Dados dos parâmetros, que vão ser monstrado na tela.

#---------------------------------------------------------------------------------

def parimpar(v1):
  if v1 % 2 == 0: #formula padrao para descobrir numero impar ou par
    return 'Par'
  else:
    return 'Impar'
print(parimpar(251))

#----------------------------------------------------------------------------------
def muitosparametros(*args): # funçoes em lista
  for parametro in args:
    print(f'Voce passou o parametro: {parametro}')
muitosparametros(10,20,'Maria','Pedro')

#----------------------------------------------------------------------------------

def muitosparametrosdicionario(**kwargs): # funçoes do dicionario
  print(kwargs.values())
muitosparametrosdicionario(nome = 'Vitor', idade = 19)

#----------------------------------------------------------------------------------
def soma(n1,n2,n3):
  return n1 + n2 + n3

print(soma(22,22,100))
#----------------------------------------------------------------------------------
def soma(n1,n2,n3=0): #adicionando um numero ao parametro 
  return n1 + n2 + n3

print(soma(22,22))
