#------------------------------------------------------------------------
# 1-Importer le module random
#------------------------------------------------------------------------

import random

#------------------------------------------------------------------------
# 2-Générer des nombres entiers
#------------------------------------------------------------------------

#       Nom	                                                        Description	                                        Paramètres	           Retour	                    Exemple(s)
# random.randint(a, b)	                        Entier aléatoire entre a et b, les deux bornes incluses.	    a, b : entiers, a <= b	        int	                random.randint(1, 6) → 4
# random.randrange(fin)	                        Entier aléatoire de 0 à fin exclu.	                            fin : entier	                int	                random.randrange(10) → 7
# random.randrange(debut, fin, pas)	            Entier aléatoire choisi parmi range(debut, fin, pas).	        Mêmes règles que range()	    int	                random.randrange(0, 101, 5) → 35

import random

de = random.randint(1, 6)
print("Vous avez obtenu", de)

nombre_pair = random.randrange(0, 21, 2)    # 0, 2, 4, ..., 20
print("Nombre pair aléatoire :", nombre_pair)

#------------------------------------------------------------------------
# 3-Générer des nombres réels
#------------------------------------------------------------------------

#       Nom	                                                    Description	                                  Paramètres	        Retour	            Exemple(s)
# random.random()	                            Réel aléatoire entre 0.0 (inclus) et 1.0 (exclu).	            Aucun	            float	    random.random() → 0.4387...
# random.uniform(a, b)	                        Réel aléatoire entre a et b.	                                a, b : nombres	    float	    random.uniform(15, 25) → 19.84...

temperature = round(random.uniform(-10, 30), 1)
print(f"Température simulée : {temperature} °C")

# Événement qui se produit 30 % du temps
if random.random() < 0.3:
    print("Il pleut!")

#------------------------------------------------------------------------
# 4-Choisir dans une liste
#------------------------------------------------------------------------

#       Nom	                            Description	                                            Paramètres	                         Retour	                         Exemple(s)
# random.choice(seq)	        Un élément choisi au hasard.	                    seq : liste, chaîne ou tuple non vide	    Un élément de seq	     random.choice(["pile", "face"]) → 'face'
# random.sample(seq, k)	        k éléments différents, choisis au hasard.	        seq : séquence, k : entier <= len(seq)	    Nouvelle list	         random.sample(range(1, 50), 6) → [12, 3, 44, 27, 8, 31]
# random.shuffle(liste)	        Mélange la liste elle-même. Ne retourne rien.	    liste : une liste	                        None	                 Voir l'exemple ci-dessous

equipes = ["Rouge", "Bleu", "Vert", "Jaune"]
print("Équipe qui commence :", random.choice(equipes))

cartes = ["As", "Roi", "Dame", "Valet", "10"]
random.shuffle(cartes)    # cartes est maintenant mélangée
print(cartes)

numeros_gagnants = random.sample(range(1, 50), 6)    # 6 numéros, sans doublon
print(sorted(numeros_gagnants))

#------------------------------------------------------------------------
# 5-Reproduire les résultats avec seed()
#------------------------------------------------------------------------

import random

random.seed(42)
print(random.randint(1, 100), random.randint(1, 100))    # toujours les mêmes deux nombres

random.seed(42)
print(random.randint(1, 100), random.randint(1, 100))    # identiques à la ligne précédente

#------------------------------------------------------------------------
# 6-Usage typiques avec les boucles
#------------------------------------------------------------------------

# Lancer un dé plusieurs fois et compter les résultats

NB_LANCERS = 1000
nb_six = 0
for _ in range(NB_LANCERS):
    if random.randint(1, 6) == 6:
        nb_six += 1
print(f"6 obtenu {nb_six} fois ({nb_six / NB_LANCERS:.1%})")

# Remplir une liste de valeur aléatoires

notes = []
for _ in range(10):
    notes.append(random.randint(40, 100))
print(notes)

# Jeu «Devine le nombre»

secret = random.randint(1, 100)
essai = int(input("Devinez un nombre entre 1 et 100 : "))
while essai != secret:
    if essai < secret:
        print("Plus grand!")
    else:
        print("Plus petit!")
    essai = int(input("Essayez encore : "))
print("Bravo!")