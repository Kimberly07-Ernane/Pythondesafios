#DESAFIO 54
#Crie um programa que leia o ano de nascimento de sete pesoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores.
from datetime import date
atual = date.today().year
total_maior=0
total_menor=0
for i in range(1,8):
    ano=int(input('Em que ano a {}° pessoa nasceu?  '.format(i)))
    idade = atual - ano
    if idade >= 21:
       total_maior+=1
    else:
        total_menor+=1

print('Ao todo tivemos {} pessoas maiores de idade'.format(total_maior))
print('Ao todo tivemos {} pessoas menores de idade'.format(total_menor))
