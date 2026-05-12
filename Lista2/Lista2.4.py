# 4) A temperatura de um exaustor na Usina Nuclear de Springfield deve estar entre 120º C e
# 140º C para estar em funcionamento normal, menos que isso e provavelmente há um mal
# funcionamento e mais que isso há risco de ocorrer um acidente. Crie um programa que
# recebe como entrada a temperatura do exaustor e então calcula se ela está no intervalo
# seguro ou maior ou menor e imprima uma mensagem adequada a situação.

temp = int(input('Digite a temperatura do exautor: '))

if temp >= 120 and temp <= 140:
    print('\nA temperatura está adequada!')
else:
    if temp < 120:
        print('\nA temperatura está a baixo da adequada!')
    else:
        if temp > 140:
            print('\nA temperatura está a cima da adequada!')
