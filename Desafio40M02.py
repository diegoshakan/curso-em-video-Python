'''Crie um programa que receba duas notas de um aluno e mostre sua média e sua situação:
Se menor que 5 - REPROVADO
Entre 5.0 e 6.9 - RECUPERAÇÃO
Média 7.0 ou superior - APROVADO
'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7 and media <=10:
    print('Aprovado, sua nota final foi {}'.format(media))
elif media >= 5 and media <= 6.9:
    print('Recuperação, sua nota final foi {}'.format(media))
elif media < 5 and media >= 0:
    print('Reprovado, sua nota final foi {}'.format(media))
else:
    print('Nota Errada!')