# Crie um programa que receba do usuário um número X e um número N. Este programa deve imprimir quais são os
# números divisíveis por N entre 1 e X, inclusive.
# Laço FOR.

# Início
print('='*50)
print('\t\t\t\t\033[1;35mDIVISORES DE N\033[m')
print('='*50)
print('Este programa informa os números divisíveis por N \ndado um intervalo [1, X].')
print('='*50)

# Coleta de dados do usuário
x = int(input('Digite o último número do intervalo: '))
n = int(input('Digite o divisor: '))

# Saída
print('='*50)
print(f'Os números divisíveis por {n} são:')
# Loop
for num in range(1, x+1):
    if num % n == 0:
        print(f'\t{num}  ', end='')

print('\n')
print('='*50)
