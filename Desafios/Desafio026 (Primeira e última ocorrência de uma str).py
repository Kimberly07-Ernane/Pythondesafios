#Desafio 26
#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aprece a última vez

frase=str(input('Digite uma frase: ')).upper
print('A letra A apreceu {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {} '.format(frase.find('A')+1))
print('A última letra apareceu na posição {} '.format(frase.rfind('A')+1))
