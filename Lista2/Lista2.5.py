# 5) Para participar de uma viagem da escola, não pode reprovar, considere 3 provas P1, P2
# e P3, crie um programa que lê as 3 notas, calcula a média ponderada entre as três notas,
# com a seguinte fórmula:
# Sendo a tabela de notas a seguinte:
# ● MP >=9 → A
# ● MP >=8 e MP<9 → B
# ● MP >=7 e MP<8 → C
# ● MP >=5 e MP<7 → D
# ● MP <5 → F
# (A,B,C → Aprovado / D,F → Reprovado)
# O programa deve dizer a nota (letra) e se Bart poderá ou não ir na viagem.

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

notaPonderada = (nota1*3 + nota2*3 + nota3*4)/10

if notaPonderada >= 9:
    print('\nA nota de Bart foi A então ele poderá ir a viajem!')
elif notaPonderada >= 8 and notaPonderada < 9:
    print('\nA nota de Bart foi B então ele poderá ir a viajem!')
elif notaPonderada >= 7 and notaPonderada < 8:
    print('\nA nota de Bart foi C então ele poderá ir a viajem!')
elif notaPonderada >= 5 and notaPonderada < 7:
    print('\nA nota de Bart foi D então ele não poderá ir a viajem')
elif  notaPonderada < 5:
    print('\nA nota de Bart foi F então ele não poderá ir a viajem')
