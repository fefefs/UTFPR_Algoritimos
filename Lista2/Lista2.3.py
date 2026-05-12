# 3) Marge está fazendo compras e chega na sessão de doces, porém como são três
# crianças e ela acha melhor evitar qualquer briga, quer apenas doces cujas unidades sejam
# divisíveis por três. Crie um programa que lê a quantidade de unidades de 4 produtos e diga
# quais são divisíveis por 3.

produto1 = int(input('Digite a quantidade do produto 1: '))
produto2 = int(input('Digite a quantidade do produto 2: '))
produto3 = int(input('Digite a quantidade do produto 3: '))
produto4 = int(input('Digite a quantidade do produto 4: '))

if produto1%3 == 0:
    print('\nO produto 1 tem a quantidade o suficiente')
if produto1%3 != 0:
    print('\nO produto 1 NÃO tem a quantidade o suficiente')

if produto2%3 == 0:
    print('\nO produto 2 tem a quantidade o suficiente')
if produto2%3 != 0:
    print('\nO produto 2 NÃO tem a quantidade o suficiente')

if produto3%3 == 0:
    print('\nO produto 3 tem a quantidade o suficiente')
if produto3%3 != 0:
    print('\nO produto 3 NÃO tem a quantidade o suficiente')

if produto4%3 == 0:
    print('\nO produto 4 tem a quantidade o suficiente')
if produto4%3 != 0:
    print('\nO produto 4 NÃO tem a quantidade o suficiente')


