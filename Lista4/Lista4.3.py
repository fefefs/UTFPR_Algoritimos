'''Para a feira de ciências da escola, Dustin vai fazer um programa que calcula diversas séries
numéricas matemáticas; crie um programa para cada uma das seguintes séries:
3) S = 1/1 - 2/4 + 3/9 - 4/16 + 5/25 - 6/36 ... - 10/100'''

s = 0
a = 1
b = 1

while b < 100 :
    if a%2 == 0:
        s += a/b
    else :
        s += a/b
    a += 1
    b += a**2
    
print(s)