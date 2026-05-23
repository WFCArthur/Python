'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''


expressao = input('Digite uma expressão: ')
paren = []
for p in expressao:
    if p == '(':
        paren.append('(')
    if p == ')':
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(')')
            break
if len(paren) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')