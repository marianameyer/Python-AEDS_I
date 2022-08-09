# A prefeitura de Cafundodojudas abriu uma linha de credito para os funcionários. O valor máximo da prestação não
# poderá ultrapassar 30% do salário bruto. Fazer um algoritmo onde o usuário informa seu salário bruto e o valor da
# prestação e o programa exibe na tela se o empréstimo pode ou não ser concedido.

# Coleta de dados do usuário
salario_bruto = float(input('Qual seu salário bruto? R$'))
valor_prest = float(input('Qual o valor da prestação? R$'))

# Cálculo
limite = salario_bruto * 0.3
print(f'O valor limite para o empréstimo é de R${limite:.2f}.')

# Condicionais
if valor_prest <= limite:
    print('Seu empréstimo foi CONCEDIDO.')
else:
    print('Seu empréstimo não pode ser CONCEDIDO...')
