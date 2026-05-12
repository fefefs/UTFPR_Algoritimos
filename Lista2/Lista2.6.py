# 6) Sr. Burns está com problemas com fiscais do governo pois sua usina nuclear polui
# demais, o máximo admitido pelo governo é 1 tonelada de resíduos por mês nos rios e 10
# toneladas de resíduos enterrados por ano, com isso, crie um programa que dadas a
# quantidade em quilogramas de resíduos jogados no rio e a quantidade de resíduos
# enterrados, imprima as seguintes mensagens mediante as condições:
#   ● Se a quantidade de resíduos enterrados for maior que o aceitável, porém a
# quantidade jogada no rio for menor ou igual a aceitável, imprima “jogar mais
# resíduos no rio!”
#   ● Se a quantidade de resíduos enterrados for maior que o aceitável, porém a
# quantidade enterrada for menor ou igual a aceitável, imprima “enterrar mais
# resíduos!”
#   ● Se ambas as quantidades forem aceitáveis imprima “tudo certo!”
#   ● Se ambas estiverem fora do aceitável, imprima “infelizmente teremos que poluir
# menos”

RRio = float(input('Digite a quantidade de resíduos jogados no rio no mês: '))
RSolo = float(input('Digite a quantidade de resíduos enterrados no ano: '))

if RSolo > 10000 and RRio <= 1000:
    print('jogar mais resíduos no rio!')
elif RSolo <= 10000 and RRio > 1000:
    print('enterrar mais resíduos!')
elif RSolo <= 10000 and RRio <= 1000:
    print('Tudo certo!')
elif RSolo > 10000 and RRio > 1000:
    print('infelizmente teremos que poluir menos')