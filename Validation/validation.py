
#--------------------------------------------------------------------------------------------------------------------------------
# Valider un Entier
#--------------------------------------------------------------------------------------------------------------------------------

valide = False
while not valide:
    try:
        age = int(input("Entrez votre âge : "))
        valide = True
    except ValueError:
        print("Ce n'est pas un nombre entier.")

#--------------------------------------------------------------------------------------------------------------------------------
# Valider un nombre réel
#--------------------------------------------------------------------------------------------------------------------------------

valide = False
while not valide:
    try:
        prix = float(input("Entrez un prix : "))
        valide = True
    except ValueError:
        print("Ce n'est pas un nombre valide.")

#--------------------------------------------------------------------------------------------------------------------------------
# Valider une chaine non vide
#--------------------------------------------------------------------------------------------------------------------------------

nom = input("Entrez votre nom : ").strip()
while nom == "":
    print("Le nom ne peut pas être vide.")
    nom = input("Entrez votre nom : ").strip()

#--------------------------------------------------------------------------------------------------------------------------------
# Valider un intervalle numérique
#--------------------------------------------------------------------------------------------------------------------------------

valide = False
while not valide:
    try:
        note = int(input("Entrez une note (0 à 100) : ")) # ou conversion avec float()
        if 0 <= note <= 100:
            valide = True
        else:
            print("La note doit être entre 0 et 100.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

#--------------------------------------------------------------------------------------------------------------------------------
# Valider l'appartenance à un ensemble de valeurs
#--------------------------------------------------------------------------------------------------------------------------------

# Exemple avec des entiers (menu)

choix_valides = (1, 2, 3, 4)

valide = False
while not valide:
    try:
        choix = int(input("Votre choix (1 à 4) : "))
        if choix in choix_valides:
            valide = True
        else:
            print("Choix invalide.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

# Exemple avec des chaîne de caractères

reponses_valides = ("o", "n")

reponse = input("Continuer ? (o/n) : ").strip().lower()
while reponse not in reponses_valides:
    print("Réponse invalide.")
    reponse = input("Continuer ? (o/n) : ").strip().lower()