#Calcular o imposto sobre o salário em 2024


salariobruto = float(input('Qual o seu salario ? '))

if salariobruto <=2112:
  print('Nao paga imposto', salariobruto.sleep())
elif salariobruto >= 2112.01 and salariobruto <= 2826.65:
  aliquota = salariobruto * 0.075
  deduçao = aliquota - 158.4
  salarioliquido = salariobruto - deduçao
elif salariobruto >= 2826.25 and salariobruto <= 3751.06:
  aliquota = salariobruto * 0.15
  deduçao = aliquota - 370.4
  salarioliquido = salariobruto - deduçao
elif salariobruto >= 3751.06 and salariobruto <= 4664.68:
  aliquota = salariobruto * 0.225
  deduçao = aliquota - 651.73
  salarioliquido = salariobruto - deduçao
elif salariobruto >= 4664.68:
  aliquota = salariobruto * 0.275
  deduçao = aliquota - 884.96
  salarioliquido = salariobruto - deduçao
print(f'Seu salário bruto é de R${salariobruto}, o (IRRF) pagante será de R${deduçao}, sendo assim o seu salário liquido será de R${salarioliquido}. ')
