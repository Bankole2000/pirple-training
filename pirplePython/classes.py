# creating a class
class Team:
    def __init__(self, Name="Name", Origin="Origin"):
        self.TeamName = Name
        self.TeamOrigin = Origin

    def defineTeamName(self, Name):
        self.TeamName = Name

    def defineTeamOrigin(self, Origin):
        self.TeamOrigin = Origin


# creating a subclass inheriting from main class
class Player(Team):
    def __init__(self, PlayerName, PPoints, TeamName, TeamOrigin):
        Team.__init__(self, TeamName, TeamOrigin)
        self.PlayerName = PlayerName
        self.PlayerPoints = PPoints

    def ScoredPoint(self):
        self.PlayerPoints += 1

    def setName(self, Name):
        self.PlayerName = Name

    def __str__(self):
        return self.PlayerName + " has scored: " + str(self.PlayerPoints) + " Points"


Player1 = Player("Brad", 0, "Sharks", "Chicago")
print(Player1.PlayerName)
print(Player1.PlayerPoints)
print(Player1.TeamName)
print(Player1.TeamOrigin)
Player1.ScoredPoint()
print(Player1.PlayerPoints)
Player1.setName("Chad")
print(Player1.PlayerName)
print(Player1)
