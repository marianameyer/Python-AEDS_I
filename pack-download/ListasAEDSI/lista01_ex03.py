# Receber do usuário seu nome, o nome de seu pai, o nome de sua mãe e exibir na tela uma
# frase como a do seguinte exemplo: Fulano, você é filho de Beltrano e Beltrana.

# Coleta dos dados do usuário
nome = str(input('Qual seu nome? ')).strip()
nome_pai = str(input('Qual o nome do seu pai? ')).strip()
nome_mae = str(input('Qual o nome da sua mãe? ')).strip()

# Ajuste dos nomes
nome = nome.capitalize()
nome_pai = nome_pai.capitalize()
nome_mae = nome_mae.capitalize()

# Saída
print(f'{nome}, você é filho de {nome_pai} e {nome_mae}.')
