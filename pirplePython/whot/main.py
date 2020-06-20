# PROJECT: FILE: main.py FOLDER: Whot
"""
File: main.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Final Project
Task: WHOT Card game with customizable options
"""
# SECTION: Game Imports
from os import system, name, path
import sys
from random import shuffle, choice
from colorama import init, Fore, Back, Style
from time import sleep
init()

# SECTION: Game Constants
redSuite = (u'\u2665',  u'\u2666')
blackSuite = (u'\u2660',  u'\u2663')
suites = (u'\u2660', u'\u2665', u'\u2666', u'\u2663')
joker = (u'\u2605',)
noOfJokers = 5
numbers = [2, 3, 4, 5, 6, 7, 8, 9]
letters = ["A", "J", "Q", "K"]
specials = ["K", "A", "2", "5", "8"]
cardDict = {'A': 'hold on', '2': 'pick two', '5': 'pick three',
            '8': 'suspension', 'K': 'general market'}
noOfStartingCards = 2
deck = []


########## Game Functions #########
# Clear Secreen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Show Card Icons only
def displaySuites(reverse=False):
    if not reverse:
        print(" " + Fore.RESET + u'\u2660' + " " + Fore.RED + u'\u2666' + " " + Fore.RESET +
              u'\u2663' + " " + Fore.RED + u'\u2665' + " " + Fore.RESET, end="")
    else:
        print(" " + Fore.RED + u'\u2665' + " " + Fore.RESET + u'\u2663' + " " + Fore.RED +
              u'\u2666' + " " + Fore.RESET + u'\u2660' + " " + Fore.RESET, end="")


def displaySingleSuite(number):
    if int(number) == 1:
        print(Fore.RESET + u'\u2660' + Fore.RESET, end="")
    elif int(number) == 2:
        print(Fore.RED + u'\u2666' + " " + Fore.RESET, end="")
    elif int(number) == 3:
        print(Fore.RESET + u'\u2663' + Fore.RESET, end="")
    elif int(number) == 4:
        print(Fore.RED + u'\u2665' + " " + Fore.RESET, end="")


# Display a single card decorated
def displaySingleCard(card, end=""):
    cardParts = card.split(" ")
    if cardParts[1] in redSuite:
        print(Back.WHITE + Fore.RED + " " + card +
              " " + Fore.RESET + Back.RESET, end=end)
    elif cardParts[1] in blackSuite:
        print(Back.WHITE + Fore.BLACK + " " + card +
              " " + Fore.RESET + Back.RESET, end=end)
    else:
        print(Back.WHITE + Fore.BLUE + " " + card +
              " " + Fore.RESET + Back.RESET, end=end)


# Display Cards
def displayCards(cards):
    for card in cards:
        cardParts = card.split(" ")
        if cardParts[1] in redSuite:
            print(Back.WHITE + Fore.YELLOW + " : " + Fore.RED +
                  cardParts[0], cardParts[1] + Back.WHITE, end="")
        elif cardParts[1] in blackSuite:
            print(Back.WHITE + Fore.YELLOW + " : " + Fore.BLACK +
                  cardParts[0], cardParts[1] + Back.WHITE, end="")
        elif cardParts[1] in joker:
            print(Back.WHITE + Fore.YELLOW + " : " + Fore.BLUE +
                  cardParts[0], cardParts[1] + Back.WHITE, end="")
    print(Fore.YELLOW + " : " + Back.RESET + Fore.RESET, end="")


# Make Deck
def makeDeck(deck, suites, letters, numbers, noOfJokers):
    for suite in suites:
        for number in numbers:
            card = str(number) + " " + suite
            deck.append(card)
        for letter in letters:
            card = letter + " " + suite
            deck.append(card)
    for i in range(noOfJokers):
        jokerCard = "W"+str(i+1)+" "+u'\u2605'
        deck.append(jokerCard)
    return deck


# Title Formatter
def showTitle(title):
    print("\n====****", end="")
    displaySuites()
    print(f"{title.upper()}", end="")
    displaySuites(True)
    print("****====")


def displayGame(game, player, computer):
    print("\n" + Back.RESET + Fore.CYAN + computer.name +
          Fore.RESET + "'s Cards ", u'\u27a4', " " + Fore.RESET + Back.RESET, end="")
    displayCards(computer.cards)
    print('\n', end="")
    print("\n" + Fore.MAGENTA + "Game Card ", u'\u27a4', " ", end="")
    displayCards(game.deck)
    print("\t\tMarket ", u'\u27a4',
          " (", str(len(game.market)), ")[", end="")
    displaySuites()
    print("]\n\n" + Back.RESET + Fore.CYAN + player.name +
          Back.RESET + Fore.RESET + "'s Cards ", u'\u27a4', " ", end="")
    displayCards(player.cards)
    print('\n', end="")


def showyDeckDisplay(deck):
    clear()
    for j in range(len(deck)):
        displaySingleCard(deck[j])
        sleep(0.01)
    print("\n")
    for i in range(4):
        displaySuites()
        sleep(0.01)
        displaySuites(True)
        sleep(0.01)
        displaySuites(True)
        sleep(0.01)
        displaySuites()
        sleep(0.01)
    print("\n")
    print("Let's Play WHOT")
    sleep(2)


