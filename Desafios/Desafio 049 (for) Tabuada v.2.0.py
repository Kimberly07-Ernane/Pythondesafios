#DESAFIO 49
#Refaça o DESAFIO 09, mostrando a tabuada de um número que
#o usuário escolheu, só que agora utiizando um laço for.

num=int(input('Digite um número para ver sua tabuada: '))
for i in range(1,11):
    print('{} x {:2} = {} '.format(num,i,num*i))
