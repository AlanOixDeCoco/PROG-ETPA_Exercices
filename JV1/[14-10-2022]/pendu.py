import os
from tabnanny import check

_word = ""
_found = False
_hint = ""
_nbErrors = 0
_letters = ""
_wrongLetters = ""

_word = input("Donnes moi un mot à faire deviner !\n> ").upper()
_hint = "_" * _word.__len__()
print("Waa bah ff hein bon chance à l'autre..")
input("\nContinuer ?")

while(not _found):
    os.system('cls') # clear console

    print(_hint)

    print("\nMauvaises lettres : " + _wrongLetters)
    print("Erreurs : " + str(_nbErrors))

    guess = input("\nUne lettre, un mot ?\n> ").upper()
    if((guess.__len__() > 1) or (_word.__len__() == guess.__len__())):
        if(guess == _word):
            print("\n[!!] Bah gg c'est ça [!!]")
            _found = True
        else:
            print("\nT'es à chier c'est pas ça")
            _nbErrors += 1
    else:
        if(_word.find(guess) != -1):
            print("\nBien vu !")
            _letters += guess + " "
            
            _hint = ""
            for i in range(0, _word.__len__()):
                checked = False
                for j in range(0, _letters.__len__()):
                    if((_word[i] == _letters[j]) and (checked == False)):
                        _hint += _word[i]
                        checked = True
                if(checked == False):
                    _hint += "_"
        else:
            print("\nnop")
            _nbErrors += 1
            _wrongLetters += (guess + " ")
    input("\nContinuer ? ")