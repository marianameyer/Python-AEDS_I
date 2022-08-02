# Faça um programa que receba do usuário dois números float e exiba na tela o resultado da
# divisão entre eles. Limite o número de casas decimais em apenas uma.

# Coleta de dados do usuário
num1 = float(input('Digite o primeiro número (não precisa ser inteiro!): '))
num2 = float(input('Digite o segundo número (também não precisa ser inteiro!): '))

# Operação
div = num1 / num2

# Saída
print(f'O número {num1} dividido por {num2} resulta em {div:.1f}.')
