
# Ouverture d'un fichier en lecture
with open("menu.txt", "a", encoding="utf-8") as fichier:
    for i in range(1,5):
        fichier.write(f"Valeur de i: {i}\n")

# print(contenu)