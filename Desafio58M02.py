from random import randint
from time import sleep

'''Melhore o jogo do Desafio 28, onde o computador irá pensar em um número de 1 a 10.
o jogador vai palpitar até acertar e irá mostrar quantas tentativas ele teve até o acerto.'''

num = randint(1, 10)
cont = 1
print('Se eu pensar em um número entre 1 e 10, será que você consegue acertar? Vamos lá!')
sleep(1.0)
palpite = int(input('Qual é o seu palpite: '))

while num != palpite:
    if palpite < num:
        palpite = int(input('Arrow! o número que estou pensando é maior. Tente outra vez: '))
    else:
        palpite = int(input('Arrow! o número que estou pensando é menor. Tente outra vez: '))
    cont += 1
if cont == 1:
    print(f'Você é um mentalista! Você acertou na {cont}ª tentativa.')
elif cont > 1 and cont <= 4:
    print(f'Você foi bem! Você acertou na {cont}ª tentativa.')
elif cont >= 5 and cont <= 7:
    print(f'Antes tarde do que nunca! Você acertou na {cont}ª tentativa.')
elif cont > 7 and cont <= 9:
    print(f'Acertou, já tava ficando chato! Você acertou na {cont}ª tentativa.')
else:
    print(f'Não desanime, você acertou na décima tentativa.')

