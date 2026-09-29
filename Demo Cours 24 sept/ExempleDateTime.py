import datetime

date_du_jour = datetime.date.today()
print(date_du_jour)
print(date_du_jour.year)
print(date_du_jour.month)
print(date_du_jour.day)

maintenant = datetime.datetime.now()
print(f"Date / Heure :{maintenant}")
print(f"Année : {maintenant.year}")
print(f"Mois : {maintenant.month}")
print(f"Jour : {maintenant.day}")
print(f"Heure : {maintenant.hour}")
print(f"Minute : {maintenant.minute}")
print(f"Seconde : {maintenant.second}")
print(f"Microseconde : {maintenant.microsecond}")



# %Y : année sur 4 chiffres
# %m : mois sur 2 chiffres
# %B : mois complet en lettres
# %d : jour du mois
# %H : heure (00-23)
# %M : minute
# %S : seconde
# %B : mois en toutes lettres
# %A : jour de la semaine en lettres


valeur_date = maintenant.strftime("%Y/%m/%d")
print(valeur_date)



print(maintenant.strftime("Rapport imprimé le: %Y-%m-%d"))
print(maintenant.strftime("Bilan exécuté à: %H:%M"))