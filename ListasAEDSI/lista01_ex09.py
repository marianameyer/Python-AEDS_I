# Crie um programa para ler dois números (num1 e num2) e imprimir as divisões entre eles.
# Limite as casas decimais em 4. Ex: num1=6 e num2=3, resultado => 6/3 = 2 e 3/6 = 0.5

# Coleta de dados do usuário
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

# Operações
div_12 = num1 / num2
div_21 = num2 / num1

# Saída
print(f'A primeira divisão é: {num1} / {num2} = {div_12:.4f}. \nA segunda divisão é: {num2} / {num1} = {div_21:.4f}.')
