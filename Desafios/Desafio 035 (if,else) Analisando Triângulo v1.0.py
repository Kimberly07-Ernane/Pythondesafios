#Desafio35
#Desenvolva um programa que leia o comprimento de três retas
#e diga ao usuário se elas podem formar um triângulo.
print('*'*30)
print('Analisador de Triângulos')
print('*'*30)

r1=int(input('Digite o valor ds primeira reta: '))
r2=int(input('Digite o valor da segunda reta: '))
r3=int(input('Digite o valor da terceira reta: '))
if r1< r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM formar um triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo')
