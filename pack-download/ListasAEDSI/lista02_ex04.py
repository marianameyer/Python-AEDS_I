# Fazer um programa no qual o usuário entra com o inicial saldo de uma aplicação, os juros e
# o número de meses o dinheiro será investido. Seu programa deve imprimir o saldo final.
# Considere juros simples, os quais são informados no formato 10% (obviamente sem o
# símbolo %). Utilize a seguinte fórmula:
# SF = SI + (SI * J * N)
# Onde SF é o saldo final, SI o saldo inicial, J os juros e N o número de meses.

# Firula
print('='*28)
print("CALCULADORA DE JUROS SIMPLES")
print('='*28)

# Coleta de dados do usuário
si = float(input('Qual seu saldo inicial? R$'))
j = float(input('Qual a percentagem dos juros? '))
n = int(input('Por quantos meses o dinheiro será investido? '))

# Operação
j = j / 100  # Conversão para porcentagem
sf = si + (si * j * n)  # Cálculo do valor final

# Saída
print(f'Ao final, você terá R${sf:.2f}.')
