Aula 03 Python (giba)

OBJETO = Atributos e metodos

Metodos = ultizamos com o ponto depois da variavel. (nome.) apenas em strings

lower = minusculo
upper = maiusculo
replace = substituir a letra
count = quantidade de letras tem

nome = 'gilberto'
print(nome.upper())  
GILBERTO

nome = nome.upper()

print(nome.replace('G','X'))

print(nome.replace('G','X').replace('E','Y).lower())

print(produto.count('a'))


string
char = 1 caractere 

Type = saber o tipo de variavel
id= saber onde esta na memoria


nome  = str('gilberto')
print(type(nome))


variaveis multaveis e imultaveis


Multaveis, elas recebem novos conteudos e mundam de lugar na memoria, sao as variaveis do tipo primitivos(strings, booleano...)




Operadores logicos

== igualdade
> maior que
< menor que
>= maior ou igual
<= menor ou igual
!= diferente


print (5 > 6)

Condiçoes (or and)

print(nome == 'GIlBERTO' or produto == 'maça')
true

print(nome == 'GIlBERTO' and produto == 'maça')
false


Exercicio

else = se nao
if = se

mes = str(input('Digite o mes :')).upper()
if mes == 'JAN':
    print('Janeiro')
elif mes == 'FEV':
   print('Fevereiro')
elif mes == 'MAR':
print('Março')
else:
print('mes incorreto !!!')


#colocar o conteudo de uma lista em ordem alfabetica
frutas.sort() #classificar em ordem alfabetica
print(frutas)
print(frutas[1])


frutas.append('Amora') # acrescentar mais algum item, apenas um de cada vez
frutas.sort()
print(frutas)


for fruta in frutas: #for (para) comando de loop, tudo que tiver em frutas ele irá monstrar utilizando FRUTA.
  print('As frutas sao: ',fruta)




