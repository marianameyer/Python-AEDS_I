# Receber um número e imprimir todos os seus divisores.
# Laço FOR

# Início
print('='*30)
print('\t\033[1;34mLISTA DE DIVISORES\033[m')
print('='*30)
print('Este programa retorna os \ndivisores do número informado.')
print('='*30)

# Coleta de dado do usuário
num = int(input('Digite um número inteiro: '))

print('='*30)
print(f'Os divisores de {num} são:')

# Loop
for n in range(1, num+1):
    if num % n == 0:
        if n != num:
            print(f'{n}, ', end='')
        elif n == num:
            print(f'{n}.')

print('='*30)
