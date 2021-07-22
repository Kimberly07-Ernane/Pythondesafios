#DESAFIO 51
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

primeiro=int(input('Primeiro termo: '))
razão=int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for i in range (primeiro,décimo + razão,razão):
    print('{}'.format(i), end='-> ')
print('ACABOU')
