# constantes...
TAUX_TPS = 0.075


# fonctions...

####################### Fonction pour obtenir un nombre #######################

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

####################### Fonction pour afficher un menu #######################

def afficher_menu(nom, options):
    """Affiche un menu"""
    print(f"Bonjour {nom}, bienvenue dans mon programme!")
    print("-"*24)

    # for option in options:
    #     print(option)

    for i in range(len(options)):
        print(f"{i+1} - {options[i]}")
    
    print("-"*24)
    valeur_menu = obtenir_nombre(1,len(options),"votre choix")
    return valeur_menu

####################### Fonction pour un rectangle #######################

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

####################### Fonction pour un carré #######################

def afficher_carre(hauteur, motif="*"):
    largeur = hauteur
    afficher_rectangle(hauteur, largeur, motif)

####################### Fonction pour un triangle #######################

def afficher_triangle(largeur, motif="*"):
     for i in range(1, largeur + 1, 1):
          print(motif * i)
          


# programme principal...


liste_options = []
liste_options.append("Afficher un rectangle")
liste_options.append("Afficher un carré")
liste_options.append("Afficher un triangle")

# liste_options.append("Bidon")
# liste_options.remove("Bidon")

# liste_options.append("Bidon2")
# valeur = liste_options.pop() # sort la dernière valeure de la liste et met la valeur dans la variable "valeur"

# print(liste_options)
# print(liste_options.pop(0))

valeur_du_menu = afficher_menu("Benoit", liste_options)

match(valeur_du_menu):
    case 1:
            hauteur = obtenir_nombre(1,100, "hauteur")
            largeur = obtenir_nombre(1,100, "largeur")
            afficher_rectangle(largeur, hauteur)
    case 2:
            hauteur = obtenir_nombre(1,100, "hauteur")
            afficher_carre(hauteur)
    case 3:
            largeur = obtenir_nombre(1,100,"largeur")
            afficher_triangle(largeur)

# afficher_menu("Pierre", ["A...", "B...", "C...", "D...", "E..."])
# afficher_menu("Nicole")

