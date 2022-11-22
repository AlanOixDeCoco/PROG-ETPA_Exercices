import random

# générateur de tableau aléatoire
def GenTableau(length):
    tableau = []
    for i in range(0, length):
        tableau.append(random.randrange(1, 10))
    
    return tableau

tableau = GenTableau(10)

print("Tableau initial : ", tableau)

for iterations in range(0, tableau.__len__()):
    indexPPValeur = iterations
    ppValeur = tableau[iterations]
    for index in range(iterations, tableau.__len__()):
        if(tableau[index] < ppValeur): 
            ppValeur = tableau[index]
            indexPPValeur = index

    tableau.pop(indexPPValeur)
    tableau.insert(iterations, ppValeur)

print("Tableau trié : ", tableau)