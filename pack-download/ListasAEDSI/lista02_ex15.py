# Crie um programa que recebe do usuário a quantidade de minutos que passaram da meia noite. O programa deve exibir
# que horas são num formato de 24 horas. Considere que o usuário informará somente valores inferiores a 1440, que
# equivale a um dia (60 minutos vezes 24 horas).
# Exemplo: o usuário informou que passaram 150 minutos da meia noite, o programa deve exibir como resultado 2:30.

# Importando bibliotecas
import datetime

# Coleta de dados do usuário
mins = int(input('Quantos minutos se passaram desde a meia noite? '))

# Operações
meia_noite = datetime.datetime(2022, 7, 18, 00, 00, 00)
novo_horario = meia_noite + datetime.timedelta(minutes=mins)
nh = novo_horario.strftime('%H:%M')

# Saída
print(f'Após {mins} minutos da meia noite o horário é {nh}.')
