'''6. Crie um programa que peça um valor inteiro e mostre quantas cédulas de R$100,
R$50, R$20 e R$10 são necessárias para compor esse valor.
Atenção: Crie uma função chamada simula_caixa(valor) que retorne um dicionário com
a quantidade de cada cédula.'''

def simula_caixa(valor):
    n100 = 0
    n50 = 0
    n20 = 0
    n10 = 0
    if valor >= 100:
        n100 = valor // 100
        valor = valor - n100 * 100
        if valor >= 50 :
            n50 = valor // 50
            valor = valor - n50 * 50
            if valor >= 20 :
                n20 = valor // 20
                valor = valor - n20 * 20
                if valor >= 10 :
                    n10 = valor // 10
                    valor = valor - n10 * 10
    elif valor >= 50 :
        n50 = valor // 50
        valor = valor - n50 * 50
        if valor >= 20:
            n20 = valor // 20
            valor = valor - n20 * 20
            if valor >= 10:
                n10 = valor // 10
                valor = valor - n10 * 10
    elif valor >= 20 :
        n20 = valor // 20
        valor = valor - n20 * 20
        if valor >= 10:
            n10 = valor // 10
            valor = valor - n10 * 10
    elif valor >= 10 :
        n10 = valor // 10
        valor = valor - n10 * 10
    else:
        return "Valor invalido"
    return {'Notas de R$100': n100, 'Notas de R$50': n50,'Notas de R$20': n20, 'Notas de R$10': n10}

#main
valor = int(input("Insira o valor :"))
res = simula_caixa(valor)
print(res)