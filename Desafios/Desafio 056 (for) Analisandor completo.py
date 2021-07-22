#DESAFIO 56
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.

soma_idade = 0
média_idade = 0
maior_idade_homem=0
nome_velho=''
total_mulher20=0
for i in range(1,5):
    print('----- {}° PESSOA -----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade =  int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho =nome
    if sexo in 'Ff' and idade < 20:
        total_mulher20+=1
        

média_idade = soma_idade /4
print('A média de idade do grupo é de {} anos '.format(média_idade))
print('O homem mais velho tem {} anos , e se chama {}'.format(maior_idade_homem,nome_velho))
print('São {} mulheres com menos de 20 anos'.format(total_mulher20))
