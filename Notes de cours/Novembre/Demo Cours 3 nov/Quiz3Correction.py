########################################################
# Auteur      = Mathew Bernard
# Date        = 3 novembre 2026
# Description = Quiz 3 correction
########################################################

########################################################
# Constantes
########################################################
NOM_PROFESSEUR = "David"

########################################################
# Fonctions
########################################################

# Fonction pour obtenir un nombre entier
def obtenir_nombre(nombre_minimal, nombre_maximal, type_nombre = "un nombre"):
    valide = False
    while not valide:
        try:
            nombre = int(input(f"Entrez {type_nombre} ({nombre_minimal} à {nombre_maximal}) : "))
            if nombre_minimal <= nombre <= nombre_maximal:
                valide = True
                return nombre
            else:
                print(f"La valeur doit être entre {nombre_minimal} et {nombre_maximal}.")
        except ValueError:
            print(f"Ce n'est pas un nombre entier.")

# Fonction pour obtenir un float

def obtenir_float(nombre_minimal, nombre_maximal, type_nombre = "un nombre"):
    valide = False
    while not valide:
        try:
            valeur_float = float(input(f"Entrez {type_nombre} ({nombre_minimal} à {nombre_maximal}) : "))
            if nombre_minimal <= valeur_float <= nombre_maximal:
                valide = True
                return valeur_float
            else:
                print(f"La valeur doit être entre {nombre_minimal} et {nombre_maximal}.")
        except ValueError:
            print(f"Ce n'est pas un nombre valide.")




########################################################
# Programme Principal
########################################################

nb_tortues = obtenir_nombre(5,10,"le nombre de tortues")

liste_tailles_tortues = []
for i in range(1,nb_tortues+1):
    #print(f"Tortue #{i}")

    # Lecture de la taille de la tortue
    taille_tortue = obtenir_float(10,25,"la taille")

    # Ajout de la taille dans la liste
    liste_tailles_tortues.append(taille_tortue)


print(f"Tailles saisies : {liste_tailles_tortues}")
liste_tailles_tortues.insert(1,12.3)
print(f"Tailles saisies après insertion : {liste_tailles_tortues}")
print(f"Nombre de tortues mesurées : {len(liste_tailles_tortues)}")

# la plus petite carapace
plus_petite_carapace = min(liste_tailles_tortues)
print(f"Carapace la plus petite : {plus_petite_carapace:.1f} cm")

# la plus grande carapace
plus_grande_carapace = max(liste_tailles_tortues)
print(f"Carapace la plus grande : {plus_grande_carapace:.1f} cm")

# Moyenne
moyenne_taille = sum(liste_tailles_tortues) / len(liste_tailles_tortues)
print(f"Longueur moyenne : {moyenne_taille:.2f} cm")

# Liste en ordre décroissant
liste_décroissante = sorted(liste_tailles_tortues, reverse=True)
print(f"De la plus grande à la plus petite : {liste_décroissante}")

# Les trois plus grandes tortues
print(f"Les 3 plus grandes : {liste_décroissante[0:3]}")