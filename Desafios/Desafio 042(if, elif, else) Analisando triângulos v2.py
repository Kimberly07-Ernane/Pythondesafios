#DESAFIO 42
#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
#que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓCELES: dois lados iguais
#ESCALENO: todos os lados diferentes.

print('*'*30)
print('Analisador de Triângulos')
print('*'*30)

r1=int(input('Digite o valor ds primeira reta: '))
r2=int(input('Digite o valor da segunda reta: '))
r3=int(input('Digite o valor da terceira reta: '))
#IF dentro de IF
if r1< r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM formar um triângulo!',end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo')

