'''Faça um programa que calcule o IMC e classifique a pessoa de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do Peso;
Entre 18.5 e 25: Peso ideal;
25 até 30: Sobrepeso;
30 até 40: Obesidade;
acima de 40: Obesidade Mórbida;
'''

# Peso ÷ altura x altura

peso = float(input('Qual é o seu peso em Kg: '))
altura = float(input('Qual é sua altura em metros(x.xx): '))

imc = (peso / altura**2)

if imc < 18.5:
    print('Abaixo do peso, seu IMC é {:.2f}.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso ideal, seu IMC é {:.2f}.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Sobrepeso, seu IMC é {:.2f}.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Obesidade, seu IMC é {:.2f}.'.format(imc))
elif imc >= 40:
    print('Obesidade Mórbida, seu IMC é {:.2f}.'.format(imc))

