tableau = ['a', 'b', 'c', 'd', 'e']

tableau.insert(0, tableau[tableau.__len__()-1])
tableau.pop()

print("Le nouveau tableau est : ", tableau)