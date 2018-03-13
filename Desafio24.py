# Desafio 24 - Gustavo Guanabara
'''Crie um programa que leia um nome de cidade e diga se ela começa ou não com o nome SANTO'''

cid = input("Digite o nome da Cidade: ").strip()
cid1 = cid.lower().split() #Aqui ele coloca a string em minúscula e a separa para conferir.

if cid1[0] == 'santo' or cid1[0] == 'são' or cid1[0] == 'san': #Aqui a condicional e a comparação.
    print('O nome da cidade começa com \"SANTO\" ou \"SÃO\" ou \"SAN\"') #Santo é o mesmo que São e San fiz um adendo.
else:
    print('O nome da cidade não começa com \"SANTO\" ou \"SÃO\" ou \"SAN\"')
print('Nome da cidade é {}'.format(cid)) #Aqui ele imprime o nome sem formatação, assim como recebeu.
