#Auteur  :   Mathew Bernard
#Date    :   2026-09-22
#Sujet   :   Exerice 22 septembre


##EXERCICE 5.1 - LA BOUCLE WHILE

#Execrice 1

compteur = 10

while compteur > 0:
    print(compteur)
    compteur -= 1


print("Décollage!")


#Exercice 2


note = int(input("Entrez une note entre 0 et 100 inclusivement: "))

while note < 0 or note > 100:
    print("Erreur")
    note = int(input("Entrez une note valide: "))

print(f"Votre note est {note}")


#Exercice 3

#a. while == continuer
#b. while == not trouve
#c. while == not partie_terminee
#d. continuer = (respone == "o")


#Exercice 4


# nombre_entier = int(input("Entrez un nombre entier de 1 à 12: "))

# while nombre_entier < 1 or nombre_entier > 12:
#     print("Nombre invalide")
#     nombre_entier = int(input("Entrez un nombre valide: "))


# multiplicateur = 1
# while multiplicateur <= 12:
#     print(nombre_entier, "x", multiplicateur, "=", nombre_entier * multiplicateur,)
#     multiplicateur += 1


#Exercice 5

# while True:
#     mot_de_passe = input("Entrez le mot de passe : ").strip()
#     if mot_de_passe == "python123":
#         break
#     print("Accès refusé.")
# print("Accès autorisé !")


#Exercice 6


i = 0
j = 0

taille = int(input("Quelle est la taille du carré: "))
recommencer = "o"

while recommencer == "o":
 i = 0
 while i < taille :
    j = 0
    while j < taille:
       print("*", end="")
       j += 1
    i += 1
    print("")
 recommencer = str(input("Un autre ? (o/n): "))


#Exercice 7


