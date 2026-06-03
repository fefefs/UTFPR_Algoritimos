'''Para a feira de ciências da escola, Dustin vai fazer um programa que calcula diversas séries
numéricas matemáticas; crie um programa para cada uma das seguintes séries:
2) S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50'''

s = 0
numerador = 1
denominador = 1

while denominador <= 50:
    s += numerador / denominador
    numerador += 2
    denominador += 1

print("O valor da série é:",s)