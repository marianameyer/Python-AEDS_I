# Receber do usuário um número e verificar se ele está entre 0 e 10, inclusive.

# Coleta de dado do usuário
num = int(input('Digite um número: '))

# Condicionais
if num in range(0, 11):
    print(f'O número {num} está entre 0 e 10.')
else:
    print(f'O número {num} está fora do intervalo entre 0 e 10.')
