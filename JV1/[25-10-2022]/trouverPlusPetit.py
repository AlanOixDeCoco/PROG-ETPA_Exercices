import os
import random

os.system('cls')

valeurs = []

# Génération et affichage du tableau original
for index in range(0, 20):
    valeurs.append(random.randint(0, 20))
print("TABLEAU : ", valeurs)

plusPetiteValeur = valeurs[0]
indexPPValeur = 0
for index in range(0, valeurs.__len__()):
    if(valeurs[index] < plusPetiteValeur):
        indexPPValeur = index
        plusPetiteValeur = valeurs[index]

print("PLUS PETITE VALEUR : ", plusPetiteValeur, ", A L'INDEX : ", indexPPValeur)