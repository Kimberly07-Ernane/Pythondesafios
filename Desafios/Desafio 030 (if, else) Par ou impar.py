#Desafio30
#Crie um programa que leia um número inteiro e mostre na tela se ele é
#PAR ou ÍMPAR.

n=int(input('Digite um número: '))
resultado=n%2
if resultado == 0:
    print('{} é um número PAR!'.format(n))
else:
    print('{} é um número ÍMPAR!'.format(n))
