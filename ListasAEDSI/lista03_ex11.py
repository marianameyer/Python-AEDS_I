# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#  "Telefonou para a vítima?"
#  "Esteve no local do crime?"
#  "Mora perto da vítima?"
#  "Devia para a vítima?"
#  "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
# positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
# "Assassino". Caso contrário, ele será classificado como "Inocente". (Fonte: https://www.pythonprogressivo.net/)

# Início do Classificador
print('=+='*12)
print('\t\033[1;31mCLASSIFICADOR DE SUSPEITOS\033[m')
print('=+='*12)

# Coleta de dados do usuário
p1 = str(input('Telefonou para a vítima? [S/N] ')).lower().strip()
p2 = str(input('Esteve no local do crime? [S/N] ')).lower().strip()
p3 = str(input('Mora perto da vítima? [S/N] ')).lower().strip()
p4 = str(input('Devia para a vítima? [S/N] ')).lower().strip()
p5 = str(input('Já trabalhou com a vítima? [S/N] ')).lower().strip()
print('=+='*12)

# Somador da primeira letra (caso o usuário digite sim/não)
soma = p1[0] + p2[0] + p3[0] + p4[0] + p5[0]
soma_sim = 0

# Loop do contador
for letra in soma:
    if letra == 's':
        soma_sim += 1

# Classificador
if soma_sim == 2:
    print('\t\t\t\033[33mSuspeita\033[m')
elif 3 <= soma_sim <= 4:
    print('\t\t\t\033[33mCúmplice\033[m')
elif soma_sim == 5:
    print('\t\t\t\033[1;31mAssasino\033[m')
else:
    print('\t\t\t\033[34mInocente\033[m')
