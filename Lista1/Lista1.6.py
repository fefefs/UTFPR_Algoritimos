'''6) Duas pessoas investem em uma missão de exploração espacial. Crie um programa que
dados os valores que cada um investiu, distribua proporcionalmente os lucros da missão
entre eles. O programa deve ler investimento 1, investimento 2 e lucro, e como saída falar
quanto recebeu o investidor 1 e o investidor 2.'''

inv1 = float(input("Insira o valor do investimento 1: "))
inv2 = float(input("Insira o valor do investimento 2: "))
lucro = float(input("Insira o valor do lucro: "))
totalInv = inv1 + inv2
recebido1 = (inv1 / totalInv) * lucro
recebido2 = (inv2 / totalInv) * lucro

print(f"O investidor 1 receberá: R$ {recebido1:.2f}")
print(f"O investidor 2 receberá: R$ {recebido2:.2f}")