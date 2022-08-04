# Crie um programa que calcula a área de uma esfera. Utilize a seguinte fórmula:
# A = 4 * pi * r²
# O usuário deve informar o raio da esfera e o programa deve exibir o resultado.

# Importando biblioteca
from math import pi

# Coleta de dados do usuário
raio = float(input('Digite o raio da esfera: '))

# Operação
area = 4 * pi * (raio ** 2)

# Saída do usuário
print(f'A área de uma esfera de raio {raio} é igual a {area:.2f}.')
