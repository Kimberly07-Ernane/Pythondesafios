#Desafio 06
#Crie um algoritmo que leia um número e mostre o seu dobro,
#triplo e raiz quadrada

n=int(input('Digite um número: '))
do=n*2
tri=n*3
rq=n**(1/2)
print('dobro de {} é {},\n  triplo de {} é {} '.format(n,do,n,tri))
print('a raiz quadarada de {} é {:.2f}' .format(n,rq))

#pode colocar os calculos dentro do print tbm
#pode usar 'pow' exemplo pow(n,(1/2))
