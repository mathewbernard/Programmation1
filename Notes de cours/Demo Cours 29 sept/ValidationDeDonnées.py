# Auteur      : Mathew Bernard
# Date        : 2026-09-29
# Description : Exemple de try/except

print("Début")
# try:
#     age = int(input("Quel est ton âge? : "))
#     valeur_division = int(input("On divise par quoi? : "))
#     try:
#         age = age / valeur_division
#     except:
#         print("Une erreur est survenue!")
#     print("Bonjour!")

#     print (age)
# except NameError:
#     print("Il y a eu une erreur de nom de variable!")
# except ZeroDivisionError:
#     print("Vous ne pouvez pas diviser par zéro!")
# except ValueError:
#     print("Vous devez inscrire un chiffre!")
# except:
#     print("Une erreur est survenue!")

# valide = False
# while valide == False:
#     try:
#         age = int(input("Age? : "))
#         age = age + 1

#         valide = True
#     except:
#         print("Erreur")


# valide = False
# while not valide:
#     try:
#         prix = float(input("Entrez un prix : "))
#         valide = True
#     except ValueError:
#         print("Ce n'est pas un nombre valide.")




# nom = input("Entrez votre nom : ").strip()
# while nom == "":
#     print("Le nom ne peut pas être vide.")
#     nom = input("Entrez votre nom : ").strip()


# valide = False
# while not valide:
#     try:
#         note = int(input("Entrez une note (0 à 100) : ")) # ou conversion avec float()
#         if 0 <= note <= 100:
#             valide = True
#         else:
#             print("La note doit être entre 0 et 100.")
#     except ValueError:
#         print("Ce n'est pas un nombre entier.")


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



reponses_valides = ("o", "n", "y", "no", "yes", "oui", "non")

reponse = input("Continuer ? (o/n) : ").strip().lower()
while reponse not in reponses_valides:
    print("Réponse invalide.")
    reponse = input("Continuer ? (o/n) : ").strip().lower()



print("Fin")