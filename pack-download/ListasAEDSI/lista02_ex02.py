#  Crie um programa onde o usuário entra com a base e a altura de um retângulo e o programa
# imprime o perímetro e sua área.
# Sabe-se que perímetro = 2*(base + altura) e a area = base * altura.

# Coletando dados do usuário
base = float(input('Digite a base do retângulo: '))
alt = float(input('Digite a altura do retângulo: '))

# Operações
perim = 2 * (base * alt)
area = base * alt

# Saída
print(f'Um retângulo com base igual a {base} e altura igual a {alt} possui:'
      f'\nPerímetro: {perim:.2f}; \nÁrea: {area:.2f}.')
