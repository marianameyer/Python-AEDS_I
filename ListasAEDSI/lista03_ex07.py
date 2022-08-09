# Receber do usuário o país onde ele nasceu e exibir na tela sua nacionalidade. Entretanto, se o usuário escrever um
# país fora a América do Sul, seu programa deve exibir a frase “Nosso banco de dados não contém tal informação”. As
# nacionalidades a serem analisadas são:
# Argentina: argentino
# Bolívia: boliviano
# Brasil: brasileiro
# Chile: chileno
# Colômbia: colombiano
# Equador: equatoriano                      Como ainda não foram abordados os conceitos de listas e dicionários, não
# Guiana: guianense                         irei utilizá-los.
# Guiana Francesa: francês
# Peru: peruano
# Uruguai: uruguaio
# Venezuela: venezuelano
# Suriname: surinamês

# Coleta de dado do usuário
pais = str(input('Em qual país você nasceu? ')).strip().lower().replace('í', 'i').replace('ô', 'o')

# Condicionais
if pais == 'argentina':
    print('Argentino(a).')
elif pais == 'bolivia':
    print('Boliviano(a).')
elif pais == 'brasil':
    print('Brasileiro(a).')
elif pais == 'chile':
    print('Chileno(a).')
elif pais == 'colombia':
    print('Colombiano(a).')
elif pais == 'equador':
    print('Equatoriano(a).')
elif pais == 'guiana':
    print('Guianense.')
elif pais == 'guiana francesa':
    print('Francês(a).')
elif pais == 'peru':
    print('Peruano(a).')
elif pais == 'uruguai':
    print('Uruguaio(a).')
elif pais == 'venezuela':
    print('Venezuelano(a).')
elif pais == 'suriname':
    print('Surinamês.')
else:
    print('Nosso banco de dados não contém tal informação.')
