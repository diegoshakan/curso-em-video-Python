'''Crie um programa que pergunta quanto a pessoa tem na carteira e converta em doláres
conforme o valor $ 1,00 = R$ 3,27'''

valor = float(input('Quanto Reais você tem na carteira: '))

conv = valor / 3.27

print('Você pode comprar $ {:.2f}'.format(conv))