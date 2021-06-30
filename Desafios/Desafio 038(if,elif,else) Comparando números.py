#DESAFIO 38
#Escreva um programa que leia dois números inteiros e compare-os,
#mostrando na tela uma mensagem:
# - 0 primeiro valor é MAIOR
# - 0 segundo valor é MENOR
# - não existe valor maior, os dois são IGUAIS

n1=int(input('Digite um número inteiro: '))
n2=int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O primeiro número é MAIOR!')
elif n2 > n1:
    print('O segundo número é MENOR!')
else:
    print('Não existe valor maior, os dois são IGUAIS!')
