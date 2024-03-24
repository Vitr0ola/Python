#calculadora de imc
# imc = peso / altura * altura

peso = float(input('Qual o seu peso? : '))
altura = float(input('Qual a sua altura? : '))

imc = peso / (altura * altura)

print(f'Seu IMC é de {imc} kg/m²')
if imc <=18.5:
  print('vocÊ está abaixo do peso')
elif imc >=18.5 and imc <=24.9:
  print('Voce está no peso adequado, PARABENS!!!!')
elif imc >=25 and imc <=29.9:
  print('Voce está sobrepeso, cuidado!!!!')
elif imc >=30 and imc <=34.9:
  print('Voce está na obesidade I, procure um especialista já!')
elif imc >=35 and imc <=39.9:
  print('Obesidade grau II')
elif imc <=40:
  print('Obesidade grau III')
else:
  print('')

