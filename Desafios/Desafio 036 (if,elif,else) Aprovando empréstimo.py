#DESAFIO 36
#Escreva um programa para aprovar o empréstimo bancário
#para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador
#e em quantos anos ele vai pagar.
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
#do salário  ou  então o emprestimo será negado.

casa= float(input('Valor da casa: R$ '))
salário= float(input('Qual é o seu salário: R$ '))
anos=int(input('Quantos anos de financiamento?  '))
prestação = casa/(anos*12)
mínimo= salário *30/100
print('Para pagar a casa de R${:.2f} em {} anos'.format(casa,anos),end='')
print(' a prestação será de R${:.2f}'.format(prestação))

if prestação <= mínimo:
    print('Emprestimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
