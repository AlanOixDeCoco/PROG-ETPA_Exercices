tableau = ['e', 'd', 'c', 'b', 'a']

print("Tableau initial : ", tableau)

indexPPValeur = 0
ppValeur = tableau[0]
for index in range(0, tableau.__len__()):
    if(tableau[index] < ppValeur):
        ppValeur = tableau[index]
        indexPPValeur = index

tableau.pop(indexPPValeur)
tableau.insert(0, ppValeur)

print("Tableau modifié : ", tableau)