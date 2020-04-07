e = [str(num) for num in range(1,10)]
f=[]
print("Welcome to the tic-tac-toe game 2019 edition")
i1=input("What do you want to play as X or O(enter as upper case):")
if i1=="X":
    i2="O"
elif i1=="O":
    i2="X"
else:
    print("Please enter the correct value")
    exit()
for x in range(1,len(e)+1):
    i = int(input("What position do you want to be marked:"))-1
    if i in f:
        print("Please do not repeat values and start the game again")
        exit()
    else:
        print('\n' * 100)
        if x % 2 == 0:
            e[i] = i2
        else:
            e[i] = i1
        if (e[0]==e[1]==e[2]) \
                or (e[3]==e[4]==e[5]) or (e[6]==e[7]==e[8]) \
                or (e[0]==e[3]==e[6]) \
                or (e[1]==e[4]==e[7]) or (e[2]==e[5]==e[8]) \
                or (e[2]==e[4]==e[6]) or (e[8]==e[4]==e[0]):
            print("  |  |  ")
            print("{} |{} |{}".format(e[6], e[7], e[8]))
            print("  |  |  ")
            print("--------")
            print("  |  |  ")
            print("{} |{} |{}".format(e[3], e[4], e[5]))
            print("  |  |  ")
            print("--------")
            print("  |  |  ")
            print("{} |{} |{}".format(e[0], e[1], e[2]))
            print("  |  |  ")
            if x%2==0:
                print("Congartulations PLAYER1 WON")
                exit()
            else:
                print("Congartulations PLAYER2 WON")
                exit()
        else:
            print("  |  |  ")
            print("{} |{} |{}".format(e[6], e[7], e[8]))
            print("  |  |  ")
            print("--------")
            print("  |  |  ")
            print("{} |{} |{}".format(e[3], e[4], e[5]))
            print("  |  |  ")
            print("--------")
            print("  |  |  ")
            print("{} |{} |{}".format(e[0], e[1], e[2]))
            print("  |  |  ")
            if x==len(e):
                print("The game is a DRAW")
    f.append(i)
