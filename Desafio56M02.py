'''Crie um programa que leia o nome de quatro pessoas, idade e o sexo e mostre:
1- A média de idade do grupo:
2 - Qual é o nome do homem mais velho
3 - Quantas mulheres tem menos de 20 anos.
'''

soma = 0
cont = 0
contm = 0
velhonome = ''
velhoidade = 0

for c in range(1, 5):
    nome = input('Digite um nome: ')
    idade = int(input('Idade: '))
    cont += 1  # este contador será usado para contar a variável para fazer a média.
    soma = soma + idade # soma para fazer a média da idade do grupo.
    sexo = input('Sexo [M/F]: ')
    if sexo in 'Mm' and idade > velhoidade: # verificar se é homem e se sua idade é maior que a idade inicial e as demais.
        velhoidade = idade
        velhonome = nome
    if sexo in 'Ff' and idade < 20:
        contm += 1
print(f'A média das idades {soma / cont}.') # F-String print(f'{exemplo}') substitui o .format() no python3.6
print(f'O homem mais velho se chama {velhonome} e tem {velhoidade} anos.')
print(f'Há {contm} mulher(es) menor(es) de 20 anos.')
