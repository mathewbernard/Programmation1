

# ligne1 = [1,2,3,4]
# ligne2 = [5,6,7,8]
# ligne3 = [9,10,11,12]

# liste_valeurs = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# print(liste_valeurs[2])
# print(liste_valeurs[2][2])


# for liste1 in liste_valeurs:
#     for item in liste1:
#         print(item)


# liste_avions = ["A", "B", "C", "D"]
# liste_marques_avions = ["Boeing", "Airbus", "Airbus", "Bombardier"]

# index_de_mon_avion = liste_avions.index("C")
# print(liste_avions.index("C"))

# marque_de_mon_avion = liste_marques_avions[index_de_mon_avion]
# print(f"La marque de mon avion est: {marque_de_mon_avion}")

# for i in range(len(liste_valeurs)):
#     for j in range(len(liste_valeurs[i])):
#         print(liste_valeurs[i][j])


liste_chats = ["Minou", "Grisou", "Poupou", "Garfield"]
liste_chatons = [["bebe1", "bebe2", "bebe3"], ["bebe4", "bebe5", "ronron"], ["ponpon"], []]

for i in range(len(liste_chats)):
    chat_actuel = liste_chats[i]
    print(f"Chat: {chat_actuel}")

    for j in range(len(liste_chatons[i])):
        chaton_actuel = liste_chatons[i][j]
        print(f" Chaton: {chaton_actuel}")

print("fin")
