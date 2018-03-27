'''Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal
e a forma de pagamento.
- À vista dinheiro/cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de acréscimo.
'''

preço = float(input('Quanto custa o produto: '))

cod = int(input('''   -=- Forma de Pagamento -=- 
[1] À Vista Dinheiro/Cheque [1] 
[2]     À Vista no Cartão   [2] 
[3]     Cartão até 2x       [3] 
[4]     Cartão 3x ou mais   [4] 
Aperte o código para o pagamento: '''))


car = preço - (preço * 0.05)
car2 = preço
car3 = preço + (preço * 0.2)

if cod == 1:
    preço = preço - (preço * 0.1)
    print('O valor do produto é R$ {:.2f} já com desconto de 10%.'.format(preço))
elif cod == 2:
    preço = preço - (preço * 0.05)
    print('O valor do produto é R$ {:.2f} já com desconto de 5%.'.format(preço))
elif cod == 3:
    print('O valor do produto é R$ {:.2f} preço sem alteração.'.format(preço))
elif cod == 4:
    preço = preço + (preço * 0.2)
    print('O valor do produto é R$ {:.2f} já com acréscimo de 20%.'.format(preço))
else:
    print('Código Inexistente!')