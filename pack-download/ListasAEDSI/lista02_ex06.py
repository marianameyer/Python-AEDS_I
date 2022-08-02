# Converter uma temperatura fornecida pelo usuário de graus Farenheit para graus Celsius.
# Utilize a seguinte fórmula:
# C = (5 * (F-32) / 9).
# Onde C é a temperatura em Celsius e F a temperatura em Farenheit.

# Coleta de dados do usuário
temp_f = float(input('Digite a temperatura em ºF que será convertida para ºC: '))

# Operação
temp_c = 5 * (temp_f - 32) / 9

# Saída
print(f'Uma temperatura igual a {temp_f}ºF é igual a {temp_c:.1f}ºC.')
