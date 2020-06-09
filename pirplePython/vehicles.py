"""
File: vehicles.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Homework #9
Task: Parent and Child classes
"""


class Vehicle:
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance=False, TripsSinceMaintenance=0):
        self.model = Model
        self.make = Make
        self.year = Year
        self.weight = Weight
        self.needsMaintenance = NeedsMaintenance
        self.tripsSinceMaintenance = TripsSinceMaintenance

    def getMake(self):
        return self.make

    def setMake(self, Make):
        self.make = Make

    def getModel(self):
        return self.model

    def setModel(self, Model):
        self.model = Model

    def getYear(self):
        return self.year

    def setYear(self, Year):
        self.year = Year

    def getTripsSinceMaintenance(self):
        return self.tripsSinceMaintenance

    def getNeedsMaintenance(self):
        return self.needsMaintenance

    def getWeight(self):
        return self.weight

    def setWeight(self, Weight):
        self.weight = Weight

    def Repair(self):
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0


class Cars(Vehicle):
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance=False, TripsSinceMaintenance=0, isDriving=False):
        Vehicle.__init__(self, Make, Model, Year, Weight)
        self.isDriving = isDriving

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        self.isDriving = False
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True

    def __str__(self):
        return (f"Vehicle Type: Car\nMake: {self.make}\nModel: {self.model}\nYear: {str(self.year)}\nWeight: {str(self.weight)} lbs\nIs Driving ? {str(self.isDriving)}\nTrips Since Maintenance: {str(self.tripsSinceMaintenance)}\nNeeds Maintenance ? {str(self.needsMaintenance)}")


class Planes(Vehicle):
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance=False, TripsSinceMaintenance=0, isFlying=False):
        Vehicle.__init__(self, Make, Mode, Year, Weight)
        self.isFlying = isFlying

    def fly(self):
        if self.needsMaintenance:
            print("Sorry - Cannot fly without Maintenance first")
            self.isFlying = False
            return False
        self.isFlying = True

    def land(self):
        self.isFlying = False
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True

    def __str__(self):
        return (f"Vehicle Type: Car\nMake: {self.make}\nModel: {self.model}\nYear: {str(self.year)}\nWeight: {str(self.weight)}lbs\nIs Driving ? {str(self.isFlying)}\nTrips Since Maintenance: {str(self.tripsSinceMaintenance)}\nNeeds Maintenance ? {str(self.needsMaintenance)}")


class Player:
    def __init__(self, name="YourName", cars=[], planes=[],):
        self.name = name
        self.cars = cars
        self.planes = planes

    def getCars(self):
        return self.cars

    def setCars(self, Cars):
        self.cars = Cars

    def getPlanes(self):
        return self.planes

    def setPlanes(self, Planes):
        self.planes = Planes

    def activateCar(self, car):
        self.activeCar = car

    def activatePlane(self, plane):
        self.activatePlane = plane

    def addCar(self, car):
        self.cars.append(car)

# myToyota = Cars("Toyota", "Corolla", 2006, 300, 0, False)

#
# # Vehicle goes on a 100 trips
# for i in range(101):
#     myToyota.Drive()
#     myToyota.Stop()

# print(myToyota)


def createNewCar(player):
    make = input(
        "1/4 what is the make of the Car (e.g. Toyota, Mercedes, Ford)? ")
    model = input("2/4 what is the model of the Car? ")
    year = input("3/4 What year was the car made? ")
    weight = input("4/4 What's the weight of the car (in pounds)? ")
    newCar = Cars(make, model, year, weight)
    player.addCar(newCar)
    print(f"\n===-*!! Congrats {player.name}! You added a new Car !!*-===")
    print(newCar)
    input("\nPress any key to continue...")
    mainMenu(player)


def createNewPlane(player):
    make = input(
        "1/4 What is the make of the Plane (e.g. Airbus, Boeing, Concord)? ")
    model = input("2/4 what is the model of the plane? ")
    year = input("3/4 What year was the plane made? ")
    weight = input("4/4 What's the weight of the plane (in pounds)? ")
    newplane = Planes(make, model, year, weight)
    player.addplane(newplane)
    print(f"\n===-*!! Congrats {player.name}! You added a new Plane !!*-===")
    print(newplane)
    input("Press any key to continue...")
    mainMenu(player)


def viewVehicles(player):
    print(f"====== {player.name}'s Cars ======")
    if len(player.cars) > 0:
        i = 1
        for car in player.cars:
            print(
                f"  [{i}] {car.make} {car.model}: Trips - {str(car.tripsSinceMaintenance)}. Needs Maintenance - {car.needsMaintenance}")
            i += 1
    else:
        print(f" - Sorry {player.name}, you don't have any cars right now\n")
    print(f"====== {player.name}'s Planes ======")
    if len(player.planes) > 0:
        i = 1
        for plane in player.planes:
            print(
                f"  [{i}] {plane.make} {plane.model}: Trips - {str(plane.tripsSinceMaintenance)}. Needs Maintenance - {plane.needsMaintenance}")
            i += 1
    else:
        print(f" - Sorry {player.name}, you don't have any planes right now\n")
    input("Press any key to continue...")
    mainMenu(player)


def perform(player, option):
    if option == "A":
        createNewCar(player)
    elif option == "B":
        createNewPlane(player)
    elif option == "C":
        activateCarMenu()
    elif option == "D":
        print(option)
    elif option == "E":
        print(option)
    elif option == "F":
        viewVehicles(player)
        # print(option)
    else:
        print(option)


def mainMenu(player):
    menuOptions = ["A", "B", "C", "D", "E", "F", "G"]
    while True:
        print(f"What would you like to do {player.name}?")
        print(" [A] Get a new Car")
        print(" [B] Get a new Plane")
        print(" [C] Drive")
        print(" [D] Fly")
        print(" [E] Repair vehicle")
        print(" [F] View All Vehicles")
        print(" [G] Exit")
        option = input("Please select an option (A - G): ")

        if option not in menuOptions:
            print("Sorry that option doesn't exist")
        else:
            perform(player, option)
            break


print("======== Welcome to Your New Garage =========")
playerName = input("Please enter your name: ")
player = Player(playerName)
print(f"Welcome to your New Garage {player.name}")
mainMenu(player)