def showHelp():
    clear()
    showTitle("how to play whot")
    print("- The Objective is to keep playing your cards till")
    print("they are finished. First to play all their cards wins.")
    print("However, only cards with either the " + Fore.CYAN + "same number " +
          Fore.RESET + "or the " + Fore.CYAN + "\nsame suite " + Fore.RESET + "(", end="")
    displaySuites()
    print(") as the" + Fore.MAGENTA +
          " Game Card " + Fore.RESET + "may be played.")
    showTitle('basic rules')
    print(Fore.CYAN + " [1]" + Fore.RESET +
          " You can only play cards that match the " + Fore.CYAN + "number" + Fore.RESET + " or " + Fore.CYAN + "suite" + Fore.RESET + " of the " + Fore.MAGENTA + "Game Card" + Fore.RESET)
    print(Fore.CYAN + " [2]" + Fore.RESET +
          " The only exception to Rule [1] are the " + Fore.YELLOW + " WHOT " + Fore.RESET + " Cards: ", end="")
    displaySingleCard("W1 ★", ",")
    displaySingleCard("W2 ★", ",")
    displaySingleCard("W3 ★", ",")
    displaySingleCard("W4 ★", ",")
    print("\n", end="")
    print(Fore.CYAN + " [3]" + Fore.RESET +
          " When a " + Fore.YELLOW + "WHOT" + Fore.RESET + " Card is played, the requested Suite MUST be played next.")
    print(Fore.CYAN + " [4]" + Fore.RESET +
          " If the player cannot play any of their cards, they have to go to the " + Fore.MAGENTA + "market" + Fore.RESET + ".")
    print(Fore.CYAN + " [5]" + Fore.RESET +
          " The first player to play all their cards, win, however - Rule[6].")
    print(Fore.CYAN + " [5]" + Fore.RESET + " The game CANNOT be won with a " + Fore.YELLOW + "'hold on'" + Fore.RESET +
          ", " + Fore.YELLOW + "'suspension'" + Fore.RESET + ", or " + Fore.YELLOW + "WHOT" + Fore.RESET + " card.")
    showTitle("special Cards")
    print("- These are cards that have special effects when played \ndepending on if those effects are enabled in the game options.")
    print("\t- Card -\t\t- Effect -\t\t- Description -\t")
    displaySingleCard("A ♠", ", ")
    displaySingleCard("A ♥", ", ")
    displaySingleCard("A ♣", ", ")
    displaySingleCard("A ♦", ", ")
    print("\t- Hold On\t- The player gets to play another card")
    displaySingleCard("2 ♠", ", ")
    displaySingleCard("2 ♥", ", ")
    displaySingleCard("2 ♣", ", ")
    displaySingleCard("2 ♦", ", ")
    print("\t- Pick Two\t- The opponent has to pick 2 cards (Can be deflected)")
    displaySingleCard("5 ♠", ", ")
    displaySingleCard("5 ♥", ", ")
    displaySingleCard("5 ♣", ", ")
    displaySingleCard("5 ♦", ", ")
    print("\t- Pick Three\t- The opponent has to pick 3 cards (Can be deflected)")
    displaySingleCard("8 ♠", ", ")
    displaySingleCard("8 ♥", ", ")
    displaySingleCard("8 ♣", ", ")
    displaySingleCard("8 ♦", ", ")
    print("\t- Suspension\t- The next player forfeits their turn")
    displaySingleCard("K ♠", ", ")
    displaySingleCard("K ♥", ", ")
    displaySingleCard("K ♣", ", ")
    displaySingleCard("K ♦", ", ")
    print("\t- General Mrkt\t- Every other payer picks a card (Cannot be deflected)")
    displaySingleCard("W1 ★", ",")
    displaySingleCard("W2 ★", ",")
    displaySingleCard("W3 ★", ",")
    displaySingleCard("W4 ★", ",")
    print("\t- WHOT\t\t- Cancels all deflectable effects, then requests a suite")
    print("Enter " + Fore.YELLOW + "'--help'" + Fore.RESET +
          " at any time during the game to view this help, and " + Fore.YELLOW + "'--rules'" + Fore.RESET + " to view rules)")
    print("Enter " + Fore.YELLOW + "'--resume'" + Fore.RESET + " to resume")
    if input("Press any key to continue ('--resume' to resume)... ").upper() == "--RESUME":
        pass
    else:
        return

    ########## Game Classes ##########
    # Player Class


