'''5.  Faça um programa que leia um ano e informe se ele é bissexto. Dica: Um ano é
bissexto se é divisível por 4 e não por 100, exceto se também for divisível por 400.
Atenção: Crie uma função chamada eh_bissexto(ano) que retorne True ou False.'''

def eh_bissexto(ano):
    if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
        return "Bissexto"
    else:
        return "Ano não bissexto"

#main
ano = int(input("Informe o ano : "))
res = eh_bissexto(ano)
print(res)
