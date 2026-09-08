# age1 = 20
# age2 = 20



# print(not (age1 != age2))



# # plus_petit = age1 < age2
# # plus_grand = age1 > age2

# # plus_petit_ou_egal = (age1 <= age2)
# # plus_grand_ou_egal = (age1 >= age2)

# # different_de = (age1 != age2)



# # age_similaire = (age1 == age2)
# # print(age_similaire)


# import math


# variable_flottante = 0.1 + 0.2
# variable_flottante2 = 0.3


# ### pour une variable flottante... C'EST MAL
# print(variable_flottante2 == variable_flottante)

# ###pour une variable flottante... C'EST MIEUX
# print(math.isclose(variable_flottante, variable_flottante2))

# # valeur = (variable_flottante2 == variable_flottante) and (a < b) and (a > c)


avoir_faim = True
age_du_client = 2
genre_client = "fémini"

client_possible = ((avoir_faim == True) or ((age_du_client >= 18) and (genre_client == "féminin")))
print(f"Client possible? : {client_possible}")