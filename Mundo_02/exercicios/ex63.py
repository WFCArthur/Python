# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

# EX: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

'''A base é sempre essa:

F(0) = 0
F(1) = 1

E depois você usa a regra:

F(n)=F(n−1)+F(n−2)

A sequência de Fibonacci é essa:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
🔁 Como ela cresce

Cada número é a soma dos dois anteriores:

0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
e assim vai...'''


'''n = int(input('Digite um número: '))
a,b = 0,1
for c in range(n):
    print(a,end=' ')
    a,b = b, a + b'''

print('--'*20)
print('Sequência de Fibonacci')
print('--'*20)
n = int(input('Quantos números: '))

a,b = 0,1
c = 0
print('~~'*25)
while c < n:
    print(a,'>',end=' ')
    c += 1
    a,b = b, a + b
print('Fim')
print('~~'*25)







