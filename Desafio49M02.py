'''Refaça o Desafio 09, mostrando a tabuada de um número que o usuário escolheu usando FOR.'''

num = int(input('Digite um número: '))
print('-=-' * 10)
cod = int(input('''Digite um código para escolher a operação:
[1] Adição
[2] Subtração
[3] Multiplicação
[4] Divisão
Escolha: '''))

for c in range(1, num + 1):
    if cod == 1:
        print('{} + {} = {}'.format(num, c, num + c))
    elif cod == 2:
        print('{} - {} = {}'.format(num, c, num - c))
    elif cod == 3:
        print('{} x {} = {}'.format(num, c, num * c))
    elif cod == 4:
        print('{} / {} = {}'.format(num, c, num / c))
print('-=-'*10)