'''Escreva um programa que leia um valor em metros e mostre em centímetros e milímetros.'''

m = float(input('Digite o valor em metros: '))


#km = m * 0.001
#hm = m * 0.01
#dam = m * 0.1
#dm = m * 10
cm = m * 100
mm = m * 1000

#print('{:.0f}km'.format(km))
#print('{:.0f}hm'.format(hm))
#print('{:.0f}dam'.format(dam))
#print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))