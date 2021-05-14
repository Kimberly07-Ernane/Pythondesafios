#Desafio12
#Faça um algoritmo que leia o preço de um produto
#e mostee seu novo preço ,com 5% de desconto

preço=float(input('Qual é o preço do produto?: R$'))
novo= preço - (preço* 5/100)
print('O preço do produto que é R${:.2f}, com o 5% de desconto vai custar R${:.2f}'.format(preço,novo))
