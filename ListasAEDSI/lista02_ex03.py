# Calcular a hipotenusa de um triângulo retângulo cujos catetos são informados pelo usuário.
# Observação: NÃO utilize a função math.hypot()

# Coletando dados do usuário
cat_o = float(input('Qual a medida do cateto oposto? '))
cat_a = float(input('Qual a medida do cateto adjacente? '))

# Operação
hip = (cat_o ** 2 + cat_a ** 2) ** (0.5)

# Saída
print(f'Um retângulo que possui cateto oposto igual a {cat_o} e cateto adjacente igual a {cat_a} possui hipotenusa '
      f'igual a {hip:.2f}.')
