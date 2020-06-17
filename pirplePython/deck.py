# suites = (u'\u2660', u'\u2665', u'\u2666', u'\u2663', u'\u2605')
# opensuites = (u'\u2664', u'\u2661', u'\u2662', u'\u2667', u'\u2730')

from random import shuffle
import random
from colorama import init, Fore, Back, Style

init()
print(dir(random))

suites = (u'\u2660', u'\u2665', u'\u2666', u'\u2663')
opensuites = (u'\u2664', u'\u2661', u'\u2662', u'\u2667')


def displaySuites():
    print(" " + u'\u2660' + " " + Fore.RED + u'\u2666' + " " + Fore.RESET +
          u'\u2663' + " " + Fore.RED + u'\u2665' + " " + Fore.RESET, end="")


# joker = ("W " + u'\u2605')
noOfJokers = 4
numbers = [2, 3, 4, 5, 6, 7, 8, 9]
letters = ["A", "J", "Q", "K"]
noOfPlayingCards = 5
deck = []
print(suites)
print(opensuites)


def displayCards(cards):
    red = (u'\u2665',  u'\u2666')
    black = (u'\u2660',  u'\u2663')
    joker = (u'\u2605',)
    # print(red, black)
    for card in cards:
        cardParts = card.split(" ")
        # print(cardParts)
        if cardParts[1] in red:
            print(Back.WHITE + Fore.YELLOW + " : " + Fore.RED +
                  cardParts[0], cardParts[1] + Back.WHITE, end="")
        elif cardParts[1] in black:
            print(Back.WHITE + Fore.YELLOW + " : " + Fore.BLACK +
                  cardParts[0], cardParts[1] + Back.WHITE, end="")
        elif cardParts[1] in joker:
            print(Back.WHITE + Fore.YELLOW + " : " + Fore.MAGENTA +
                  cardParts[0], cardParts[1] + Back.WHITE, end="")
    print(Fore.YELLOW + " : " + Back.RESET + Fore.RESET, end="")


def makeDeck(deck, suites, letters, numbers):
    for suite in suites:
        for number in numbers:
            card = str(number) + " " + suite
            deck.append(card)
        for letter in letters:
            card = letter + " " + suite
            deck.append(card)
    for i in range(noOfJokers):
        joker = "W"+str(i+1)+" "+u'\u2605'
        deck.append(joker)
    return deck


deck = makeDeck(deck, suites, letters, numbers)
displayCards(deck)
shuffle(deck)


def serveCards(deck, playerCards):
    for i in range(noOfPlayingCards):
        playerCards.append(deck[-1])
        deck.pop()


def setMarket(deck, market):
    market = deck[0: len(deck) - 1]
    del deck[0: len(deck) - 1]
    return market
# (u'\u2660', u'\u2665', u'\u2666', u'\u2663')
# colorDict = {
# }


# print(deck)
computerCards = []
player1Cards = []
market = []
serveCards(deck, computerCards)
serveCards(deck, player1Cards)
market = setMarket(deck, market)
print("\n ====== Market ======")
displayCards(market)
print("\n ====== Game Area ======")


print("\n" + Back.RESET + Fore.MAGENTA + "Computer" +
      Fore.RESET + "'s Cards ", u'\u27a4', " " + Fore.RESET + Back.RESET, end="")
displayCards(computerCards)
print('\n', end="")
print("\n" + Fore.MAGENTA + "Game Card ", u'\u27a4', " ", end="")
displayCards(deck)
print("\t\tMarket ", u'\u27a4', " (", str(len(market)), ")[", end="")
displaySuites()
print("]\n\n" + Back.RESET + Fore.MAGENTA + "Player" +
      Back.RESET + Fore.RESET + "'s Cards ", u'\u27a4', " ", end="")
displayCards(player1Cards)
print('\n', end="")
# # print("Computer - ")
# print(market[len(market)-2:len(market)])
# market.pop()
# market.pop()
# print(market)
# print(market[len(market)-1])
# print(deck)

"""
  Game Rules
  - Each player gets 5 cards at the beginning, 
  - 2 - pick 2
  - 5 - pick 3
  - A - hold on
  - 8 - Suspension
  - K - General Market
"""
