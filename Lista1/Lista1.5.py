'''5) Crie um programa que calcula o gasto de energia em Km/MW (quilômetros por
megawatt) da nave espacial de Rick.
Dados:
KI = quilômetro inicial
KF = quilômetro final
CC = consumo de energia (em megawatts)
DP = distância percorrida; DP = KF - KI
GC = gasto de energia (Km/MW); GC = DP/CC'''

kI = float(input("Insira o valor do quilômetro inicial: "))
kF = float(input("Insira o valor do quilômetro final: "))
cC = float(input("insira o consumo de energia (em megawatts") )
dP = kF - kI
gC = dP/cC
print("O gasto de energia foi de :", gC)