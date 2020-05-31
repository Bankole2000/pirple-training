"""
File: lists.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Homework #4
Task: function to add unique values to a list
"""
import time

myUniqueList = []
myLeftOvers = []


def addToList(arg):
    if arg not in myUniqueList:
        myUniqueList.append(arg)
        print(f"\n{arg} added to myUniqueList")
        print(f"myUniqueList is now {myUniqueList}")
        print(f"myLeftOvers is : {myLeftOvers}")
        return True
    else:
        addToLeftOvers(arg)
        return False


def addToLeftOvers(arg):
    myLeftOvers.append(arg)
    print(f"\n{arg} is already in 'myUniqueList'")
    print(f"so {arg} will be added to 'myLeftOvers' instead")
    print(f"myUniqueList is : {myUniqueList}")
    print(f"myLeftOvers is now : {myLeftOvers}")


def tryAddingToList(arg):
    print(f"\nLet's try adding {arg} to myUniqueList")
    time.sleep(4)  # pause for 4 seconds
    addToList(arg)


testCases = [24, 32, 32, 65, "John", "Mary",
             "John", 65, "Mike", 24, 79, "Mike", 32]

for i in testCases:
    tryAddingToList(i)
