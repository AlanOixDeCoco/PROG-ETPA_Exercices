from random import randint

print("Ca game ici ?")
input("> ")
x = randint(1, 12)
if(x % 2 == 0):
    print(str(x%2) + " | T'as gagné franchement c'est gg")
else:
    print(str(x%2) + " | T'as perdu c'est rng de fou")