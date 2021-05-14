#Desafio19
#Um professor quer sortear um ods seus quatro alunos para apagar o quadro.
#Faça um programa que jude a ele,
#lendo o nome deles e escrevendo o nome do escolhido.
import random
A1=str(input('Primeiro aluno: '))
A2= str(input('Segundo aluno: '))
A3=str(input('Terceiro aluno: '))
A4=str(input('Quarta aluno: '))
lista=[A1,A2,A3,A4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
