
# print(liste_poules[]) Affiche une valeur à la position donnée
# print(max(liste_poules)) Trouve la valeur la plus haute de la liste (seulement les chiffres)
# print(min(liste_poules)) Trouve la valeur la plus basse de la liste (seulement les chiffres)
# print(len(liste_poules)) Trouve le nombre de valeurs dans une liste
# print(liste_poule.count(i)) Trouve la quantité d'une valeur dans une liste à l'index i

liste_poules = ["pouline", "poulette"] # La liste commence toujours à 0. La première variable est mise à la position 0
liste_poules.append("marie-poule") # Ajoute une variable à la liste
liste_poules.append("benoit")
liste_poules.insert(0,"yvette") # Insère une variable à la position spécifiée
print(liste_poules)
print(liste_poules[1])

nom_poule = liste_poules.pop() # Permet d'aller chercher une valeur précise à une position précise. Si vide, prend la valeur à la fin de la liste

for poule in liste_poules:
    print(poule)

for i in range(len(liste_poules)):
    print(liste_poules[i])

liste_avions = [40, 30, 20, 50, 10]
for avion in liste_avions:
    print(f"Avion #: {avion}")

print("Décollage en cours...")
liste_decollage = liste_avions.copy()
for avion in liste_avions:
    numero_avion = liste_decollage.pop(0)
    print(f"Décollage de l'avion {numero_avion}")

print("Décollage en cours...")
while(len(liste_avions) > 0):
    numero_avion = liste_avions.pop(0)
    print(f"Décollage de l'avion {numero_avion}")


valeurs = ["a", "b", "c", "b", "d", "e", "f"]

valeur_a_supprimer = "b"
while valeur_a_supprimer in valeurs:
    valeurs.remove(valeur_a_supprimer)

#valeurs.remove("b") # Permet d'aller retirer la première occurence seulement d'une valeur peut importe sa position
print(valeurs)


liste_valeurs = [10,20,44,22,11,35]
liste_valeurs.sort() # Trie la liste en ordre croissant ou en ordre alphabétique, mais est permanent
liste_valeurs.sort(reverse=True) # Trie la liste en ordre décroissant ou en order alphabétique inverse
liste_valeurs_triees = sorted(liste_valeurs) # Fait une copie de la liste, puis trie la copie
print(liste_valeurs)
print(liste_valeurs_triees)