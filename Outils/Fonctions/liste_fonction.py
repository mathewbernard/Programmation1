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

#------------------------------------------------------------------------
# Lire un entier
#------------------------------------------------------------------------

def lire_entier(message, minimum=0, maximum=99):
    """Demande un nombre entier jusqu'à ce que la saisie soit valide.

    Args:
        message (str): Le message affiché à l'utilisateur.
        minimum (int, optional): La plus petite valeur acceptée. Par défaut 0.
        maximum (int, optional): La plus grande valeur acceptée. Par défaut 99.

    Returns:
        int: L'entier saisi, compris entre minimum et maximum.
    """
    valide = False
    while not valide:
        try:
            valeur = int(input(message))
            if minimum <= valeur <= maximum:
                valide = True
            else:
                print(f"Erreur : entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            print("Erreur : ce n'est pas un nombre entier.")
    return valeur

#------------------------------------------------------------------------
# Lire oui ou non
#------------------------------------------------------------------------

def lire_oui_non(message):
    """Pose une question fermée jusqu'à obtenir « o » ou « n ».

    Args:
        message (str): La question affichée à l'utilisateur.

    Returns:
        bool: True si l'utilisateur répond « o », False s'il répond « n ».
    """
    reponses_valides = ("o", "n")
    reponse = input(message).strip().lower()
    while reponse not in reponses_valides:
        print("Erreur : répondez par o ou n.")
        reponse = input(message).strip().lower()
    return reponse == "o"