#Desafio18
#Faça um programa que leia um ângulo qualquer e
#Mostre na tela o valor do seno,cosseno e tangente desse ângulo.
#from math import radians,sin,cos,tan(pode ser assim tbm ai tira as ref.das outras variaveis
import math
ang=int(input('Digite o ângulo: '))
seno=math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,seno))
cosseno=math.cos(math.radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,cosseno))
tangente=math.tan(math.radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang,tangente))
