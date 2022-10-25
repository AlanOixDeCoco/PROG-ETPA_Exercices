from datetime import datetime
import os
import random

os.system('cls')

valeurs = []

for index in range(0, 10000):
    valeurs.append(random.randint(0, 20))

print("TABLEAU : ", valeurs)

# Début test performances
debut = datetime.now()

sorted = False
while(not sorted):
    sorted = True
    for index in range(0, valeurs.__len__() - 1):
        if(valeurs[index] > valeurs[index+1]):
            valeurTemp = valeurs[index]
            valeurs[index] = valeurs[index+1]
            valeurs[index+1] = valeurTemp
            sorted = False

# Stop test performances
fin = datetime.now()
duree = fin - debut

# Affichage du tableau après le tri
print("\nTABLEAU TRIE : ", valeurs, "\nTEMPS D'EXECUTION : ", duree)