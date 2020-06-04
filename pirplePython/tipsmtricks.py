# Trick 1 - Reversign a string
from collections import Counter
import itertools
a = "programmer"
print(f"Reverse is {a[::-1]}")

# Trick 2 - Transposing a Matrix
mat = [[1, 2, 3], [4, 5, 6]]
transmat = zip(*mat)  # [(1, 4), (2, 5), (3, 6)]
print(transmat)

# Trick 3 - Spread Operator
x, y, z = mat[0]
print(x, y, z)  # 1, 2, 3

# Trick 4 - Create a single string from all the elements in the list above
words = ["The", "Tech", "Lead", "with", "Banky"]
print(" ".join(words))

# Trick 5 - Write a Python code to print

# Trick 6 - Swap two numbers with one line of code.
a = 7
b = 5
b, a = a, b

# Trick 7 - repeat print strings without loops
print("code"*4+' '+"mentor"*5)

# Trick 8 - flatten array - Convert to a single list without using loops
a = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a)))  # [1, 2, 3, 4, 5, 6]

# Trick 9 - Checking if two words are anagrams


def is_anagram(word1, word2):
    print(Counter(word1) == Counter(word2))


is_anagram("abcd", "dcab")

# Trick 10 - Taking a string input
x = "1234"
result = map(lambda x: int(x), x.split())
print(result)
