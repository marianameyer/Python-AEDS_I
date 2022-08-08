# Receber do usuário 3 números e exibir o maior deles.
# Como esta atividade está no módulo de Condicionais If, não usarei a função max()

# Coleta de dados do usuário
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Condicionais
if n1 >= n2 and n1 >= n3:
    print(f'O número {n1} é o maior informado.')
elif n2 >= n1 and n2 >= n3:
    print(f'O número {n2} é o maior informado.')
elif n3 >= n1 and n3 >= n2:
    print(f'O número {n3} é o maior informado.')
