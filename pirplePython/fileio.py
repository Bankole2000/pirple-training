# How to open files
# open("filename", "options") options -> "r", "w", "a", "r+"
# File = open("filename", 'w')

# File.close()  # Always Close files

VacationSpots = ["London", "Paris", "New York", "Utah", "Iceland"]

# Will create the file if it doesn't exist
# Will overwrite if it exists
VacationFile = open("VacationPlaces", "w")

for spots in VacationSpots:
    VacationFile.write(" \""+str(spots)+"\"\n")
    # print(spots, " added to file")  # Must be a string

print("done")

VacationFile.close()

VacationFile = open("VacationPlaces", "r")

# Read a single line in the file
firstLine = VacationFile.readline()
print(firstLine)
secondLine = VacationFile.readline()
print(secondLine)
# # Read the file line by line
for line in VacationFile:
    print(line, end="")


# Reading the whole file
# TheWholeFile = VacationFile.read()

# print(TheWholeFile)

VacationFile.close()

finalSpot = " \"Thailand\"\n"

# open the file in append mode
VacationFile = open("VacationPlaces", "a")
VacationFile.write(finalSpot)

VacationFile.close()

# VacationFile = open("VacationPlaces", "r")
# for line in VacationFile:
#     print(line, end="")

# # Using the with keyword, the file is automatically closed after the code block
# with open("VacationPlaces", "r") as VacationFile:
#     for line in VacationFile:
#         print(line)

# Using with keyword in a loop
# This will read multiple lines in a loop
# for i in range(5):
#     with open("VacationPlaces"+str(i), "r") as VacationFile:
#         for line in VacationFile:
#             print(line)
