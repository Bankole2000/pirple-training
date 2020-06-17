class Rules:
    def __init__(self, pickTwo, pickThree, holdOn, suspension, generalMarket):
        self.pickTwo = pickTwo
        self.pickThree = pickThree
        self.holdOn = holdOn
        self.suspension = suspension
        self.generalMarket = generalMarket

    def __str__(self):
        return (f"Current game rules are:\n    Rule\t\tIs Enabled\n1. Pick Two:\t\t - {self.pickTwo}\n2. Pick Three:\t\t - {self.pickThree}\n3. Hold On:\t\t - {self.holdOn}\n4. Suspension:\t\t - {self.suspension}\n5. General Market:\t - {self.generalMarket}")


GameRules = Rules(False, False, False, False, False)
print(GameRules)
