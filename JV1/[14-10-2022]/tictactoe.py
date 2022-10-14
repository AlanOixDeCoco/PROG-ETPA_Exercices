import os

_grid = "1  2  3\n4  5  6\n7  8  9"
_finished = False
_player = 1

os.system('cls') # clears console
print(_grid)

while(not _finished):
    print("\nJoueur " + str(_player) + ", ou veux-tu placer ta marque ?")
    choice = input("\n[Joueur " + str(_player) + "] > ")

    playerMark = ""
    if(_player == 1):
        playerMark = "◼"
    else:
        playerMark = "O"
    
    if(choice == '1'):
        _grid = _grid.replace("1", playerMark)
    elif(choice == '2'):
        _grid = _grid.replace("2", playerMark)
    elif(choice == '3'):
        _grid = _grid.replace("3", playerMark)
    elif(choice == '4'):
        _grid = _grid.replace("4", playerMark)
    elif(choice == '5'):
        _grid = _grid.replace("5", playerMark)
    elif(choice == '6'):
        _grid = _grid.replace("6", playerMark)
    elif(choice == '7'):
        _grid = _grid.replace("7", playerMark)
    elif(choice == '8'):
        _grid = _grid.replace("8", playerMark)
    elif(choice == '9'):
        _grid = _grid.replace("9", playerMark)

    os.system('cls') # clears console
    print(_grid)

    check = input("\nC'est fini ? [O/N]").upper()
    if(check == 'O'):
        _finished = True
    else:
        if(_player == 1):
            _player = 2
        else:
            _player = 1

print("\nGG au joueur " + str(_player) + " !")