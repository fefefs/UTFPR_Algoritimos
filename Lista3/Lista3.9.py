'''9. O programa escolhe um número entre 1 e 10 e o usuário tem 3 tentativas para
adivinhar.
Dica se o número é maior ou menor a cada tentativa.
Atenção: Crie funções chamadas gera_numero(),  verifica_chute() e jogar(). '''
import random


def gera_numero():
    n = random.randint(1, 10)
    return n

def verifica_chute(chute, n):
    if chute == n:
        return "Correto!!"
    else:
        if chute < n:
            return "Errado, o número é mais alto"
        else:
            return "Errado, o número é mais baixo"

def jogar():
    n = gera_numero()
    c = 0
    t =0
    while t < 3 and c != n:
        c = int(input("Insira o seu chute :"))
        res = verifica_chute(c, n)
        print(res)
        t += 1

#main
jogar()
print('O jogo acabou!')
