# Faça um programa que receba um texto do usuário e exiba na tela se o texto contém somente números, ou contém
# somente letras ou contém letras e números.

# Coleta de dados do usuário
texto = str(input('Digite um texto: ')).strip().lower().replace(' ', '')

# Condicionais
if texto.isalpha():
    print('O texto possui apenas letras.')
elif texto.isnumeric():
    print('O texto possui apenas números.')
else:
    print('O texto possui letras e números.')
