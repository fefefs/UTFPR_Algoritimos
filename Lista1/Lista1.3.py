'''3) Uma bomba de neutrinos é capaz de destruir um volume de 10 ua³ (unidades
astronômicas ao cubo), crie um programa que dado o valor do volume (em ua³) de um local
do espaço, calcule quantas bombas seriam necessárias para destruí-lo'''

volume = float(input("Insira o volume de um local do espaço em ua³ :"))
print("Serão nescessarias {0} bombas para destruir esse local".format(volume/10))