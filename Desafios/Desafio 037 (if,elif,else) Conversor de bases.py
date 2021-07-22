#DESAFIO 37
#Escreva um programa que leia um número inteiro qualquer
#e peça para o úsuario escolher qual será a base de conversão:
# 1 - para binário
# 2 - para octal
# 3 - para hexadecimal

n=int(input("Digite um número inteiro: "))
print( '''Escolha uma das bases para conversão:
[ 1 ] - converter para BINÁRIO
[ 2 ] - converter para OCTAL
[ 3 ] - converter para HEXADECIMAL ''')
opção=int(input('Sua opção: '))

if opção == 1:
    print('A conversão em binário do número {} será:{}'.format(n,bin(n)[2:]))
elif opção == 2:
    print('A conversão em octal do número {} será:{}'.format(n,oct(n)[2:]))
elif opção == 3:
    print('A conversão em Hexidecimal do número {} será:{}'.format(n,hex(n)[2:]))
else:
    print('Opção invalida!')
