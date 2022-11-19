tableau = [1, 2, 3, -2, 6]

indexPPValeur = 0
ppValeur = tableau[0]
for index in range(0, tableau.__len__()):
    if(tableau[index] < ppValeur):
        ppValeur = tableau[index]
        indexPPValeur = index
    
print("Le plus petit élément du tableau : ", tableau, " est : [", indexPPValeur, ": ", ppValeur, "]")