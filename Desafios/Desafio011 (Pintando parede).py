#Desafio11
#Faça um programa que leia a largura e a altura de uma parede
#em  metros , calcule a sua área e a quantidade de tinta necessária
#para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

larg=float(input('Largura da aparede: '))
alt=float(input('Alutra da parede: '))
area = larg*alt
print('Sua parede tem a dimensão de {}x{} e sua área de {}m.'.format(larg,alt,area))
tinta=area/2
print('Para pintar essa parede , você precisará de {}l de tinta.'.format(tinta))
