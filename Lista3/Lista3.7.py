'''7. Faça 3 perguntas ao usuário (respostas 'sim' ou 'não') e classifique: - 0 sim → "Você é um anjo!" -
1 ou 2 sim → "Hmm... tenho dúvidas." - 3 sim → "Detector explodiu!"
Atenção: Crie função chamada analisa_respostas(resp1, resp2, resp3).'''

def analisa_respostas(resp1, resp2, resp3):
    if resp1 == 'sim' and resp2 == 'sim' and resp3 == 'sim':
        return "Detector explodiu!"
    elif resp1 == 'sim' or resp2 == 'sim' or resp3 == 'sim' :
        return "Humm ... tenho duvidas"
    elif resp1 == 'não' and resp2 == 'não' and resp3 == 'não' :
        return "Você é um anjo!"


#main
p1 = input("pergunta 1 : ")
p2 = input("pergunta 2 : ")
p3 = input("pergunta 3 : ")
res = analisa_respostas(p1, p2, p3)
print(res)
