import csv

INDEX_COLONNE_NOM = 0
INDEX_COLONNE_NBVIES = 1

# liste_produit = []
# with open("menu.csv", "r", encoding="utf-8") as fichier:
#     lecteur = csv.reader(fichier,delimiter=";")
#     for champs in lecteur:
#         print(champs)



def sauvegarder_liste(liste_valeurs, liste_valeurs_entete, nom_de_fichier):# sauvegarder une liste en csv
    with open(nom_de_fichier, "w", encoding="utf-8", newline="") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(liste_valeurs_entete)
        ecrivain.writerows(liste_valeurs)


def main():
    liste_personnages = [
    ["Merlin", 3],
    ["Perlin", 4],
    ["Gamin", 10]
]

    sauvegarder_liste(liste_personnages, ["Nom", "Nombre de vie"], "personnage.csv")