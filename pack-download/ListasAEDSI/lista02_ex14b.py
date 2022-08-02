# Crie um programa que recebe do usuário um número com casas decimais e exiba na tela a parte inteira e a parte
# fracionária do número informado. - Convertendo o número para string

# Coleta de dado do usuário
num = str(input('Digite um número decimal: '))

# Operações
nums = num.split('.')

# Saída
print(f'O número {num} possui parte inteira igual a {nums[0]} e parte fracionária igual a {nums[1]}.')
