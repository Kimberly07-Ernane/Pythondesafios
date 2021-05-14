#Desafio 25
#Crie um programa que leia o nome de uma pessoa
#e diga se ela tem "SILVA" no nome.
#mostrar true or false

nome=str(input("Digite seu nome completo: ")).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.lower()))
