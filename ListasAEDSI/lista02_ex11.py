# Crie um programa que calcula a aceleração média (a) de um carro durante um aumento de velocidade. O usuário deve
# informar a velocidade inicial (Vi), a velocidade final (Vf) e o tempo (Δt) gasto para que a velocidade passe de Vi
# para Vf. Utilize a fórmula:
# a = (Vf - Vi) / Δt
# Considere números com casas decimais.

# Coleta de dados do usuário
vi = float(input('Qual a velocidade inicial [m/s]? '))
vf = float(input('Qual a velocidade final [m/s]? '))
t = float(input('E qual foi o tempo gasto [s]? '))

# Operação
a = abs((vf - vi) / t)

# Saída
print(f'Uma partícula com velocidade inicial igual a {vi}m/s que, após {t}s, obteve velocidade igual a {vf}m/s possui '
      f'módulo da aceleração média igual a {a:.2f}m/s².')
