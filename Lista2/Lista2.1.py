#1) O salário dos trabalhadores da usina nuclear de Springfield são definidos pelo salário
# base acrescido de um valor extra de 10% por filho menor que 14 anos quando o cônjuge
# não trabalha, e 5% por filho quando o cônjuge trabalha. Crie um programa que pergunta o
# salário base, a quantidade de filhos menor que 14 anos e se o cônjuge trabalha ou não (1
# para sim, 0 para não).

salario = float(input('insira o seu salario:' ))
filhos = int(input('\nInsira a quantitate de filhos menores de 14 anos: '))
conjuge = int(input('Caso o seu cônjuge trabalhe insira 1 para sim e 0 para não: '))

if conjuge == 1:
    salarioF = salario + (salario * (filhos * 0.05))
    print('\nseu salario é: ', salarioF)
if conjuge == 0:
    salarioF = salario + (salario * (filhos * 0.10))
    print('\nseu salario é: ', salarioF)