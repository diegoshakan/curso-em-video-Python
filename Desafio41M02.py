from datetime import date
from time import sleep

'''Faça um programa que leia a data de nascimento de um atleta e informe a sua categoria:
- Até 9 anos, mirim;
- Até 14 anos, infantil;
- Até 19 anos, Juvenil;
- Até 20 anos, Sênior;
- Acima de 20 anos, master.
'''

ano = date.today().year

nasc = int(input('Qual o seu ano de nascimento: '))

cat = ano - nasc

if cat <= 9:
    print('Sua idade {} anos, categoria MIRIM.'.format(cat))
elif cat > 9 and cat <= 14:
    print('Sua idade {} anos, categoria INFANTIL.'.format(cat))
elif cat > 14 and cat <= 19:
    print('Sua idade {} anos, categoria JUVENIL.'.format(cat))
elif cat > 19 and cat <=20:
    print('Sua idade {} anos, categoria SÊNIOR.'.format(cat))
elif cat > 20:
    print('Sua idade {} anos, categoria MASTER.'.format(cat))
else:
    print('Categoria Inexistente!')