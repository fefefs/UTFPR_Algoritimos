'''4) O radar da nave de Rick foi danificado, crie um novo programa para a nave que, medindo
a circunferência de um planeta calcule seu volume. Lembrando que a circunferência é
equivalente a 2𝜋R, sendo R a medida do raio, e o volume da esfera é dado por
V = 4𝜋𝑅³
3'''

raio = float(input("Insira o raio do circulo do planeta :"))
volume = (4*3.14*raio**2)/3

print("Este planeta tem o volume igual a :", volume)