class Player:
    def __init__(self, name, score=0, cards=[], hasToPick=0, isSuspended=False, hasWon=False, isTurn=False, hasPlayed=False, hasToPlay="", jokerWasLastCard=False):
        self.name = name
        self.score = score
        self.cards = cards
        self.hasWon = hasWon
        self.isTurn = isTurn
        self.hasPlayed = hasPlayed
        self.hasToPlay = hasToPlay
        self.hasToPick = hasToPick
        self.isSuspended = isSuspended
        self.jokerWasLastCard = jokerWasLastCard

    def goToMarket(self, market, opponent):
        self.cards.append(market[len(market)-1])
        market.pop()
        shuffle(market)
        print(Fore.CYAN + self.name + Fore.RESET +
              " picked a card from the market")
        self.isTurn = False
        opponent.isTurn = True

    def pickTwo(self, market):
        self.cards.extend(market[len(market)-2:len(market)])
        shuffle(market)
        market.pop()
        market.pop()
        print(Fore.CYAN + self.name + Fore.RESET +
              " picked 2 cards from the market")

    def pickThree(self, market):
        self.cards.extend(market[len(market)-3:len(market)])
        shuffle(market)
        market.pop()
        market.pop()
        market.pop()
        print(self.name, "picked 3 cards from the market")

    def canPlay(self, cardIndex, gameCard):
        cardParts = self.cards[cardIndex-1].split(" ")
        gameCardParts = gameCard[0].split(" ")
        # print(cardParts[0], gameCardParts[0])
        # print(cardParts[1], gameCardParts[1])
        if cardParts[0] == gameCardParts[0]:
            return True
        elif cardParts[1] == gameCardParts[1]:
            return True
        else:
            return False

    def canDeflect(self, key):
        for card in self.cards:
            if card.split(" ")[0] == key:
                return True
            elif card.split(" ")[1] == joker[0]:
                return True
        return False

    def deflect(self, key, opponent, gameCard, market, rules):
        for card in self.cards:
            if card.split(" ")[0] == key:
                Index = self.cards.index(card)
                self.forcePlay(Index, gameCard, opponent, market, rules)
                self.hasToPick = 0

                break
            elif card.split(" ")[1] == joker[0]:
                jokerIndex = self.cards.index(card)
                if self.name == "COMPUTER":
                    self.autoPlayJoker(opponent, jokerIndex,
                                       gameCard, market, rules)
                    self.hasToPick = 0
                    break
                else:
                    self.playJoker(opponent)
                    self.forcePlay(jokerIndex, gameCard,
                                   opponent, market, rules)
                    self.hasToPick = 0

                    return
        print(Fore.CYAN + self.name + Fore.RESET + " deflected the card")
        if len(self.cards) == 1:
            print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                  Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
        if len(self.cards) == 0:
            self.hasWon = True
        if len(opponent.cards) == 1:
            print(Fore.CYAN + opponent.name + Fore.RESET + " said - " +
                  Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
        if len(opponent.cards) == 0:
            opponent.hasWon = True

    def playJoker(self, computer):
        self.hasToPlay = ""
        print(Fore.CYAN + self.name + Fore.RESET + " played a " +
              Fore.YELLOW + "WHOT" + Fore.RESET + " Card")
        print("Which Suite do you want?", end="")
        print(" (1) ", end="")
        displaySingleSuite(1)
        print(" (2) ", end="")
        displaySingleSuite(2)
        print("(3) ", end="")
        displaySingleSuite(3)
        print(" (4) ", end="")
        displaySingleSuite(4)
        suiteChoice = input(": ")
        try:
            if int(suiteChoice) == 1:
                print(Fore.CYAN + self.name + Fore.RESET +
                      " said - I want a ", end="")
                displaySingleSuite(1)
                computer.hasToPlay = suites[0]
                self.hasToPlay = suites[0]
            elif int(suiteChoice) == 2:
                print(Fore.CYAN + self.name + Fore.RESET +
                      " said - I want a ", end="")
                displaySingleSuite(2)
                self.hasToPlay = suites[2]
                computer.hasToPlay = suites[2]

            elif int(suiteChoice) == 3:
                print(Fore.CYAN + self.name + Fore.RESET +
                      " said - I want a ", end="")
                displaySingleSuite(3)
                computer.hasToPlay = suites[3]
                self.hasToPlay = suites[3]

            elif int(suiteChoice) == 4:
                print(Fore.CYAN + self.name + Fore.RESET +
                      " said - I want a ", end="")
                displaySingleSuite(4)
                self.hasToPlay = suites[1]
                computer.hasToPlay = suites[1]
        except:
            if suiteChoice == "--help":
                showHelp()
            elif suiteChoice == "--resume":
                loadSavedGame()
        print("\n", end="")

    def autoPlayJoker(self, player, Index, gameCard, market, rules):
        gameCard.append(self.cards[Index])
        print(Fore.CYAN + self.name + Fore.RESET + " played ", end="")
        displaySingleCard(self.cards[Index], end="\n")
        if len(self.cards) == 1 and self.cards[Index].split(" ")[1] == joker[0]:
            self.jokerWasLastCard = True
            print(Fore.CYAN + self.name + Fore.RESET +
                  "'s Last Card was a WHOT so")
        self.cards.pop(Index)
        if self.jokerWasLastCard:
            self.goToMarket(market, player)
            self.jokerWasLastCard = False
        market.append(gameCard[0])
        shuffle(market)
        gameCard.pop(0)
        if len(self.cards) == 1:
            print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                  Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
        if len(self.cards) == 0:
            self.hasWon = True
        self.isTurn = False
        player.isTurn = True
        print(Fore.CYAN + self.name + Fore.RESET + " played a " + Fore.YELLOW +
              "WHOT" + Fore.RESET + " Card")
        suiteChoice = choice(suites)
        print(Fore.CYAN + self.name + Fore.RESET + " said - I want a " +
              Fore.MAGENTA + suiteChoice + Fore.RESET)
        player.hasToPlay = suiteChoice
        self.hasToPlay = suiteChoice
        return

    def playCard(self, cardIndex, gameCard, market, opponent, rules):

        cardParts = self.cards[cardIndex-1].split(" ")
        gameCardParts = gameCard[0].split(" ")
        if cardParts[0] == gameCardParts[0]:
            print(Fore.CYAN + self.name + Fore.RESET + " played ", end="")
            displaySingleCard(self.cards[cardIndex-1], end="\n")
            gameCard.append(self.cards[cardIndex-1])

            if self.cards[cardIndex-1].split(" ")[0] in cardDict.keys():
                key = self.cards[cardIndex-1].split(" ")[0]
                if specials.index(key) == 0 and rules.generalMarket:
                    print(" - That's a " + Fore.YELLOW +
                          cardDict[key] + Fore.RESET)
                    opponent.goToMarket(market, self)
                    self.cards.pop(cardIndex-1)
                    market.append(gameCard[0])
                    shuffle(market)
                    gameCard.pop(0)
                    if len(self.cards) == 1:
                        print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                              Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                    if len(self.cards) == 0:
                        self.hasWon = True
                    self.isTurn = True
                    opponent.isTurn = False
                    return

                elif specials.index(key) == 1 and rules.holdOn:
                    print(" - That's a " + Fore.YELLOW +
                          cardDict[key] + Fore.RESET)
                    self.cards.pop(cardIndex-1)
                    market.append(gameCard[0])
                    shuffle(market)
                    gameCard.pop(0)
                    if len(self.cards) == 1:
                        print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                              Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                    if len(self.cards) == 0:
                        print(Fore.CYAN + self.name + Fore.RESET + " can't win with a " +
                              Fore.YELLOW + "'hold on'" + Fore.RESET + " so")
                        self.goToMarket(market, opponent)
                        self.hasWon = False
                    self.isTurn = True
                    opponent.isTurn = False
                    return

                elif specials.index(key) == 2 and rules.pickTwo:
                    self.cards.pop(cardIndex-1)
                    market.append(gameCard[0])
                    shuffle(market)
                    gameCard.pop(0)
                    print(" - That's a " + Fore.YELLOW +
                          cardDict[key] + Fore.RESET)
                    opponent.hasToPick = 2
                    print(Fore.CYAN + opponent.name + Fore.RESET + " has to pick " +
                          Fore.MAGENTA + str(opponent.hasToPick) + Fore.RESET + " cards")
                    canDeflect = opponent.canDeflect(key)
                    if canDeflect:
                        if self.name == 'COMPUTER':
                            print(Fore.CYAN + opponent.name + Fore.RESET, end="")
                            print(" can deflect this card. Deflect?" +
                                  Fore.CYAN + " (y/n) " + Fore.RESET + ": ", end="")
                            if input().upper() == "Y":
                                opponent.deflect(
                                    key, self, gameCard, market, rules)
                                print(Fore.CYAN + opponent.name + Fore.RESET +
                                      " deflected the card")
                            else:
                                opponent.pickTwo(market)
                        else:
                            print(Fore.CYAN + opponent.name +
                                  Fore.RESET + " deflected the card")
                            opponent.deflect(
                                key, self, gameCard, market, rules)
                    else:
                        print(Fore.CYAN + opponent.name + Fore.RESET +
                              " couldn't deflect the card")
                        opponent.pickTwo(market)
                    return

                elif specials.index(key) == 3 and rules.pickThree:
                    self.cards.pop(cardIndex-1)
                    market.append(gameCard[0])
                    shuffle(market)
                    gameCard.pop(0)
                    print(" - That's a " + Fore.YELLOW +
                          cardDict[key] + Fore.RESET)
                    opponent.hasToPick = 3
                    print(Fore.CYAN + opponent.name + Fore.RESET + " has to pick " +
                          Fore.MAGENTA + str(opponent.hasToPick) + Fore.RESET + " cards")
                    canDeflect = opponent.canDeflect(key)
                    if canDeflect:
                        if self.name == 'COMPUTER':
                            print(Fore.CYAN + opponent.name + Fore.RESET, end="")
                            print(" can deflect this card. Deflect?" +
                                  Fore.CYAN + " (y/n) " + Fore.RESET + ": ", end="")
                            if input().upper() == "Y":
                                opponent.deflect(
                                    key, self, gameCard, market, rules)
                                print(Fore.CYAN + opponent.name + Fore.RESET +
                                      " deflected the card")
                            else:
                                opponent.pickThree(market)
                        else:
                            print(Fore.CYAN + opponent.name +
                                  Fore.RESET + " deflected the card")
                            opponent.deflect(
                                key, self, gameCard, market, rules)
                    else:
                        print(Fore.CYAN + opponent.name + Fore.RESET +
                              " couldn't deflect the card")
                        opponent.pickThree(market)
                    return

                elif specials.index(key) == 4 and rules.suspension:
                    print(" - That's a " + Fore.YELLOW +
                          cardDict[key] + Fore.RESET)
                    self.cards.pop(cardIndex-1)
                    market.append(gameCard[0])
                    shuffle(market)
                    gameCard.pop(0)
                    if len(self.cards) == 1:
                        print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                              Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                    if len(self.cards) == 0:
                        print(Fore.CYAN + self.name + Fore.RESET + " can't win with a " +
                              Fore.YELLOW + "'suspension'" + Fore.RESET + " so")
                        self.goToMarket(market, opponent)
                        self.hasWon = False
                    self.isTurn = True
                    opponent.isTurn = False
                    return

            self.cards.pop(cardIndex-1)
            market.append(gameCard[0])
            shuffle(market)
            gameCard.pop(0)
            if len(self.cards) == 1:
                print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                      Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
            if len(self.cards) == 0:
                self.hasWon = True
            self.isTurn = False
            opponent.isTurn = True
            return

        elif cardParts[1] == gameCardParts[1]:
            print(Fore.CYAN + self.name + Fore.RESET + " played ", end="")
            displaySingleCard(self.cards[cardIndex-1], end="\n")
            gameCard.append(self.cards[cardIndex-1])
            if self.cards[cardIndex-1].split(" ")[0] in cardDict.keys():
                key = self.cards[cardIndex-1].split(" ")[0]
                if specials.index(key) == 0 and rules.generalMarket:
                    print(" - That's a " + Fore.YELLOW +
                          cardDict[key] + Fore.RESET)
                    opponent.goToMarket(market, self)
                    self.cards.pop(cardIndex-1)
                    market.append(gameCard[0])
                    shuffle(market)
                    gameCard.pop(0)
                    if len(self.cards) == 1:
                        print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                              Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                    if len(self.cards) == 0:
                        self.hasWon = True
                    self.isTurn = True
                    opponent.isTurn = False
                    return

                elif specials.index(key) == 1 and rules.holdOn:
                    print(" - That's a " + Fore.YELLOW +
                          cardDict[key] + Fore.RESET)
                    self.cards.pop(cardIndex-1)
                    market.append(gameCard[0])
                    shuffle(market)
                    gameCard.pop(0)
                    if len(self.cards) == 1:
                        print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                              Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                    if len(self.cards) == 0:
                        print(Fore.CYAN + self.name + Fore.RESET + " can't win with a " +
                              Fore.YELLOW + "'hold on'" + Fore.RESET + " so")
                        self.goToMarket(market, opponent)
                        self.hasWon = False
                    self.isTurn = True
                    opponent.isTurn = False
                    return

                elif specials.index(key) == 2 and rules.pickTwo:
                    self.cards.pop(cardIndex-1)
                    market.append(gameCard[0])
                    shuffle(market)
                    gameCard.pop(0)
                    print(" - That's a " + Fore.YELLOW +
                          cardDict[key] + Fore.RESET)
                    opponent.hasToPick = 2
                    print(Fore.CYAN + opponent.name + Fore.RESET + " has to pick " +
                          Fore.MAGENTA + str(opponent.hasToPick) + Fore.RESET + " cards")
                    canDeflect = opponent.canDeflect(key)
                    if canDeflect:
                        if self.name == 'COMPUTER':
                            print(Fore.CYAN + opponent.name + Fore.RESET, end="")
                            print(" can deflect this card. Deflect?" +
                                  Fore.CYAN + " (y/n) " + Fore.RESET + ": ", end="")
                            if input().upper() == "Y":
                                opponent.deflect(
                                    key, self, gameCard, market, rules)
                                print(Fore.CYAN + opponent.name + Fore.RESET +
                                      " deflected the card")
                            else:
                                opponent.pickTwo(market)
                        else:
                            print(Fore.CYAN + opponent.name +
                                  Fore.RESET + " deflected the card")
                            opponent.deflect(
                                key, self, gameCard, market, rules)
                    else:
                        print(Fore.CYAN + opponent.name + Fore.RESET +
                              " couldn't deflect the card")
                        opponent.pickTwo(market)
                    return

                elif specials.index(key) == 3 and rules.pickThree:
                    self.cards.pop(cardIndex-1)
                    market.append(gameCard[0])
                    shuffle(market)
                    gameCard.pop(0)
                    print(" - That's a " + Fore.YELLOW +
                          cardDict[key] + Fore.RESET)
                    opponent.hasToPick = 3
                    print(Fore.CYAN + opponent.name + Fore.RESET + " has to pick " +
                          Fore.MAGENTA + str(opponent.hasToPick) + Fore.RESET + " cards")
                    canDeflect = opponent.canDeflect(key)
                    if canDeflect:
                        if self.name == 'COMPUTER':
                            print(Fore.CYAN + opponent.name + Fore.RESET, end="")
                            print(" can deflect this card. Deflect?" +
                                  Fore.CYAN + " (y/n) " + Fore.RESET + ": ", end="")
                            if input().upper() == "Y":
                                opponent.deflect(
                                    key, self, gameCard, market, rules)
                                print(Fore.CYAN + opponent.name + Fore.RESET +
                                      " deflected the card")
                            else:
                                opponent.pickThree(market)
                        else:
                            print(Fore.CYAN + opponent.name +
                                  Fore.RESET + " deflected the card")
                            opponent.deflect(
                                key, self, gameCard, market, rules)
                    else:
                        print(Fore.CYAN + opponent.name + Fore.RESET +
                              " couldn't deflect the card")
                        opponent.pickThree(market)
                    return

                elif specials.index(key) == 4 and rules.suspension:
                    print(" - That's a " + Fore.YELLOW +
                          cardDict[key] + Fore.RESET)
                    self.cards.pop(cardIndex-1)
                    market.append(gameCard[0])
                    shuffle(market)
                    gameCard.pop(0)
                    if len(self.cards) == 1:
                        print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                              Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                    if len(self.cards) == 0:
                        print(Fore.CYAN + self.name + Fore.RESET + " can't win with a " +
                              Fore.YELLOW + "'suspension'" + Fore.RESET + " so")
                        self.goToMarket(market, opponent)
                        self.hasWon = False
                    self.isTurn = True
                    opponent.isTurn = False
                    return

            self.cards.pop(cardIndex-1)
            market.append(gameCard[0])
            shuffle(market)
            gameCard.pop(0)
            if len(self.cards) == 1:
                print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                      Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
            if len(self.cards) == 0:
                self.hasWon = True
            self.isTurn = False
            opponent.isTurn = True
            return

    def hasJoker(self):
        for card in self.cards:
            if card.split(" ")[1] == joker[0]:
                return True
        return False

    def autoPlay(self, player, gameCard, market, rules):

        if len(self.hasToPlay) > 0:
            hasJoker = self.hasJoker()
            if hasJoker:
                for card in self.cards:
                    if card.split(" ")[1] == joker[0]:
                        jokerIndex = self.cards.index(card)
                        break
                self.autoPlayJoker(player, jokerIndex, gameCard, market, rules)
            else:
                for card in self.cards:
                    if card.split(" ")[1] == self.hasToPlay:
                        indexToPlay = self.cards.index(card)
                        self.forcePlay(indexToPlay, gameCard,
                                       player, market, rules)
                        self.hasToPlay = ""
                        player.hasToPlay = ""
                        return
                self.goToMarket(market, player)
            return
        hasJoker = self.hasJoker()
        if hasJoker:
            for card in self.cards:
                if card.split(" ")[1] == joker[0]:
                    jokerIndex = self.cards.index(card)
                    break
            self.autoPlayJoker(player, jokerIndex, gameCard, market, rules)
            return
        for card in self.cards:
            computerCanPlay = self.canPlay(self.cards.index(card), gameCard)
            if computerCanPlay == True:
                indexToPlay = int(self.cards.index(card))

                # print(indexToPlay, self.cards, indexToPlay-1)
                self.playCard(indexToPlay,
                              gameCard, market, player, rules)
                self.hasPlayed = True
                break
            else:
                continue
        if self.hasPlayed == False:
            self.goToMarket(market, player)
        else:
            self.hasPlayed = False
            return

    def forcePlay(self, Index, gameCard, computer, market, rules):
        gameCard.append(self.cards[Index])
        print(Fore.CYAN + self.name + Fore.RESET + " played ", end="")
        displaySingleCard(self.cards[Index], end="\n")
        if len(self.cards) == 1 and self.cards[Index].split(" ")[1] == joker[0]:
            self.jokerWasLastCard = True
            print(Fore.CYAN + self.name + Fore.RESET +
                  "'s Last Card was a WHOT so")
        if self.cards[Index].split(" ")[0] in cardDict.keys():
            key = self.cards[Index].split(" ")[0]
            if specials.index(key) == 0 and rules.generalMarket:
                print(" - That's a " + Fore.YELLOW +
                      cardDict[key] + Fore.RESET)
                computer.goToMarket(market, self)
                self.cards.pop(Index)
                market.append(gameCard[0])
                shuffle(market)
                gameCard.pop(0)
                if len(self.cards) == 1:
                    print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                          Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                if len(self.cards) == 0:
                    self.hasWon = True
                self.isTurn = True
                computer.isTurn = False
                return

            elif specials.index(key) == 1 and rules.holdOn:
                print(" - That's a " + Fore.YELLOW +
                      cardDict[key] + Fore.RESET)
                self.cards.pop(Index)
                market.append(gameCard[0])
                shuffle(market)
                gameCard.pop(0)
                if len(self.cards) == 1:
                    print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                          Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                if len(self.cards) == 0:
                    print(Fore.CYAN + self.name + Fore.RESET + " can't win with a " +
                          Fore.YELLOW + "'hold on'" + Fore.RESET + " so")
                    self.goToMarket(market, computer)
                    self.hasWon = False
                self.isTurn = True
                computer.isTurn = False
                return

            elif specials.index(key) == 2 and rules.pickTwo:
                self.cards.pop(Index)
                market.append(gameCard[0])
                shuffle(market)
                gameCard.pop(0)
                print(" - That's a " + Fore.YELLOW +
                      cardDict[key] + Fore.RESET)
                computer.hasToPick = 2
                print(Fore.CYAN + computer.name + Fore.RESET + " has to pick " +
                      Fore.MAGENTA + str(computer.hasToPick) + Fore.RESET + " cards")
                canDeflect = computer.canDeflect(key)
                if canDeflect:
                    if self.name == 'COMPUTER':
                        print(Fore.CYAN + computer.name + Fore.RESET, end="")
                        print(" can deflect this card. Deflect?" +
                              Fore.CYAN + " (y/n) " + Fore.RESET + ": ", end="")
                        if input().upper() == "Y":
                            computer.deflect(
                                key, self, gameCard, market, rules)
                            print(Fore.CYAN + computer.name + Fore.RESET +
                                  " deflected the card")
                        else:
                            computer.pickTwo(market)
                            if len(self.cards) == 1:
                                print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                                      Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                            if len(self.cards) == 0:
                                self.hasWon = True
                    else:
                        print(Fore.CYAN + computer.name +
                              Fore.RESET + " deflected the card")
                        computer.deflect(key, self, gameCard, market, rules)
                else:
                    print(Fore.CYAN + computer.name + Fore.RESET +
                          " couldn't deflect the card")
                    computer.pickTwo(market)
                    if len(self.cards) == 1:
                        print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                              Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                    if len(self.cards) == 0:
                        self.hasWon = True
                return

            elif specials.index(key) == 3 and rules.pickThree:
                self.cards.pop(Index)
                market.append(gameCard[0])
                shuffle(market)
                gameCard.pop(0)
                print(" - That's a " + Fore.YELLOW +
                      cardDict[key] + Fore.RESET)
                computer.hasToPick = 3
                print(Fore.CYAN + computer.name + Fore.RESET + " has to pick " +
                      Fore.MAGENTA + str(computer.hasToPick) + Fore.RESET + " cards")
                canDeflect = computer.canDeflect(key)
                if canDeflect:
                    if self.name == 'COMPUTER':
                        print(Fore.CYAN + computer.name + Fore.RESET, end="")
                        print(" can deflect this card. Deflect?" +
                              Fore.CYAN + " (y/n) " + Fore.RESET + ": ", end="")
                        if input().upper() == "Y":
                            computer.deflect(
                                key, self, gameCard, market, rules)
                            print(Fore.CYAN + computer.name + Fore.RESET +
                                  " deflected the card")
                        else:
                            computer.pickThree(market)
                            if len(self.cards) == 1:
                                print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                                      Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                            if len(self.cards) == 0:
                                self.hasWon = True
                    else:
                        print(Fore.CYAN + computer.name +
                              Fore.RESET + " deflected the card")
                        computer.deflect(key, self, gameCard, market, rules)
                else:
                    print(Fore.CYAN + computer.name + Fore.RESET +
                          " couldn't deflect the card")
                    computer.pickThree(market)
                    if len(self.cards) == 1:
                        print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                              Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                    if len(self.cards) == 0:
                        self.hasWon = True
                return

            elif specials.index(key) == 4 and rules.suspension:
                print(" - That's a " + Fore.YELLOW +
                      cardDict[key] + Fore.RESET)
                self.cards.pop(Index)
                market.append(gameCard[0])
                shuffle(market)
                gameCard.pop(0)
                if len(self.cards) == 1:
                    print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                          Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
                if len(self.cards) == 0:
                    print(Fore.CYAN + self.name + Fore.RESET + " can't win with a " +
                          Fore.YELLOW + "'suspension'" + Fore.RESET + " so")
                    self.goToMarket(market, computer)
                    self.hasWon = False
                self.isTurn = True
                computer.isTurn = False
                return

        self.cards.pop(Index)

        if self.jokerWasLastCard == True:
            self.goToMarket(market, computer)
            self.jokerWasLastCard = False

        market.append(gameCard[0])
        shuffle(market)
        gameCard.pop(0)
        if len(self.cards) == 1:
            print(Fore.CYAN + self.name + Fore.RESET + " said - " +
                  Fore.MAGENTA + "'Last Card!!'" + Fore.RESET)
        if len(self.cards) == 0:
            self.hasWon = True
        self.isTurn = False
        computer.isTurn = True
        return

    def takeTurn(self, computer, gameCard, market, rules):

        print("What would you like to do?")
        displaySuites()
        print("Play a card" + Fore.CYAN + " ( 1 -", str(len(self.cards)), ")" + Fore.RESET +
              " Go to Market " + Fore.CYAN + "( " + str(len(self.cards) + 1) + " )" + Fore.RESET + " : ", end="")
        action = input()

        try:
            if int(action) in range(1, len(self.cards) + 1):
                cardParts = self.cards[int(action) - 1].split(" ")
                if cardParts[1] == joker[0]:
                    print("That's a Joker!")
                    self.playJoker(computer)
                    self.forcePlay(int(action) - 1,
                                   gameCard, computer, market, rules)

                    return
                if len(self.hasToPlay) > 0:
                    if self.cards[int(action) - 1].split(" ")[1] == self.hasToPlay:
                        self.forcePlay(int(action) - 1,
                                       gameCard, computer, market, rules)
                        self.hasToPlay = ""
                    else:
                        print("Sorry " + Fore.CYAN + self.name + Fore.RESET + ", " + Fore.CYAN + computer.name +
                              Fore.RESET + " said you have to play a " + Fore.MAGENTA + self.hasToPlay + Fore.RESET)
                    return
                canPlay = self.canPlay(int(action), gameCard)
                if canPlay:
                    self.playCard(int(action), gameCard,
                                  market, computer, rules)
                else:
                    print("Sorry " + Fore.CYAN + self.name +
                          Fore.RESET + ", you can't play that card")
                    print("(enter " + Fore.YELLOW + "'--help'" + Fore.RESET +
                          " for help, or " + Fore.YELLOW + "'--rules'" + Fore.RESET + " for rules)")
            elif int(action) == len(self.cards) + 1:
                self.goToMarket(market, computer)
                return
        except:
            if action == "--help":
                showHelp()

            elif action == "--rules":
                print(rules)

    def __str__(self):
        return (self.name, self.score, self.hasWon, self.isTurn)


# Rules Class
class Rules:
    def __init__(self, pickTwo=True, pickThree=True, holdOn=True, suspension=True, generalMarket=True, deflect=False):
        self.pickTwo = pickTwo
        self.pickThree = pickThree
        self.holdOn = holdOn
        self.suspension = suspension
        self.generalMarket = generalMarket
        self.deflect = deflect

    def __str__(self):
        return (f"Current game rules are:\n    Rule\t\tIs Enabled\n1. Pick Two:\t\t - {self.pickTwo}\n2. Pick Three:\t\t - {self.pickThree}\n3. Hold On:\t\t - {self.holdOn}\n4. Suspension:\t\t - {self.suspension}\n5. General Market:\t - {self.generalMarket}")


# Game Class
class Game:
    def __init__(self, rules, deck=[], market=[]):
        self.deck = deck
        self.market = market
        self.rules = rules

    def serveCards(self):
        cards = []
        for i in range(noOfStartingCards):
            cards.append(deck[-1])
            self.deck.pop()
        return cards

    def setMarket(self):
        self.market = self.deck[0: len(self.deck) - 1]
        del self.deck[0: len(self.deck) - 1]

    def goToMarket(self):
        print(Fore.MAGENTA + "Game " + Fore.RESET +
              "started with a WHOT card so")
        print(Fore.MAGENTA + "Game " + Fore.RESET + "went to the market")
        self.deck.append(self.market[-1])
        self.market.append(self.deck[0])
        self.deck.pop(0)
        shuffle(self.market)

    def __str__(self):
        return(self.deck, self.market, self.rules)


# Game Menu
def mainMenu():
    clear()

    showTitle("Let's Play WHOT")
    print(Fore.CYAN + " [1]" + Fore.RESET +
          " Start A New Game")
    print(Fore.CYAN + " [2]" + Fore.RESET + " View How to Play")
    print(Fore.CYAN + " [3]" + Fore.RESET + " Exit Program")
    print("\n - Please select an option " + Fore.CYAN +
          "(1 - 3)" + Fore.RESET+": ", end="")
    menuOption = input()
    try:
        if int(menuOption) == 1:
            prepareNewGame()

        elif int(menuOption) == 2:
            showHelp()

        elif int(menuOption) == 3:
            showTitle('Thank you for Playing')
            sys.exit(0)
    except:
        if menuOption == "--help":
            showHelp()
    else:
        print("Please enter a valid option")


mainMenu()


displaySuites()
playerName = input("What's your name, Player? : ").upper()
player = Player(playerName)
computer = Player("Computer".upper())

displaySuites()
print(player.name, end="")
print(", do you want to use the default options? (default is yes) (y/n): ", end="")
useDefaultOptions = input().upper()
if useDefaultOptions == "N":
    displaySuites()
    pickTwo = False if input(
        "Enable Pick Two? (Default is yes) (y/n) : ").upper() == "N" else True
    displaySuites()
    pickThree = False if input(
        "Enable Pick Three? (Default is yes) (y/n) : ").upper() == "N" else True
    displaySuites()
    holdOn = False if input(
        "Enable Hold On? (Default is yes) (y/n) : ").upper() == "N" else True
    displaySuites()
    suspension = False if input(
        "Enable Suspension? (Default is yes) (y/n) : ").upper() == "N" else True
    displaySuites()
    generalMarket = False if input(
        "Enable General Market? (Default is yes) (y/n) : ").upper() == "N" else True
    displaySuites()
    deflection = False if input(
        "Enable Deflection? (Default is yes) (y/n) : ").upper() == "N" else True
    rules = Rules(pickTwo, pickThree, holdOn,
                  suspension, generalMarket, deflection)
else:
    rules = Rules()
showTitle("Rules Set")
print(rules)

# create new deck, and empty market
displaySuites()
print("Setting Deck")
newDeck = makeDeck(deck, suites, letters, numbers, noOfJokers)
# Shuffle Deck
displaySuites()
print("shuffling Cards")
shuffle(newDeck)
# create game object with rules
displaySuites()
print("setting up New Game")
input("Press any Button to continue...")


clear()
game = Game(rules, newDeck, [])
player.cards = game.serveCards()
computer.cards = game.serveCards()
game.setMarket()
player.isTurn = True
while game.deck[0].split(" ")[1] == joker[0]:
    game.goToMarket()

while player.hasWon == computer.hasWon == False:
    displayGame(game, player, computer)
    print("\n", end="")
    if player.isTurn:
        print(Fore.CYAN + player.name +
              Fore.RESET + ", it's your turn")
        player.takeTurn(computer, game.deck, game.market, game.rules)
        sleep(1)
    else:
        print("it's the " + Fore.CYAN +
              computer.name + Fore.RESET + "'s turn")
        computer.autoPlay(player, game.deck, game.market, game.rules)
        sleep(1)
if player.hasWon:
    showTitle(player.name + ' WINS!!!')
    displaySuites()
    print(" - Congrats " + Fore.CYAN +
          player.name + Fore.RESET + "! Good Game!!!")
    input("Press any Key to continue... ")

elif computer.hasWon:
    showTitle(computer.name + " WINS!!!")
    displaySuites()
    print(" - Too bad " + Fore.CYAN + player.name +
          Fore.RESET + ", maybe next time ")
    input("Press any Key to continue...")
mainMenu()
