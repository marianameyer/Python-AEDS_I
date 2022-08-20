# Fazer um algoritmo que imprima os números de 1 a 100 e depois de 100 até 1.
# Laço FOR

# Impressão crescente
print('Crescente:')
for n in range(1, 101):
    print(f'{n} ', end='')

print('\n')

# Impressão decrescente
print('Decrescente:')
for n in range(100, 0, -1):
    print(f'{n} ', end='')
