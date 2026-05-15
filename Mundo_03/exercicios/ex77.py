'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

frase = (
'Python',
'Loss',
'Caneta',
'Sanfona',
'Birita',
'Abacate',
'Amizade',
'Azedo',
'Beleza',
'Baleia',
'Banana',
'Cabide')

for palavra in frase:
    print(f'Na Palavra {palavra.upper()} temos:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
    print()