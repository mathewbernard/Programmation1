## Auteur       :   Mathew Bernard
## Date         :   24 septembre 2026
## Description  :   Exemple important de couleurs

from colorama import Fore, Back, Style, init
init(autoreset=True)

# nom = input(f"Votre nom : {Fore.GREEN}")
# # print(end=Style.RESET_ALL)  # on remet à zéro, sinon le print suivant est aussi coloré!
# print(f"Bienvenue, {Fore.GREEN}{nom}")
# print(f"{Back.GREEN}{Fore.BLUE} Le texte que je veux")


print(f" Le verdict est : {Back.RED}URGENT")
print(f" Le verdict est : {Back.GREEN}Normal")
print(f" Le verdict est : {Back.YELLOW}À surveiller")




print(f"{Style.RESET_ALL}")
print("J'aime la pizza!")