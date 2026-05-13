'''1. Faça um programa que solicite o peso (em kg) e a altura (em metros) de uma pessoa
e calcule o seu IMC.
Em seguida, mostre em qual faixa a pessoa se encontra: - Abaixo de 18.5 → Abaixo do peso - Entre 18.5 e 24.9 → Peso normal
- Entre 25.0 e 29.9 → Sobrepeso - Acima de 30.0 → Obesidade
Atenção: Crie uma função chamada calcula_imc(peso, altura) que retorne o valor do
IMC e a classificação.'''

def calcula_imc(peso, altura):
    return peso / altura ** 2

#main

peso = float(input("Digite o peso: "))
altura = float(input("Digite o altura: "))
imc = calcula_imc(peso, altura)

if imc < 18.5:
    print("\nAbaixo do peso")
elif imc >= 18.5 and imc < 24.9:
    print("\nPeso normal")
elif imc >= 25.0 and imc < 29.9:
    print("\nSobrepeso")
elif imc >= 30.0 :
    print("\nObesidade")
