# 2) Quando Homer estava tentando emagrecer, precisa de um jeito de monitorar seu peso,
# crie um programa que recebe sua altura (h) e calcule o peso ideal com base na seguinte
# fórmula: Peso ideal = (72.7*h)-58, então leia o peso atual de Homer, se o peso for maior
# que o peso ideal, escreva “faltam X kg para atingir o peso ideal), se o peso for menor ou
# igual ao peso ideal, escreva “parabens, voce atingiu seu peso ideal”

altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))

pesoIdeal = (72.7 * altura) - 58

if peso > pesoIdeal:
    print('\nfaltam ', peso - pesoIdeal, 'kg para atingir o seu peso ideal')
if peso <= pesoIdeal:
    print('\nParabens voce ja esta no seu peso ideal')
