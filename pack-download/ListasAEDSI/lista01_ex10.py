# Receber do usuário o raio de um círculo e exibir sua área e seu perímetro.

# Importando biblioteca
from math import pi

# Coleta de dado do usuário
raio = float(input('Digite o raio do círculo: '))

# Operações
area = pi * (raio ** 2)
per = 2 * pi * raio

# Saída
print(f'Para um círculo com raio igual a {raio}, temos que sua área é igual a {area:.2f} e '
      f'seu perímetro é igual a {per:.2f}.')
