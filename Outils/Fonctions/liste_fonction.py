# Auteur      : Mathew Bernard
# Date        : 3 Novembre 2026
# Description : Liste de fonctions


#------------------------------------------------------------------------
# Afficher un carré ou un rectangle
#------------------------------------------------------------------------

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

#------------------------------------------------------------------------
# Calculer l'aire d'un carré
#------------------------------------------------------------------------

def calculer_aire_carre(hauteur):
    largeur = hauteur
    aire_carre = hauteur * largeur
    return aire_carre

#------------------------------------------------------------------------
# Afficher un triangle
#------------------------------------------------------------------------

def afficher_triangle(largeur, motif="*"):
     for i in range(1, largeur + 1, 1):
          print(motif * i)

#------------------------------------------------------------------------
# Afficher un nombre 
#------------------------------------------------------------------------

## Int

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

## Float

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

#------------------------------------------------------------------------
# Afficher un menu
#------------------------------------------------------------------------

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
