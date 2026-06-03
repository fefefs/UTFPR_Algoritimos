'''8) Foi feita uma pesquisa para saber o perfil dos alunos que cursam o ginásio da escola de
Hawkins. Cada aluno fornecia a sua idade, série (primeira-1, segunda-2, terceira-3 ou
quarta-4), quantos livros liam por mês e se gostavam de fazer redação (Sim-1 ou Não-0).
Fazer um programa que leia os dados, calcule e imprima:
1. A quantidade de alunos que está na terceira série;
2. A maior quantidade de livros lidos por um aluno que está na quarta série;
3. A porcentagem de alunos que não gostam de fazer redação e que estão na terceira série.
4. Média de idade dos alunos da primeira e segunda séries.
OBS: A condição de parada (flag) é que seja digitado 0 (zero) para idade'''
qnt3 = 0
leitor4 = -1
qntRed = 0
qnt12 = 0
idade12 = 0
a = int(input("Insira a quantidade de alunos de Hawkins:"))
for i in range(1,a+1):
    # Serie ---------------------------------------------------------------------------------------
    serie = int(input(f"\nInsira a série do {i}° aluno(a):"))
    while serie < 1 or serie > 4:
        serie = int(input(f"Série Invalida! Insira novamente a série do {i}° aluno(a):"))
    if serie == 3:
        qnt3 += 1
    elif serie == 1 or serie == 2:
        qnt12 += 1

    # Idade ---------------------------------------------------------------------------------------
    idade = int(input(f"Insira a idade do {i}° aluno(a):"))
    if serie == 1 or serie == 2:
        idade12 += idade

    #Livros ---------------------------------------------------------------------------------------
    qntLivros = int(input(f"Insira a quantidade de livros que o {i}° aluno(a) lê por mês:"))
    while qntLivros < 0 :
        qntLivros = int(input(f" Quantidade invalida, insira novamente!\n Insira a quantidade de livros que o {i}° aluno(a) lê por mês:"))
    if serie == 4:
        if qntLivros > leitor4:
            leitor4 = qntLivros

    # Redação ---------------------------------------------------------------------------------------
    red = int(input(f"O {i}° aluno(a) gosta de fazer redação? (Sim-1 ou Não-0): "))
    while red != 1 and red != 0:
        red = int(input(f" Resposta invalida, Insira novamente!\n O {i}° aluno(a) gosta de fazer redação? (Sim-1 ou Não-0): "))
    if serie == 3 and red == 0 :
        qntRed += 1


print("\n\nDADOS CALCULADOS:")
print(f"\nA quantidade de alunos que está na terceira série é de {qnt3} alunos")
if leitor4 == -1:
    print("Não temos alunos da 4° serie!")
else :
    print(f"A maior quantidade de livros lidos por um aluno que está na quarta série é de {leitor4} livros")
if qntRed == 0 :
    print("Não tem alunos na terceira serie que não gostam de fazer redação!")
else:
    pR = (100 * qntRed) / qnt3
    print(f"A porcentagem de alunos que não gostam de fazer redação e que estão na terceira série é de {pR}%")
print(f"Média de idade dos alunos da primeira e segunda séries é de {idade12/qnt12} anos")

