#DESAFIO 41
#A confederação Nacional De Natação precisa de um programa que leia:
#o ano de nascimento de um  atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER
from datetime import date
atual = date.today().year
ano=int(input('Informe o  ano de nascimento do atleta: '))
idade= atual-ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
