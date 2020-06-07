def drawField(field):
    for row in range(5):
        if row % 2 == 0:
            pracitcalRow = int(row/2)
            for column in range(5):
                if column % 2 == 0:
                    practicalColumn = int(column/2)
                    if column != 4:
                        print(field[practicalColumn][pracitcalRow], end="")
                        # print(" ", end="")
                    else:
                        print(field[practicalColumn][pracitcalRow])
                        # print(" ")
                else:
                    print("|", end="")
        else:
            print("-----")


player = 1
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# print(currentField)
drawField(currentField)
while(True):
    print("Players turn: ", player)
    MoveRow = int(input("Enter the row:\n"))
    MoveColumn = int(input("Enter the column:\n"))
    if player == 1:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "X"
            player = 2
        else:
            print("Sorry, can't move there - Please try again")
    else:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "O"
            player = 1
        else:
            print("sorry, can't move there - Please try again")
    drawField(currentField)
    print(currentField)
drawField()
