#DESAFIO 43
#Desenvolva uma lógica que leia o peso a altura de uma pessoa,
#calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# -  Abaixo de 18.5: Abaixo do peso
# -  Entre 18.5 e 25: peso ideal
# -  25 até 30: Sobrepeso
# -  30 até 40: Obesidade
# -  Acima de 40: Obesidade móbida

peso=float(input('Qual é seu peso? (kg) '))
altura=float(input('Qual é a sua altura? (m) '))
imc= peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f} '.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:
    print('Você está com o PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
else:
    print('ATENÇÃO , você etá em OBESIDADE MÓRBIDA!')

    
