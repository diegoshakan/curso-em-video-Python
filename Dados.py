import random

'''Aqui eu criei dois dados com base no Desafio19, com o método random eu fiz dois algorítmos
de dados, os que estão em comentários são a segunda forma.'''

#dado1 = random.randint(1, 6)
#dado2 = random.randint(1, 6)

dado1 = [1, 2, 3, 4, 5, 6]
dado2 = [1, 2, 3, 4, 5, 6]

print('Jogando dados...')

a = random.choice(dado1)
b = random.choice(dado2)


#soma = dado1 + dado2
soma = a + b

print(a)
print(b)
#print(dado1)
#print(dado2)
print('Ande {} casas'.format(soma))

if a == b:
    print('e jogue os dados de novo!')

#if dado1 == dado2:
#    print('e jogue os dados de novo!')