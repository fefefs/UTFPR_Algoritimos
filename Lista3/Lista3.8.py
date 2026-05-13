'''8. Simulador de Café Personalizado
Peça ao usuário: tipo de café, colheres de açúcar e copo térmico.
Monte uma mensagem criativa com as escolhas.
Atenção: Crie uma função chamada monta_pedido(tipo, acucar, termico).'''

def monta_pedido(tipo, acucar, termico):
    return {'Aqui está o seu café': tipo, 'com': acucar, 'colheres de açucar e no copo' :termico}


#main
t = input("Qual tipo de café você deseja? ")
a = int(input("Quantas colheres de açucar? "))
c = input("Qual copo termico vc quer? ")
res = monta_pedido(t,a,c)
print(res)