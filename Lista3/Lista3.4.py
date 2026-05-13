'''4 Escreva um programa que leia três números e informe qual deles é o maior.
Atenção: Crie uma função chamada maior_de_tres(a, b, c) que retorne o maior valor.'''

def maior_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c

#main

n1 = int(input("Insira o primeiro valor : "))
n2 = int(input("Insira o segundo valor : "))
n3 = int(input("Insira o terceiro valor : "))
res = maior_de_tres(n1, n2, n3)
print("O maior valor entre os três é :", res)

