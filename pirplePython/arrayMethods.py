myList = ['Apple', 'Banana', 'Cherry']
myString = 'Hello World'
print(myList)
myList.append('Orange')  # add to the end of the list
print(myList)
myOtherList = ['Strawberry', 'Pineapple', 'Pawpaw']
myList.append(myOtherList)  # You can append one list to another
print(myList)
# List.clear() - removes all the elements from a list
# List.copy() - method returns a copy of the specified list
# copiedList = List.copy()
# List.count('arg') - returns the number of times 'arg' occurs in list
myList.extend(myOtherList)  # append elements one by one - flat map
myList.extend(myString)  # adds each letter because strings are iterateable
print(myList.index('Apple'))  # returns index of apple - 0
# Adds the 2nd arg to the at the index of the first argument
myList.insert(1, 'Lemon')
myList.pop()  # removes the last element
# myList.pop(arg) removes the element at index 'arg'
myList.remove('Lemon')  # removes the first occurence of the element in arg
myList.reverse()  # reverse the order of the list
# myList.sort()  # sort list elements
# myList.sort(reverse=True|False, key=myFunc) # myFunc will return the length of the element, thus sorting the list by element length
#   def myFunc(e):
#       return len(e)
# we can also sort a list of dictionaries
#   def myFunc(e):
#       return e['key']
print(myList)

"""
ON TUPLES
"""
# A tuple is a collection which is ordered and UNCHANGEABLE. They are written in ()
myTuple = ("apple", "banana", 'cherry')
suites = (u'\u2660', u'\u2665', u'\u2666', u'\u2663')
opensuites = (u'\u2664', u'\u2661', u'\u2662', u'\u2667')
print(myTuple)
print(suites)
print(opensuites)
# myTuple[-1]  returns last element of tuple
# myTuple[2:5] returns 3rd, 4th and 5th element

# # Turn Tuple into list and edit then return to Tuple
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# Add tuples together
myOtherTuple = ("pineapples", "strawberry", "peaches")
print(myTuple + myOtherTuple)  # flat map
# Tuples can do tuple.count() and tuple.index()

"""
lamda functions
"""
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))  returns 22
# print(mytripler(11))  returns 33


def x(a, b, c): return a + b + c


print(x(5, 6, 2))
myStringList = myString.split(" ")
print(myString)
print(myStringList)  # return list after splitting at space
myNewString = " ".join(myStringList)
print(myNewString)
newestList = [tuple(myStringList)]
print(dict(newestList))
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
print(thisdict['brand'])
# print(myList[:3])
# myList.remove(myList[])
print(myList[len(myList)-5:len(myList)])
print(myList)
