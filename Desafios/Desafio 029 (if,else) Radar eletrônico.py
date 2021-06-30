#Desafio29
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acma do limite.

velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade-80)*7
if velocidade > 80:
    print('MULTADO! Você execedeu o limite permitido que é de 80Km/h')
    print('O valor da multa será R${:.2f}.'.format(multa))
print('Tenha um bom dia, dirija com SEGURANÇA!')
