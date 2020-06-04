# # num = 1


# # def func():
# #     num = 4
# #     print(num)


# # func()
# # # print(num)
# # Scores = [70, 85, 67.5, 90, 80]
# # print(Scores)
# # Scores.append(100)  # add to a list
# # print(Scores)
# # li = [1, 2, 3, 4, 3, 2, 1]
# # print(li[3:4])
# # len(array) => returns the no of elements in a list
# # li = [['john', 'doe']]
# # print(li[-1][-1])
# # print(len(li[0]))

# print('Hello world')

# myList1 = [1, 2, 3]
# myList2 = [1, 2, 3]
# myList3 = ['1', '2', '3']

# print(myList1 == myList2)
# print(myList1 != myList2)
# print(myList1[0] == myList2[0]
#       and myList1[1] == myList2[1]
#       and myList1[2] == myList2[2])
# print(myList1[0] == myList3[0])
# # What's the output?

# # range(starting, stopping, steps)
# for num in range(10):
#     print(num)  # does not include 10 / last value

# while (condition):
#     Action
#     conditionChange?

# counter = 1
# Sum = 0
# while(counter <= 100):
#     print(counter)
#     Sum = Sum + counter
#     counter += 1

# while (index < len(letters)):
#     print(Index)
#     print(Letters[Index])
#     Index += 1

# height = 5000
# velocity = 49
# time = 0
# while (height > 0):
#     height = height - velocity
#     time += 1

# Get position in Breaking and continuing
# Participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]
# position = 1

# for name in Participants:
#     print(f"Iteration: {position}")
#     if name == "Tina":
#         print('Breaking')
#         break
#     print("incrementing")
#     position += 1
# print(position)

# Index = 0
# for currentIndex in range(len(Participants)):
#     if Participants[currentIndex] == "Joe":
#         break

# for number in range(10):
#     if number % 3 == 0:
#         print(f"{number} Divisible by 3")
#         continue  # skip the rest of the loop to the next iteration
#     print(f"{number} Not divisible by 3")

# for num in range(2.0):
#     print(num)

# counter = 1
# while(counter <= 10):
#     print(counter)
#     counter = counter + 1

# x = "abcd"
# for i in range(len(x)):
#     print(i)


# for row in range(5):
#     if row % 2 == 0:
#         for column in range(1, 6):
#             if column % 2 == 1:
#                 if column != 5:
#                     print(" ", end="")
#                 else:
#                     print(" ")
#             else:
#                 print("|", end="")
#     else:
#         print("-----")

# for pos in range(1, 3):
#     print("c"*pos)

# length = 3
# ToPrint = "a"
# for pos in range(1, length + 1):
#     print(ToPrint*pos)

# for pos in range(length, 0, -1):
#     print(ToPrint*pos)

# x = 2
# for i in range(x):
#     for j in range(x):
#         a = x - j + i
#         print(a)

# f = 1
# A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
# for i in range(0, 3):
#     f = f*i
#     for j in range(0, 3):
#         A[i][j] = f
# print(A)

# Sets contain unique values (repeating values eliminate repeats leaving only 1)
# countryList = []
# for i in range(5):
#     Country = input("please enter your country: ")
#     countryList.append(Country)

# countrySet = set(countryList)

# print(countryList)
# print(countrySet)

# Dictionary = Key value pairs

# countryDictionary = {}
# for Country in countryList:
#     if Country in countryDictionary:
#         countryDictionary[Country] += 1
#     else:
#         countryDictionary[Country] = 1

# print(countryDictionary)


# Simple Black shows inventory
# BlackShoes = {42: 2, 41: 3, 40: 3, 40: 4, 39: 1, 38: 0}
# while(True):
#     purchaseSize = int(input("Which shoe size would you like to buy?:\n "))
#     if purchaseSize < 0:
#         break
#     if purchaseSize in BlackShoes:
#         if BlackShoes[purchaseSize] > 0:
#             BlackShoes[purchaseSize] -= 1
#             print(f"Thanks for purchasing a size {purchaseSize} shoe")
#             print(BlackShoes)
#         else:
#             print("Sorry that shoe size is out of stock")
#             print("Shoe sizes in stock are: ")
#             print(BlackShoes)

#     else:
#         print("sorry that shoe size isn't available")
#         print("Shoe sizes available are: ")
#         print(BlackShoes)

# print("Thanks for shopping :)")

# nums = set([7, 7, 1, 3, 4, 5, 5, 2])
# print(len(nums))

# dict = {}
# dict[1] = 2
# dict['1'] = 4
# dict[1] += 2
# count = 0

# for key in dict:
#     count += dict[key]

# print(count)

# s = {1, 2, 3, [4, 5]} Produces an error

# s = {"1", "2", "3", "4", "5"}

# if "3" in s:
#     print("3")

# for i in range(10):
#     print(i)

# f = open("VacationPlaces")
# f.readlines()

string = "a"
print(string.upper())
