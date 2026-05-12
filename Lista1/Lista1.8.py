'''8) O tempo de uma viagem espacial é dado em segundos, crie um programa que lê o tempo
ao início da viagem TI e o tempo final na chegada TF, então escreva na tela o tempo total
em horas, minutos e segundos'''

tI = float(input("Insira o tempo inicial da viagem em segundos: "))
tF = float(input("Insira o tempo final da viagem em segundos: "))
tempo_total = tF - tI

# Conversão para horas, minutos e segundos
horas = tempo_total // 3600
minutos = (tempo_total % 3600) // 60
segundos = tempo_total % 60

# Exibição do resultado
print(f"Tempo total da viagem: {horas}h {minutos}m {segundos}s")