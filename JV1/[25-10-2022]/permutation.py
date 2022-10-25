import os

os.system('cls')

valeurs = [20, 10, 5, 2]

print("TABLEAU : ", valeurs)

valeurTemporaire = valeurs[1]
valeurs[1] = valeurs[2]
valeurs[2] = valeurTemporaire

print("TABLEAU MODIFIE : ", valeurs)