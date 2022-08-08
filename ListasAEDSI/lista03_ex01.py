# Verificar se um número informado pelo usuário é par ou ímpar

# Coleta de dado do usuário
num = int(input('Digite um número: '))

# Condicionais
if num % 2 == 0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é ÍMPAR.')
