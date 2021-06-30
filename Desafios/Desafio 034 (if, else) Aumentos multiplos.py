#Desafio34
#Escreva um programa que pergunte o salário de um funcionário
#e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento de 15%.

salario=float(input('Digite seu salário:R$   '))
if salario <= 1250:
    novo salario+(slario*15/100)
else:
    novo= salario+(salario*10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,novo))
