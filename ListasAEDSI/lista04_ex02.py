# Criar um algoritmo que imprima a soma dos números pares em um intervalo fornecido pelo usuário.
# Laço FOR

# Início
print('\t\t\t\t\033[1;33mSOMADOR DE NÚMEROS PARES\033[m')
print('~'*70)
print('Você deverá informar um intervalo.')

# Coleta de dados do usuário
a = int(input('Digite o primeiro valor do intervalo (incluso): '))
b1 = int(input('Digite o último valor do intervalo (incluso): '))

# Ajuste do intervalo
b = b1 + 1  # Para incluir o último número no intervalo fornecido

# Somador
soma = 0

# Loop
for num in range(a, b):
    if num % 2 == 0:
        soma += num

print('~'*70)
print(f'A soma dos números pares dentro do intervalo fornecido é igual a {soma}.')
print('~'*70)
