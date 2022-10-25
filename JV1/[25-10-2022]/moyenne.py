import os
import random

os.system('cls')

scores = [0, 0, 0, 0]
total = 0

for index in range(0, scores.__len__()):
    scores[index] = random.randint(0, 20)
    total += scores[index]

print("TABLEAU : ", scores)

moyenne = total / scores.__len__()
print("\nMOYENNE : ", moyenne)