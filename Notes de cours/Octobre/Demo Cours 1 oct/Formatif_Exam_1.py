#Auteur       : Mathew Bernard
#Date         : 2026-10-01
#Description  : Formatif de l'examen 1

import datetime
date_du_jour = datetime.date.today()

nom_complet = str(input("Prénom et nom de l'étudiant: "))
nom_sans_espace = nom_complet.strip()
j = 0
while j < 1:
    if nom_sans_espace == "":
        print("Le nom ne peut pas être vide. Recommencer, SVP.")
        nom_complet = str(input("Prénom et nom de l'étudiant: "))
        nom_sans_espace = nom_complet.strip()
    else:
        j += 1

position_espace = nom_complet.find(" ")
i = 0
while i < 1:
    if position_espace <=0:
        print("Entrez le prénom et le nom. Recommencer, SVP.")
        nom_complet = str(input("Prénom et nom de l'étudiant: "))
        position_espace = nom_complet.find(" ")
        nom_sans_espace = nom_complet.strip()
        e = 0
        while e < 1:
            if nom_sans_espace == "":
                print("Le nom ne peut pas être vide. Recommencer, SVP.")
                nom_complet = str(input("Prénom et nom de l'étudiant: "))
                nom_sans_espace = nom_complet.strip()
                position_espace = nom_complet.find(" ")
            else:
                e += 1
    else:
        i += 1

prenom = nom_complet[0:position_espace]
nom_famille = nom_complet[position_espace:len(nom_complet)]


note_minimale = 100
i = 1
while i <= 5:
    try:
        note = float(input(f"Note du cours {i}: "))
    except ValueError:
        print("Cette note est invalide. Recommencer, SVP.")
        note = float(input(f"Note du cours {i}: "))
    u = 0
    while u <= 1:
        if note < 0 or note > 100:
            print("La note doit être entre 0 et 100. Recommencer, SVP.")
            note = float(input(f"Note du cours {i}: "))
        else:
            u += 1
    if(note < note_minimale):
        note_minimale = note
    i += 1


note_maximale = 100
i = 1
while i <= 5:
    try:
        note = float(input(f"Note du cours {i}: "))
    except ValueError:
        print("Cette note est invalide. Recommencer, SVP.")
        note = float(input(f"Note du cours {i}: "))
    u = 0
    while u <= 1:
        if note < 0 or note > 100:
            print("La note doit être entre 0 et 100. Recommencer, SVP.")
            note = float(input(f"Note du cours {i}: "))
        else:
            u += 1
    if(note > note_minimale):
        note_maximale = note
    i += 1



print(f"{"BULLETIN DE SESSION":^50}")
print("+"*50)
print(f"| {"Date"} {":":^31}{date_du_jour} |")
print(f"| {"Étudiant"} {":":^23}{nom_famille}, {prenom} |")

