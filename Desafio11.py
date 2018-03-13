'''Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a
quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta 2m².'''

lar = float(input("Digite a largura em metros: "))
alt = float(input('Digite a altura em metros: '))
area = lar * alt
tinta = area / 2

print('Sua parede tem de largura {:.2f}m², de altura {:.2f}m², sua área é de {:.2f}m²'.format(lar, alt, area))
print('É necessário {}L de tinta para pintar toda a parede.'.format(tinta))