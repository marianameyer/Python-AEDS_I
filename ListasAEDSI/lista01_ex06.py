# Receber o lado de um quadrado e exibir na tela sua área.

# Coleta de dado do usuário
lado = float(input('Digite a medida do lado do quadrado: '))

# Área
area = lado ** 2

# Saída
print(f'Um quadrado com lado igual a {lado} possui área igual a {area:.2f}.')  # Cálculos sem unidades
