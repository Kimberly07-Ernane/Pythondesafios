#Desafio 22
#Crie um programa que leia o nome complemeto de uma pessoa e mostre:
#O nome com todas as letras minusculas
#O nome com todas as letras maiúsculas
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome.
nome=str(input('Digite seu nome inteiro: ')).strip()
print('Análisando seu nome...')
print('Seu nome em letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
