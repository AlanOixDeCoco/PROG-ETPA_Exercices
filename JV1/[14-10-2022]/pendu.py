import os

_word = ""
_found = False
_hint = ""
_remainingTries = 10
_letters = ""
_wrongLetters = ""

_word = input("Donnes moi un mot à faire deviner !\n> ").upper()
_hint = "_" * _word.__len__()
print("Waa bah ff hein bon chance à l'autre..") 
input("\nContinuer ?")

while(not _found):
    os.system('cls') # clears console

    print(_hint)

    print("\nMauvaises lettres : " + _wrongLetters)
    print("Essais restants : " + str(_remainingTries))

    guess = input("\nUne lettre, un mot ?\n> ").upper()
    if((guess.__len__() > 1) or (_word.__len__() == guess.__len__())):
        if(guess == _word):
            print("\n[!!] Bah gg c'est ça [!!]")
            _found = True
        else:
            print("\nT'es à chier c'est pas ça")
            _remainingTries -= 1
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
            _remainingTries -= 1
            _wrongLetters += (guess + " ")
    
    if(not _found):
        if(_remainingTries == 0):
            print("\n[!!] T'as perdu (tema le nullos) [!!]")
            _found = True
        else:
            input("\nContinuer ? ")
    
    if(_found):
        print("\nLe mot était : " + _word)