# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
# - salário bruto
# - quanto pagou ao INSS
# - quanto pagou ao sindicato
# - o salário líquido
# Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

# Coleta de dados do usuário
valor = float(input('Quanto você recebe por hora trabalhada? R$'))
horas = int(input('Quantas horas você trabalhou esse mês? '))

# Operações
salario_bruto = valor * horas
ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sind = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - ir - inss - sind

# Saída
print(f'Seu salário bruto é igual a R${salario_bruto:.2f}. Deste valor, são descontados: \nIR (11%): R${ir:.2f}; '
      f'\nINSS (8%): R${inss:.2f}; \nSindicato (5%): R${sind:.2f}. \nApós os descontos, seu salário será igual '
      f'a R${salario_liquido:.2f}.')
