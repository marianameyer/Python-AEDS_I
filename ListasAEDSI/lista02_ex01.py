#  Imprimir a média aritmética entre 4 números informados pelo usuário.

# Coleta de dados do usuário
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
n4 = float(input('Digite o quarto (e último) número: '))

# Operação
media = (n1 + n2 + n3 + n4) / 4

# Saída
print(f'A média aritmética dos quatro números informados é igual a \033[1;33m{media:.2f}\033[m.')
