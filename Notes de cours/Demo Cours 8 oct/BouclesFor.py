print("Début")

# range(100   ,  0   ,  -1 )
#       Début   Fin    Changement
# for i in range(100,0,-1):
#     print(f"je tourne... tour #{i}")
#     print("...")

# nom = "david"
# for c in nom:
#     print(c)

# nom = "david"
# for caractere in nom:
#     print(caractere)

# nom = "david"
# for lettre in nom:
#     print(lettre)


# liste_personnage = ("Mario", "Luigi", "Peach", "Toad", "Bowser", "Tortue")
# for personnage in liste_personnage:
#     print(f"Mon personnage se nomme: {personnage}")

# for i in range(10,0,-1):
#     print(f"{i} secondes...")
# print("Décollage")

# valide = False
# while not valide:
#     try:
#         nb_tours = int(input("Entrez un nombre de tours (1 à 5) : ")) # ou conversion avec float()
#         if 1 <= nb_tours <= 5:
#             valide = True
#         else:
#             print("Le nombre de tours doit être entre 1 et 5.")
#     except ValueError:
#         print("Ce n'est pas un nombre entier.")

# for i in range(1, nb_tours+1):
#     print(f"Tour #{i}")



valide = False
while not valide:
    try:
        nb_ligne = int(input("Entrez un nombre de ligne (1 à 5) : ")) # ou conversion avec float()
        if 1 <= nb_ligne <= 5:
            valide = True
        else:
            print("Le nombre de ligne doit être entre 1 et 5.")
    except ValueError:
        print("Ce n'est pas un nombre entier.")

nb_colonne = nb_ligne # c'est un carré... c'est pareil...
for i in range(nb_ligne):
    for j in range(nb_colonne):
        print("*", end="")
    print("")
    nb_colonne -= 1 # ça fait un triangle si l'on rajoute cette ligne




print("Fin")