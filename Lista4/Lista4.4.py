'''Para a feira de ciências da escola, Dustin vai fazer um programa que calcula diversas séries
numéricas matemáticas; crie um programa para cada uma das seguintes séries:
4) S(n) =  1 + 1/X² + 1/X³ + 1/X4 + … +1/Xn Sendo “n” um valor informado pelo usuário.'''

n = int(input("Insira o valor maximo de n:"))
x = int(input("Insira o valor de x:"))
s = 0

for i in range(1,n+1):
    s += 1/x**i
    print(s)
print(s)