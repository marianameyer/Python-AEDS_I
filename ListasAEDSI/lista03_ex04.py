# Verificar se a letra digitada pelo usuário é vogal ou consoante

# Coleta de dado do usuário
letra = str(input('Digite uma letra: ')).strip().lower()

# Lista com as vogais
lista = ['a', 'e', 'i', 'o', 'u']

# Condicionais
if letra in lista:
    print(f'A letra {letra} é VOGAL.')
else:
    print(f'A letra {letra} é CONSOANTE.')
