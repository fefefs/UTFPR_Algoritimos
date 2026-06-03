'''6) O laboratório de Hawkins fez uma pesquisa com 100 de seus funcionários, coletando
dados sobre o salário e número de filhos. A empresa deseja saber: a média salarial destes
funcionários; a média do número de filhos; e o percentual de pessoas com salário de até
$500,00, que possuem filhos.'''

sSal = 0
mSalarial = 0
pSF = 0
sFilhos = 0
MFilhos = 0

for i in range(0,100):
    sal = float(input(f"Insira salario do funcionárii {i}: "))
    nFilhos = int(input(f"Insira quantos filhos {i} tem: "))
    sSal += sal
    sFilhos += nFilhos
    if sal <= 500 and nFilhos > 0:
        pSF += 1

mSalarial = sSal / 100
mFilhos = sFilhos / 100
porc = (100*pSF)/100

print(f"A média salarial do laboratório Hawkins é de {mSalarial:.2f}.")
print(f"A média de filhos dos funcionários do laboratório é de {mFilhos:.2f}.")
print(f"O percentual de funcionários com salário de até 500 dólares que possuem filhos é de {porc}%.")