for i in range(1, 11):
    for j in range(1, i + 1):
        if(j == 1 or j == i):
            string = "* " * i
            print(string)
        else:
            string = "* " + ((i-2) * "  ") + "*"
            print(string)
    print()