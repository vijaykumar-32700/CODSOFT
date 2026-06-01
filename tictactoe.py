import random

game = [" "," "," "," "," "," "," "," "," "]

def board():
    print()
    print(game[0],"|",game[1],"|",game[2])
    print("---------")
    print(game[3],"|",game[4],"|",game[5])
    print("---------")
    print(game[6],"|",game[7],"|",game[8])
    print()

def winner(mark):

    if game[0]==game[1]==game[2]==mark:
        return True
    if game[3]==game[4]==game[5]==mark:
        return True
    if game[6]==game[7]==game[8]==mark:
        return True
    if game[0]==game[3]==game[6]==mark:
        return True
    if game[1]==game[4]==game[7]==mark:
        return True
    if game[2]==game[5]==game[8]==mark:
        return True
    if game[0]==game[4]==game[8]==mark:
        return True
    if game[2]==game[4]==game[6]==mark:
        return True

    return False

print("TIC TAC TOE")
print("You = X")
print("Computer = O")

while True:

    board()

    p = int(input("Enter position (1-9): ")) - 1

    if p>=0 and p<=8 and game[p]==" ":
        game[p]="X"
    else:
        print("Wrong position")
        continue

    if winner("X"):
        board()
        print("You won the game!")
        break

    empty = []

    for i in range(9):
        if game[i]==" ":
            empty.append(i)

    if len(empty)==0:
        board()
        print("Game Draw")
        break

    comp = random.choice(empty)
    game[comp]="O"

    if winner("O"):
        board()
        print("Computer Won!")
        break