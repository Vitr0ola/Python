#Exercicio 1

x = int(input('Digite um numero inteiro:'))
y = int(input('Digite um segundo numero inteiro:'))

res = f'o resultado da soma de {x} com {y} sera {x + y}.'
print(res)



#EXERCÍCIO 2

#Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos e de segundos. Calcule o total de segundos resultante e imprima na tela para o usuário.

d = int(input('Quantos dias?'))
h = int(input('Quantos horas?'))
m = int(input('Quantos minutos?'))
s = int(input('Quantos segundos?'))

# 1 dia = 24h / 1 hora é = 60min / 1 min = é 60 s

total = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60)

res = f'o total de segundos calculado é de {total}.'

print(res)




#EXERCÍCIO 3

#Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto.


preco =  float(input('Digite o preço do produto:'))

p = float(input('Digite o percentual de desconto (0-100%):'))

desconto = preco * (p/100)
final = preco - desconto

print(f'O preço do produto é {preco}. Desconto aplicado de {p}%')
print(f'Valor de desconto calculado: {desconto}.')
print(f'Valor final do produto: {final}')


#EXERCÍCIO 4

#Desenvolva um algoritmo que converta uma temperatura em Celsius (C) para Fahrenheit (F). A equação de conversão é:  

<center>$\frac{9 \times C}{5} + 32$</center>

C = float(input('Digite um temperatura em Celsius (c):'))

F = (9 * C) / 5 + 32

print(f'Celsius: {C}. Fahrenheit: {F}')



#Exercicio 5

#Desenvolva um algoritmo que seja capaz de calcular a soma e a subtração entre 2 valores com vírgula.Crie duas variáveis de teste. Uma que testa se a soma é maior do que 10. Outra que testa se a subtração é menor do que 0. Imprima tudo na tela.



x = float(input('Digite um valor:'))
y = float (input('Digite um segundo valor:'))

soma = x + y
sub = x - y

test = soma > 10
testb =  sub < 0 

print(f'Soma:{soma}. Subtraçao:{sub}')
print(f'A soma é maior que 10? {test}')
print(f'A subtraçao é menor que 0? {testb}')



#Exercicio 6

#Desenvolva um algoritmo para calcular o tempo de redução de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que o fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá, Exiba o total em dias.

qtd_dia = int(input('Quantidade de cigarros voce fuma por dia?'))
anos_fumando = int(input('Quantos anos voce fuma?'))
dias_fumando = anos_fumando * 365

tempo_1cigarro = 10
total_cigarros = dias_fumando * qtd_dia

tempo_perdido_min = tempo_1cigarro * total_cigarros

tempo_perdido_dias = tempo_perdido_min / 60 / 24

print(f'Voce fuma por {dias_fumando}. Um total de {total_cigarros} cigarros')
print(f'O seu total de tempo de vida perdido, considerando que cada cigarro consome {tempo_1cigarro} minutos da sua vida é de {tempo_perdido_dias}')

