'''Faça um programa que leia um valor de salário e dê um aumento de 10% se o salário for maior
que R$ 1.250,00, para os inferiores ou iguais um aumento de 15%.'''

sal = float(input('Digite seu salário: '))

if sal > 1250:
    print('Seu aumento foi de 10% e seu salário agora é R$ {:.2f}'.format(sal*0.10+sal))
elif sal <= 1250:
    print('Seu aumento foi de 15% e seu salário agora é R$ {:.2f}'.format(sal*0.15+sal))