#DESAFIO 53
#Crie um programa que leia uma frase qualquer
#e diga se ela é um palindromo, considerando os espaços.
#Ex: apos a sopa , a sacada da casa, a torre da derrota, o lobo ama o bolo...

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print ('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um  Palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
