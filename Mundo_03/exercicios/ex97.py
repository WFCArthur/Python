'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escreva(frase):

    print('~'*len(frase))
    print(frase)
    print('~'*len(frase))


escreva('  Eu gosto muito de programar  ')
escreva('  Python  ')
escreva('  Com o professor Gustavo Guanabara  ')