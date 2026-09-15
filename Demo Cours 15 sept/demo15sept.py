# auteur: Mathew Bernard
# date: 15 septembre 2026
# description: Exemple du cours


# age = int(input("Quel est ton age?:"))
avoir_faim_oui_non = bool(input("As-tu faim? Oui ou Non:"))
avoir_faim = (True if (avoir_faim_oui_non == "Oui") else False)

# if(avoir_faim == "Oui" or "oui"):
#     valeur_avoir_faim = True
# else:
#     valeur_avoir_faim = False





# if(age >= 90):
#     print("Très très vieux")
# elif(age >= 80):
#     print("Un peu moins vieux")
# elif(age >= 40):
#     print("Petite jeunesse")
# else:
#     print("Jeune")







jour = 2

match jour:
    case 1:
        print("Lundi")
    case 2:
        print("Mardi")
    case 3:
        print("Mercredi")
    case 4:
        print("Jeudi")
    case 5:
        print("Vendredi")
    case 6 | 7:
        print("Weekend!")
    case _:
        print("Aucune idée")


nom_professeur = "David"

match nom_professeur:
    case "David":
        print("Excellent")
    case "Benoit":
        print("OK")
    case _:
        print("Sans opinion")











# if (age >= 18 and valeur_avoir_faim == True):
#     print("Merci de votre visite!")
# else:
#     print("Malheureusement, vous êtes trop jeune ou vous n'avez pas faim!")









print("fin")