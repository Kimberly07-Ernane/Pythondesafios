#DESAFIO 39
#Faça um prorama que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
#Seu programa també, deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
ano=int(input('Digite seu ano de nascimento:' ))
idade=atual-ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano,idade,atual))
if idade == 18:
      print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    falta=18 - idade
    print('Ainda falta {} anos para o alistamento.'.format(falta))
    ano2=atual+falta
    print('Seu alistamento será  em {}.'.format(ano2))
else:
    falta= idade - 18
    print('Você já deveria ter se alistado há {} anos. '.format(falta))
    ano2=atual-falta
    print('Seu alistamento foi em {}.'.format(ano2))
