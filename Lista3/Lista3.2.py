'''2. Escreva um programa que peça ao usuário um número inteiro e diga se ele é par ou
ímpar.
Atenção: Crie uma função chamada par_ou_impar(numero) que retorne "par" ou
"ímpar".'''

def par_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"

#main

num = int(input('Insira um número inteiro: '))
print(par_impar(num))