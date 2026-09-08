# # print("hello!")

# # nom_du_professeur = input("Quel est le nom de ton professeur? " )
# # print(f"Le nom de mon professeur est {nom_du_professeur}")

# # age = int(input("Quel est son âge? "))
# # print(type(age))


# # age = age + 1
# # print(f"L'age + 1 de ton prof est {age}")


# ami1 = "David"
# ami2 = "Benoit"
# ami3 = "Pierre"

# # print(ami1,ami2,ami3, sep=",")

# print("a", end="")
# print("b", end="")
# print("c", end="")
# print("")


# # import math

# # VALEUR_DE_PI = math.pi
# # print(f"Valeur de Pi : {VALEUR_DE_PI:.0f}")
# # print(f"Valeur de Pi : {VALEUR_DE_PI:.1f}")
# # print(f"Valeur de Pi : {VALEUR_DE_PI:.2f}")
# # print(f"Valeur de Pi : {VALEUR_DE_PI:.3f}")
# # print(f"Valeur de Pi : {VALEUR_DE_PI:.4f}")
# # print(f"Valeur de Pi : {VALEUR_DE_PI:.5f}")
# # print(f"Valeur de Pi : {VALEUR_DE_PI:.6f}")
# # print(f"Valeur de Pi : {VALEUR_DE_PI:.7f}")
# # print(f"Valeur de Pi : {VALEUR_DE_PI:.8f}")
# # print(f"Valeur de Pi : {VALEUR_DE_PI:.9f}")


# animal1 = "Chien"
# animal2 = "Chat"
# animal3 = "Renard"
# animal4 = "Raton laveur"

# age_animal1 = 10
# age_animal2 = 11
# age_animal3 = 12
# age_animal4 = 13

# print("--------------------")
# print(f"|{animal1:>12}|{age_animal1:^5}|") #padding aligné à gauche
# print(f"|{animal2:<12}|{age_animal2:^5}|") #padding aligné à droite
# print(f"|{animal3:^12}|{age_animal3:^5}|") #padding aligné au centre
# print(f"|{animal4:^12}|{age_animal4:^5}|")
# print("--------------------")



# produits = [("Pomme", 1.25, 10), ("Banane", 0.75, 5), ("Orange", 2.50, 3)]

# print(f"{'Produit':<10} {'Prix':>10} {'Quantité':>10}")
# for nom, prix, quantite in produits:
#     print(f"{nom:<10} {prix:>10.2f} {quantite:>10}")



a = 11
b = 6

print(a / b)
print(a // b)
print(a % b)