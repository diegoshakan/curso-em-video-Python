'''Faça um programa que leia a velocidade e aplique uma multa caso este limite seja ultrapassado.
A multa será de R$ 7,00 por cada Km acima do limite, velocidade máxima 80km.'''

vel = int(input("Qual foi a velocidade? "))

if (vel > 80):
    print('Você ultrapassou a velocidade máxima de 80km, foi multado!')
    multa = ((vel-80)*7)
    print('A sua multa vai custar R$ {:.2f}'.format(multa))
else:
    print('Parabéns, você está dentro do limite de velocidade!')