#DESAFIO 57
#Faça um pragrama que leia o sexo de cada pessoas,
#mas só aceite os valores 'M' ou 'F'.
#Caso os valores esteja errado peça a digitação novamente
#até ter um valor correto.

sexo=str(input('Informe o sexo [M/F]: ')).upper()[0]
while sexo not in 'M''F':
    sexo=str(input('Dados inválidos. Informe o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso')
