# Receba do aluno o valor de 3 provas, calcule a média aritmética entre elas e exiba na tela se o aluno foi aprovado ou
# reprovado. Obs.: um aluno é aprovado se sua nota for maior ou igual a 6.

# Coleta de dados do aluno
nota1 = float(input('Digite o valor da primeira prova: '))
nota2 = float(input('Digite o valor da segunda prova: '))
nota3 = float(input('Digite o valor da terceira prova: '))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3
print(f'A média do aluno foi igual a {media:.1f}.')

# Condicionais
if media >= 6.0:
    print('O aluno foi APROVADO!')
else:
    print('O aluno foi REPROVADO...')
