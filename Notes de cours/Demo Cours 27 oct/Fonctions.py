#============================================================================================================
# Suite des listes
#============================================================================================================

# eleves = [
#     [
#         [1,2],
#         [3,4],
#         [5,6,100]
#     ],
#     [
#         [7,8],
#         [9,10],
#         [11,12,100]
#     ],
#     [
#         [1,1],
#         [1,1],
#         [1,1,100]
#     ],
#     [
#         [0,0],
#         [0,0],
#         [0,0,100]
#     ]
# ]

# nom_eleves = [
#     "Gabriel",
#     "Steve",
#     "Antoine",
#     "Mathew"
# ]

# nom_examens = [
#     "le quiz #1",
#     "le quiz #2",
#     "l'examen intra"
# ]

# # for eleve in eleves:
# #     # pour tous les élèves
# #     for note in eleve:
# #         print(note)
# #     print("-"*7)


# for i in range(len(eleves)):
#     print(f"Liste des notes de {nom_eleves[i]}:")
#     for j in range(len(eleves[i])):
#         print(f"Note pour {nom_examens[j]} :")
#         for k in range(len(eleves[i][j])):
#             print(f"Note: {eleves[i][j][k]}")
              
#     print("-"*15)

#============================================================================================================
# Fonctions
#============================================================================================================

########################### fonction afficher_carre ###########################
def afficher_rectangle(hauteur, largeur, motif="*"):
    if hauteur == largeur:
        forme = "carré"
    else:
        forme = "rectangle"

    print(f"Début de mon {forme}")
    for i in range(hauteur):
        for j in range(largeur):
            print(f"{motif} ", end="")
        print("")
    print(f"Fin de mon {forme}")
    print("")

def afficher_carre(hauteur, motif="*"):
    largeur = hauteur
    afficher_rectangle(hauteur, largeur, motif)


def calculer_aire_carre(hauteur):
    largeur = hauteur
    aire_carre = hauteur * largeur
    return aire_carre

########################### programme principal ###########################
# for i in range(1,5):
#     # afficher_carre(i, "#")
#     afficher_rectangle(i, i, "*")
for i in range(1,100):
    valeur_aire = calculer_aire_carre(i)
    print(f"La valeur de l'aire est: {valeur_aire}")