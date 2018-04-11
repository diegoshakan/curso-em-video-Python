from time import sleep

'''Crie um programa que leia dois valores e mostre um menu. Seu programa deverá realizar
a operação em cada caso:
[1] Somar
[2] Multiplicar
[3] Maior e Menor
[4] Inserir novos números
[5] sair do programa.
'''
print('~'*30)
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
print('~'*30)
opcao = 0

while opcao.upper != 5 and opcao in 'SN':
    print('''    [1] Soma
    [2] Multiplicação
    [3] Maior e Menor
    [4] Inserir novos números
    [5] Sair do programa''')
    opcao = int(input('Qual é sua opção: '))

    if opcao == 1:
        print(f'Soma de {a} + {b} = {a+b}')
    elif opcao == 2:
        print(f'Multiplicação de {a} * {b} = {a*b}')
    elif opcao == 3:
        if a > b:
            print(f'O primeiro número é {a} e é maior que o segundo número {b}')
        elif a < b:
            print(f'O segundo número é {b} e é maior que o primeiro {a}')
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        a = int(input('Digite um novo número: '))
        b = int(input('Digite outro novo número: '))
    elif opcao == 5:
        break
    else:
        print('Opção inexistente! Digite novamente.')
    print('~' * 30)
    sleep(1.0)




print('Você saiu do programa! Até mais!')