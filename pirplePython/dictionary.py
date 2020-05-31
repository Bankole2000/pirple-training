"""
Name: dictionary.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Homework #7
Task: Dictionaries and Sets
      from Homework #1 (main.py)
"""
FavoriteSong = {
    "Song Title": "I'm with You",
    "Artist Name": "Avril Lavigne",
    "Genre": "Rock",
    "Duration In Seconds": 300,
    "Album Name": "Let go",
    "Track Number": 4,
    "Country": "USA",
    "Record Label": "Sony Music",
    "Year Released": "2004",
    "Mp3 File Size in MB": 9.09,
    "Mp3 File Size in KB": 9.09 * 1024,
    "Available in Stores": True,
}
correctAnswers = []

# while(True):
print("========== Favorite Song game ==========")
print(" Guess the Details of my favorite song")
for i in FavoriteSong:
    userAnswer = input(f"What's the {i} of the song:\n")
    # print(i, FavoriteSong[i])
    print(userAnswer)

# print(FavoriteSong)


def checkAnswer(key, value):
    print(key, value)
