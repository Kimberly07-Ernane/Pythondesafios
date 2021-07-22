#Desafio15
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias=int(input('A quantidade de dias que  você alugou o carro: '))
km=float(input('A quantidade de KM que foi percorrido: '))
pago=dias*60 + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(pago))
