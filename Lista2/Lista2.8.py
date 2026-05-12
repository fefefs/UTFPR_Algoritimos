'''8) Em aulas extras de programação,
bart sempre esquecia o ponto e
vírgula no final da linha, crie um
programa que leia quantas vezes ele
errou (5,10 ou 15) e escreva na tela
esse mesmo número de vezes a
seguinte frase: Não devo esquecer o ponto e virgula no final da linha;'''

#main

erro = int(input("Digite quantas vezes o Bart errou :"))
for i in range(0, erro):
    print("Não devo esquecer o ponto e virgula no final da linha;")