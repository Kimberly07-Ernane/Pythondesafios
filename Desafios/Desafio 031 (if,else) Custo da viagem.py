#Desafio31
#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#e R$0,45 para viagens mais longas.

distancia=float(input("Qual é a distância da viagem? "))
c1=distancia*0.50
c2=distancia*0.45
if distancia <= 200:
    print('O valor da viagem de {}Km será R${:.2f}'.format(distancia, c1))
else:
    print('O valor da viagem de {}Km será R${:.2f}'.format(distancia, c2))
