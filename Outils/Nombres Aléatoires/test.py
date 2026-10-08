import random

equipes = ["Rouge", "Bleu", "Vert", "Jaune"]
print("Équipe qui commence :", random.choice(equipes))

cartes = ["As", "Roi", "Dame", "Valet", "10"]
random.shuffle(cartes)    # cartes est maintenant mélangée
print(cartes)

numeros_gagnants = random.sample(range(1, 50), 6)    # 6 numéros, sans doublon
print(sorted(numeros_gagnants))