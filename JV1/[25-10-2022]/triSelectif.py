from datetime import datetime
import os
import random

os.system('cls')

valeurs = []

# Génération et affichage du tableau original
for index in range(0, 10000):
    valeurs.append(random.randint(0, 20))
print("TABLEAU : ", valeurs)

# Début test performances
debut = datetime.now()

# Tri du tableau
for iteration in range(0, valeurs.__len__()-1):
    plusPetiteValeur = valeurs[iteration]
    indexPPValeur = iteration
    for index in range(iteration, valeurs.__len__()):
        if(valeurs[index] < plusPetiteValeur):
            indexPPValeur = index
            plusPetiteValeur = valeurs[index]

    temp_valeurIteration = valeurs[iteration]
    valeurs[iteration] = valeurs[indexPPValeur]
    valeurs[indexPPValeur] = temp_valeurIteration

# Stop test performances
fin = datetime.now()
duree = fin - debut

# Affichage du tableau après le tri
print("\nTABLEAU TRIE : ", valeurs, "\nTEMPS D'EXECUTION : ", duree)