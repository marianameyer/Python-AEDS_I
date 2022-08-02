# Crie um programa que calcula a Energia Potencial Elástica (E) de molas. O usuário deve informar todos os dados
# necessários e o programa deve exibir o resultado no final. Considere a seguinte fórmula:
# 𝐸 = (k * x²) / 2
# Onde k é a constante elástica e x a elongação da mola.

# Coleta de dados do usuário
k = float(input('Qual a constante elástica da mola [N/m]? '))
x = float(input('E qual a elongação [m]? '))

# Operação
energia = k * (x ** 2) / 2

# Saída do usuário
print(f'Para uma mola com constante elástica de {k}N/m e elongação de {x}m, '
      f'\na energia potencial elástica é igual a {energia:.2f}J.')
