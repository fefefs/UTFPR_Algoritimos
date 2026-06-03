'''7) Em uma pesquisa de campo na cidade de Hawkins. Indiana, uma editora solicitou os
seguintes dados para os entrevistados: sexo, idade e quantidade de livros que leu no ano
de 2010. Faça um programa que leia os dados digitados pelo usuário, sendo que deverão
ser solicitados dados até que a idade digitada seja um valor negativo. Depois, calcule e
imprima: 1. A quantidade total de livros lidos pelos entrevistados menores de 10 anos. 2. A
quantidade de mulheres que leram 5 livros ou mais. 3. A média de idade dos homens que
leram menos que 5 livros. 4. O percentual de pessoas que não leram livros.'''
sF = 0
sIdades = 0
nLivros = 0
s = 0
qL = 0
mH = 0
sH = 0
pP = 0
idade = 0

for i in range(0,5) :
    s += 1
    idade = int(input("Insira sua idade :"))
    sexo = input("Indira o sexo f para Feminino e m para Masculino: ")
    livros = int(input("Insira sua quantidade de livros que leu em 2010 :"))
    if idade < 10:
        qL += livros
    if sexo == "f"  and livros >= 5 :
        sF += 1
    if sexo == "m" and livros < 5 :
        sH += 1
        sIdades += idade
    if livros == 0 :
        nLivros += 1

mH = sIdades / sH
pP = (100*nLivros)/s

print(f"A quantidade total de livros lidos pro menosres de 10 anos foi {qL} livros")
print(f"A quantidade total de mulheres que leram 5 livros ou mais foi de {sF} mulheres")
print(f"A média de idade de homens que leram menos de 5 livros é {mH}")
print(f"A porcentagem de pessoas que não leram nenhum livro é {pP}")


