# Receber do usuário o consumo de um carro (em litros por quilômetros) e a distância a ser percorrida. Exibir quantos
# litros de combustível serão gastos.

# Coleta de dados do usuário
consumo = float(input('Qual o consumo do carro [l/km]? '))
dist = float(input('Qual a distância a ser percorrida [km]? '))

# Operação
lit = consumo * dist

# Saída do usuário
print(f'Um carro com consumo igual a {consumo}l/km que percorre uma distância {dist}km irá consumir {lit:.1f}l de '
      f'combustível.')
