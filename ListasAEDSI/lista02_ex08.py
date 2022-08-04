# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário a quantidade de
# tinta a ser comprada e os respectivos preços em 3 situações:
# -comprar apenas latas de 18 litros;
# -comprar apenas galões de 3,6 litros;
# -misturar latas e galões, de forma que o preço seja o menor.

# Importando bibliotecas
import math

# Coleta de dados do usuário
area = float(input('Qual a área, em m², a ser pintada? '))

# Operações
quant_l = area / 6  # Quantidade de litros necessários para a área informada
latas = math.ceil(quant_l / 18)  # Quantidade de latas necessárias (valor inteiro)
galoes = math.ceil(quant_l / 3.6)  # Quantidade de galões necessários (valor inteiro
valor_l = latas * 80
valor_g = galoes * 25

# Saída para o usuário
print(f'Para uma área de {area}m² você precisará de {quant_l}l. Na nossa loja, temos: '
      f'\nLata com 18 litros: R$80,00 \nGalão com 3,6 litros: R$25,00')

# Condicionais
if valor_l < valor_g:
    print(f'No seu caso, é mais econômico comprar {latas} latas de tinta. '
          f'\nO valor total será de R${valor_l:.2f}.')
elif valor_l > valor_g:
    print(f'No seu caso, é mais econômico comprar {galoes} galões de tinta. '
          f'\nO valor total será de R${valor_g:.2f}.')
elif valor_l == valor_g:
    print(f'Neste caso, tanto faz se você levar {latas} latas ou {galoes} galões de tinta. '
          f'\nO valor total será de R${valor_l:.2f}.')
