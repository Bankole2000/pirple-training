"""
File: board.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Homework #6
Task: Create tictactoe board of variable size with limit
"""

noOfRows = 4  # set number of rows
noOfColumns = 5  # set number of columns
maxRowSize = 7  # set maximum no of row
maxColSize = 30  # set maximum no of columns


def makeBoard(rows, columns):
    if rows > maxRowSize or columns > maxColSize:
        print(f"Specified no of rows or column is too large")
        print(
            f"Maximum Board Size: {maxRowSize} X {maxColSize} (Rows X Columns)")
        print(f"Requested Board Size : {rows} X {columns}")
    else:
        for row in range(rows * 2 - 1):
            if row % 2 == 0:
                for column in range(1, (columns*2)):
                    if column % 2 == 1:
                        if column != (columns * 2) - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-"*(columns*2-1))
        print(f"Board Size : {rows} X {columns} (Rows X Colmns)")
        return True


makeBoard(noOfRows, noOfColumns)
