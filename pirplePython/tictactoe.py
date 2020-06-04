def drawField():
    for row in range(5):
        if row % 2 == 0:
            for column in range(5):
                if column % 2 == 0:
                    if column != 4:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            print("-----")


player = 1
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print(currentField)
while(True):
    print("Players turn: ", player)
    MoveRow = int(input("Enter the row:\n"))
    MoveColumn = int(input("Enter the column:\n"))
    if player == 1:
        currentField[MoveColumn][MoveRow] = "X"
        player = 2
    else:
        currentField[MoveColumn][MoveRow] = "O"
        player = 1
    print(currentField)
drawField()
