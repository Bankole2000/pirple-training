"""
Name: dictionary.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Homework #7
Task: Dictionaries and Sets
      from Homework #1 (main.py)
"""
FavoriteSong = {
    "Song Title": "I'm with you",
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
    "Availability in Stores": True,
}
correctAnswers = []


def checkAnswer(key, value):
    if type(FavoriteSong[key]) is int:
        try:
            value = int(value)
        except ValueError:
            print("You didn't enter a valid Value\n")
            return False
        else:
            value = int(value)
    elif type(FavoriteSong[key]) is bool:
        value = bool(value) if (value == True) or (value == False) else "False"
    elif type(FavoriteSong[key]) is float:
        try:
            value = float(value)
        except ValueError:
            print("You didn't enter a valid Value\n")
            return False
        else:
            value = float(value)
    if value == FavoriteSong[key]:
        print("== !!! That issss CORRECT !!! ==\n")
        return True
    else:
        print("== XX Sorry! WRONG Answer XX ==\n")
        return False


print("\n  ========== Favorite Song game ==========")
print("   Guess the Details of my favorite song")
print("   type 'exit' to leave the game at anytime\n")

for i in FavoriteSong:
    userAnswer = input(
        f"What's the '{i}' of the song:\n")
    if userAnswer == 'exit':
        break
    if checkAnswer(i, userAnswer):
        correctAnswers.append(userAnswer)

print(f"Your Final Score is: {len(correctAnswers)}/{len(FavoriteSong)}")

if len(correctAnswers) == len(FavoriteSong):
    print("Wow! You know me pretty well :)")

viewAll = input("\nWant to see all the answers? (y/n) \n")

if viewAll == "y" or viewAll == "Y":
    print("==== The Answers ====")
    for i in FavoriteSong:
        print(f"{i}: {FavoriteSong[i]}")
else:
    print("Thanks for Playing :)")
