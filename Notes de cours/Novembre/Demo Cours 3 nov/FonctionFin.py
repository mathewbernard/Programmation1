# Docstring
def calculer_total(sous_total, rabais=0.0, pourboire=0.0):
    # Début du docstring
    """Calcule le total à payer.

    Args:
        sous_total (float): Le sous-total de la commande.
        rabais (float, optional): Le taux du rabais. Par défaut 0.0.
        pourboire (float, optional): Le pourboire, en dollars. Par défaut 0.0.

    Returns:
        float: Le total, rabais, taxes et pourboire inclus.
    """
    # Fin du docstring

    # montant = sous_total - calculer_rabais(sous_total, rabais)
    # tps, tvq = calculer_taxes(montant)
    # return round(montant + tps + tvq + pourboire, 2)



# constante
NOM_PROFESSEUR = "DAVID"

# fonction
def afficher_message(message):
    print(f"Message : {message}")

def main():
    afficher_message("Bonjour!")

# programme principal
try:
    main()
except:
    print("Une erreur fatale s'est produite")