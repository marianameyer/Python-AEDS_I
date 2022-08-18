# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#  Álcool: até 20 litros, desconto de 3% por litro
#  acima de 20 litros, desconto de 5% por litro
#  Gasolina: até 20 litros, desconto de 4% por litro
#  acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte
# forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
# da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.(Fonte: https://www.pythonprogressivo.net/)

# Início do programa
print('*.*'*10)
print('\t\t\033[1;33mPOSTO PYTHON\033[m')
print('*.*'*10)

# Saída para o usuário
print('Gasolina: \tR$ 2,50 litro. \nÁlcool: \tR$ 1,90 litro.')
print('*.*'*10)

# Coleta de dados do usuário
litros = float(input('Quantos litros? '))
tipo_c = str(input('[A-álcool/G-gasolina] \nQual combustível? ')).upper()
print('*.*'*10)

# Cálculos
if tipo_c == 'A':
    valor = litros * 1.9
    if litros <= 20:
        valor = valor * 0.97
    elif litros > 20:
        valor = valor * 0.95

if tipo_c == 'G':
    valor = litros * 2.5
    if litros <= 20:
        valor = valor * 0.96
    elif valor > 20:
        valor = valor * 0.94
print(f'Valor Total: R$ {valor:.2f}.')
