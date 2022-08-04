# Fazer um programa como o anterior, mas com juros compostos. Utilize a seguinte fórmula:
# SF = SI * (1+J)^N

# Firula
print('='*30)
print('CALCULADORA DE JUROS COMPOSTOS')
print('='*30)

# Coleta de dados do usuário
si = float(input('Qual o valor a ser aplicado? R$'))
j = float(input('Qual a taxa de juros? '))
n = int(input('Por quantos meses o dinheiro será investido? '))

# Operações
j = j / 100  # Convertendo o valor para porcentagem
sf = si * (1 + j) ** n

# Saída
print(f'O valor ao final do investimento será igual a \033[1;33mR${sf:.2f}\033[m.')
