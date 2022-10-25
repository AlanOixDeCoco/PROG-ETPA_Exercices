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

for n in range(0,len(valeurs)):
    a=valeurs[n]
    for i in range(0+n,len(valeurs)):
        if valeurs[i]<a:
            a=valeurs[n]
            valeurs[n]=valeurs[i]
            valeurs[i]=a
        
# Stop test performances
fin = datetime.now()
duree = fin - debut

# Affichage du tableau après le tri
print("\nTABLEAU TRIE : ", valeurs, "\nTEMPS D'EXECUTION : ", duree)