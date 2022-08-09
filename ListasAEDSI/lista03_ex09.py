# Faça um programa que receba do usuário dois números reais (a e b). Após isso, o programa deve exibir na tela o
# seguinte menu:
#  Digite 1 para somar.
#  Digite 2 para subtrair.
#  Digite 3 para multiplicar.
#  Digite 4 para dividir.
#  Digite 5 para sair.
# De acordo com a opção do usuário, o programa vai imprimir na tela o resultado de a+b, a-b, a*b ou a/b.

# Coleta de dados do usuário
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo núemro: '))

# Menu e escolha
print('O que você deseja fazer? Digite: \n[ 1 ] para SOMAR; \n[ 2 ] para SUBTRAIR; \n[ 3 ] para MULTIPLICAR;'
      '\n[ 4 ] para DIVIDIR; \n[ 5 ] para SAIR.')
option = int(input('Opção: '))

# Condicionais
if option == 1:
    print(f'{a} + {b} = {a+b}.')
elif option == 2:
    print(f'{a} - {b} = {a-b}.')
elif option == 3:
    print(f'{a} x {b} = {a*b}.')
elif option == 4:
    print(f'{a} / {b} = {a/b:.2f}.')
elif option == 5:
    print('Tchau!')
else:
    print('Essa opção não existe!')
