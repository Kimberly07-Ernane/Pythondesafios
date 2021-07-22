#DESAFIO 45
#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
itens=('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
print('''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print ('PÔ')
sleep(1)
print('**'*20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('**'*20)
    
if computador == 0:#computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1:
        print('Você GANHOU!!!')

    elif jogador == 2:
        print('Computador VENCE!!!')
    else:
        print('JOGADA INVALIDA!')


elif computador == 1:#computador jogou PAPEL
     if jogador == 0:
         print('Computador VENCE!!!')

     elif jogador == 1:
         print('EMPATE!')

     elif jogador == 2:
         print('Você GANHOU!!!')
     else:
         print('JOGADA INVALIDA!')


elif computador == 2:#computador jogou TESOURA
     if jogador == 0:
        print('Você GANHOU!!!')

     elif jogador == 1:
         print('Computador VENCE!!!')

     elif jogador == 2:
         print('EMPATE!')
     else:
         print('JOGADA INVALIDA!')

    
