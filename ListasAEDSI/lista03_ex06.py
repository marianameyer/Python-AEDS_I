# Receba do usuário seu peso e altura, calcule o IMC. Exiba na tela qual a classificação da pessoa de acordo com a
# seguinte tabela:
# IMC                   CLASSIFICAÇÃO
# MENOR QUE 18,5        MAGREZA
# ENTRE 18,5 E 24,9     NORMAL
# ENTRE 25,0 E 29,9     SOBREPESO
# ENTRE 30,0 E 39,9     OBESIDADE
# MAIOR QUE 40,0        OBESIDADE GRAVE
# Utilize a seguinte fórmula: IMC = peso / altura²

# Coleta de dados do usuário
peso = float(input('Digite seu peso [kg]: '))
altura = float(input('Digite sua altura [m]: '))

# Cálculo IMC
imc = peso / (altura ** 2)
print(f'Seu IMC é igual a {imc:.1f}. Sua classificação é: ', end='')

# Condicionais
if imc < 18.5:
    print('MAGREZA.')
elif imc < 24.9:
    print('NORMAL.')
elif imc < 29.9:
    print('SOBREPESO.')
elif imc < 39.9:
    print('OBESIDADE.')
else:
    print('OBESIDADE GRAVE.')
