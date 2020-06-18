"""
File: main.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Final Project
Task: Whot Card game
"""
# Game Imports
from os import system, name, path
import sys
from random import shuffle, choice
from colorama import init, Fore, Back, Style
from time import sleep
init()

# Game Constants
redSuite = (u'\u2665',  u'\u2666')
blackSuite = (u'\u2660',  u'\u2663')
suites = (u'\u2660', u'\u2665', u'\u2666', u'\u2663')
joker = (u'\u2605',)
noOfJokers = 5
# numbers = [2, 3, 4, 5, 6, 7, 8, 9]
numbers = [2, 5, 8]
# letters = ["A", "J", "Q", "K"]
letters = ["A", "K"]
specials = ["K", "A", "2", "5", "8"]
cardDict = {'A': 'hold on', '2': 'pick two', '5': 'pick three',
            '8': 'suspension', 'K': 'general market'}
noOfStartingCards = 5
deck = []
gameIsOn = False


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

# Show Help


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


########## Game Objects ##########
# Player Object
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
        print(self.name, "picked 2 cards from the market")

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
                    print("line 335 - That's a " + Fore.YELLOW +
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
                    print("line 352 - That's a " + Fore.YELLOW +
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

        elif cardParts[1] == gameCardParts[1]:
            print(Fore.CYAN + self.name + Fore.RESET + " played ", end="")
            displaySingleCard(self.cards[cardIndex-1], end="\n")
            gameCard.append(self.cards[cardIndex-1])
            if self.cards[cardIndex-1].split(" ")[0] in cardDict.keys():
                key = self.cards[cardIndex-1].split(" ")[0]
                if specials.index(key) == 0 and rules.generalMarket:
                    print("line 419 - That's a " + Fore.YELLOW +
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
                    print("line 352 - That's a " + Fore.YELLOW +
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
                print("line 419 - That's a " + Fore.YELLOW +
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

            elif specials.index(key) == 1 and rules.holdOn:
                print("line 352 - That's a " + Fore.YELLOW +
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
                    print("reached here - line 447")
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
        except:
            if action == "--help":
                showHelp()
            elif action == "--resume":
                loadSavedGame()

    def __str__(self):
        return (self.name, self.score, self.hasWon, self.isTurn)

# Rules Object


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


# Game Object
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


def gameLoop(game, player, computer):
    # ##### Game Loop begins ######
    player.isTurn = True
    # Game Display Game
    displayGame(game, player, computer)
    while True:
        if player.hasWon == False and computer.hasWon == False:
            game.displayGame()
            if player.isTurn:
                player.takeTurn()
            else:
                computer.autoPlay(player, game.deck, game.market, rules)


# Game Menu
def mainMenu():
    clear()
    showTitle("Let's Play WHOT")
    print(Fore.CYAN + " [1]" + Fore.RESET +
          " Start A New Game")
    print(Fore.CYAN + " [2]" + Fore.RESET +
          " Resume Saved Game")
    print(Fore.CYAN + " [3]" + Fore.RESET + " View Rules")
    print(Fore.CYAN + " [4]" + Fore.RESET + " Exit Program")
    while True:
        print("\n - Please select an option " + Fore.CYAN +
              "(1 - 4)" + Fore.RESET+": ", end="")
        option = input()
        try:
            if int(option) == 1:
                prepareNewGame()
            elif int(option) == 2:
                resumeGame()
            elif int(option) == 3:
                showHelp()
                newUrl = input("Please enter a URL : ")
                # runCode(newUrl)
            elif int(option) == 4:
                showTitle('Thank you for Playing')
                sys.exit(0)
        except:
            if option == "--help":
                showHelp()
            elif option == "--resume":
                loadSavedGame()


def setRules():
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
    return rules


def prepareNewGame():
    # Check if there's a saved File
    # if saved file, ask if User wants to overwrite file or resume
    # If resume, load file
    # If overwrite start new game and overwrite file
    # Get player name
    displaySuites()
    playerName = input("What's your name, Player? : ").upper()
    player = Player(playerName)

    # Ask to set rules, if yes ask options and set rules and instatiate rules object with answers
    displaySuites()
    print(player.name, end="")
    print(" want to use the default settings? (default is yes) (y/n): ", end="")
    useDefaultOptions = input().upper()
    if useDefaultOptions == "N":
        rules = setRules()
        pass
    else:
        rules = Rules()
    # showSmallTitle("Rules Set")
    print(rules)

    computer = Player("Computer")
    # create new deck, and empty market
    print("Setting Deck")
    newDeck = makeDeck(deck, suites, letters, numbers, noOfJokers)
    # Shuffle Deck
    print("shuffling Cards")
    shuffle(newDeck)
    # create game object with rules
    print("setting New Game")
    newGame = Game(rules, newDeck)
    # Game servercards to player
    newGame.serveCards(player)
    newGame.serveCards(computer)
    newGame.setMarket()
    # Game save Game

    # Start Game loo


# mainMenu()
# showHelp()
# Player plays card

# Check if card is special

def showyDeckDisplay(deck):
    displaySuites()
    displaySuites(True)
    for i in range(len(deck)):
        displaySingleCard(deck[i])
        if i > 0 and i % 11 == 0:
            displaySuites(True)
            displaySuites()
            print("\n")
        sleep(0.02)
    displaySuites(True)
    displaySuites()


newDeck = makeDeck(deck, suites, letters, numbers, noOfJokers)
showyDeckDisplay(newDeck)
shuffle(newDeck)
rules = Rules()
game = Game(rules, newDeck, [])
player = Player("Banky".upper())
computer = Player("Computer".upper())
# print(game.deck)
player.cards = game.serveCards()
computer.cards = game.serveCards()
print(player.cards, computer.cards)
# print(game.deck)
print(game.deck)

# print(player.cards, computer.cards)
game.setMarket()
# displayGame(game, player, computer)
player.isTurn = True
while game.deck[0].split(" ")[1] == joker[0]:
    game.goToMarket()
# clear()

while True:
    if player.hasWon == False and computer.hasWon == False:
        displayGame(game, player, computer)

        if player.isTurn:
            print(Fore.CYAN + player.name + Fore.RESET + ", it's your turn")
            player.takeTurn(computer, game.deck, game.market, game.rules)
            # sleep(2)
        else:
            print("it's the " + Fore.CYAN +
                  computer.name + Fore.RESET + "'s turn")
            computer.autoPlay(player, game.deck, game.market, game.rules)
            # sleep(2)
