from os import system
import os
import random

_sujets = ["Nayle", "Achille", "Louis", "Sam", "Rapido des Ratz"]
_verbes = ["mange", "foudroie", "accompagne", "réconforte", "atomise", "jute dans"]
_complements = ["une trace de fond de chiottes", "une 86 chaude", "Liam en gaber à Amsterdam"]

phrase = ""
phrase += (_sujets[random.randint(0, _sujets.__len__() - 1)] + " ")
phrase += (_verbes[random.randint(0, _verbes.__len__() - 1)] + " ")
phrase += (_complements[random.randint(0, _complements.__len__() - 1)] + " ")



keepGoing = True
while(keepGoing):
    os.system('cls')
    print("Ca dit quoi ?")
    input(" > Ca dit FEUR < ")
    print("Sinon ça dit :")
    phrase = ""
    phrase += (_sujets[random.randint(0, _sujets.__len__() - 1)] + " ")
    phrase += (_verbes[random.randint(0, _verbes.__len__() - 1)] + " ")
    phrase += (_complements[random.randint(0, _complements.__len__() - 1)] + " ")
    print(phrase)
    input()