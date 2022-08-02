# Perguntar para o usuário quantos irmão ele tem, quantas irmãs e exibir na tela o total de
# filhos de seus pais. Ex: se o usuário tem 1 irmão e uma irmã, seus pais têm 3 filhos.

# Coleta de dados do usuário
n_m = int(input('Quantos irmãos você tem? '))
n_f = int(input('Quantas irmãs você tem? '))

n_total = n_m + n_f + 1

# Saída
print(f'Você possui {n_m} irmãos e {n_f} irmãs. Logo, seus pais possuem {n_total} filhos.')
