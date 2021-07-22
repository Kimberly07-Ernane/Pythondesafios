#Desafio17
#Faça um programa que leia o comprimento do cateto oposto do cateto adjacente
#de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
co=float(input('Informe o comprimento do cateto oposto: '))
ca=float(input('Informe o comprimento do cateto adjacente: '))
hi=math.hypot(co,ca)
print('A hipotenusa vai merdir: {:.2f}'.format(hi))
