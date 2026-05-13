'''3. Um mercado oferece descontos nas compras com base no valor gasto por cada
cliente. Solicite o valor da compra e calcule o valor final com desconto conforme regras
a seguir: - Até R$ 100 → 0% - R$ 100,01 até R$ 200 → 10% - Acima de R$ 200 → 20%
Atenção: Crie uma função chamada calcula_desconto(valor). '''

def calcula_desconto(valor):
    if valor <= 100:
        return valor
    elif valor > 100 and valor <= 200:
        valor = (valor - (valor * 0.10))
        return valor
    elif valor > 200:
        valor = (valor - (valor * 0.20))
        return valor

#main

valor = float(input('Insira o valor da compra: '))
valorF = calcula_desconto(valor)
print('O valor da compra com desconto foi {}'.format(valorF))