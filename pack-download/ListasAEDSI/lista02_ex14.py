# Crie um programa que recebe do usuário um número com casas decimais e exiba na tela a parte inteira e a parte
# fracionária do número informado. - Ficou tosco!

# Coleta de dado do usuário
num = float(input('Digite um número decimal: '))

# Saída
print(f'O número {num} possui parte inteira igual a {int(num)} e a parte fracionária é igual a {num - int(num)}.')
