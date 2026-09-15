#Auteur : Mathew Bernard
#Date: 15 septembre 2026
#Description: Exercice du cours du 15 septembre




##La structure si-sinon

#Exercice 1

nombre = int(input("Insérez un nombre entier:"))

if(nombre < 0):
    print("Nombre Négatif")
else:
    print("Nombre positif ou nul")


#Exercice 2

age = int(input("Entrez votre age:"))

if(age >= 18):
    print("Majeur")
else:
    print("Mineur")

#Exercice 3

mot_de_passe = input("Entrez un mot de passe:")

if(len(mot_de_passe) >= 8):
    print("Mot de passe accepté")
else:
    print("Mot de passe trop court")

#Exercice 4

nombre = int(input("Entrez un nombre entier"))

if(nombre % 3 == 0):
    print("Multiple de 3")
else:
    print("N'est pas un multiple de 3")

#Exercice 5

import math
a = float(input("Longueur du premier coté:"))
b = float(input("Longueur du deuxième coté:"))
c = float(input("Longueur du troisième coté:"))

if((math.isclose(a,b)) or (math.isclose(a,c)) or (math.isclose(b,c))):
    print("Triangle isocèle")
else:
    print("Triangle scalène")


##Les conditions enchaînées


#Exercice 1

nombre = int(input("Insérez un nombre entier:"))

if(nombre < 0):
    print("Négatif")
elif(nombre == 0):
    print("Nul")
elif(nombre > 0):
    print("Positif")

#Exercice 2

age = int(input("Entrez votre age:"))

if(age < 13):
    print("Enfant")
elif(age >= 13) and (age <= 17):
    print("Adolescent")
elif(age >= 18) and (age <= 65):
    print("Adulte")
else:
    print("Senior")

#Exercice 3

note= int(input("Entrez votre note"))

if(note >= 90):
    print("Excellent")
elif(note >= 75) and (note <= 89):
    print("Très bien")
elif(note >= 60) and (note <= 74):
    print("Bien")
elif(note >= 50) and (note <= 59):
    print("Passable")
elif(note < 50):
    print("Échec")
elif(note < 0) and (note > 100):
    print("Note invalide")

#Exercice 4



#Exercice 5

poids = float(input("Entrez votre poids"))
taille = float(input("Entrez votre taille"))

imc = (poids / (taille ** 2))

if(imc < 18.5):
    print("Insuffisance pondérale")
elif(18,5 <= imc < 25):
    print("Poids normal")
elif(25 <= imc < 30):
    print("Surpoids")
elif(imc >= 30):
    print("Obésité")

#Exercice 6

jour = int(input("Numéro de jour? 1 à 7:"))

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
    case 6:
        print("Samedi")
    case 7:
        print("Dimanche")
    case _:
        print("Numéro de jour invalide")