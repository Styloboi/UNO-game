import math
from colorama import Fore, Back, Style
from pynput import keyboard
from pynput.keyboard import Key
import time
import os
import random


# Here's a huge list of ASCII cards
# You have to scroll down to line 181 see the important code
cardOne = """
╔════════╗
║░░░/┐░░░║
║░░/││░░░║
║░░└││░░░║
║░░░││░░░║
║░░░││░░░║
║░░░││░░░║
║░░░││░░░║
║░░░└┘░░░║
╚════════╝
"""
cardTwo = """
╔════════╗
║░░/──\░░║
║░/ ── \░║
║░└┘░░ │░║
║░░░░/ │░║
║░░░/ /░░║
║░░/ /░░░║
║░/ ───┐░║
║░└────┘░║
╚════════╝
"""
cardThree = """
╔════════╗
║░░/──\░░║
║░/┌──┐\░║
║░└┘░░││░║
║░░░┌─┘│░║
║░░░└─┐│░║
║░┌┐░░││░║
║░\└──┘/░║
║░░\──/░░║
╚════════╝
"""
cardFour = """
╔════════╗
║░░░/┐░░░║
║░░/││░░░║
║░//││░░░║
║░│└││─┐░║
║░└─││─┘░║
║░░░││░░░║
║░░░││░░░║
║░░░└┘░░░║
╚════════╝
"""
cardFive = """
╔════════╗
║░┌────┐░║
║░│┌───┘░║
║░││░░░░░║
║░│└──\░░║
║░└─── \░║
║░┌┐░░││░║
║░\ ── /░║
║░░\──/░░║
╚════════╝
"""
cardSix = """
╔════════╗
║░░/──\░░║
║░/ ── \░║
║░││░░└┘░║
║░│ ──\░░║
║░│ ── \░║
║░││░░││░║
║░\ ── /░║
║░░\──/░░║
╚════════╝
"""
cardSeven = """
╔════════╗
║░┌────┐░║
║░└─── /░║
║░░░░//░░║
║░░░//░░░║
║░░░││░░░║
║░░░││░░░║
║░░░││░░░║
║░░░└┘░░░║
╚════════╝
"""
cardEight = """
╔════════╗
║░░/──\░░║
║░/ ── \░║
║░││░░││░║
║░\ ── /░║
║░/ ── \░║
║░││░░││░║
║░\ ── /░║
║░░\──/░░║
╚════════╝
"""
cardNine = """
╔════════╗
║░░/──\░░║
║░/ ── \░║
║░││░░││░║
║░\ ── │░║
║░░\── │░║
║░┌┐░░││░║
║░\ ── /░║
║░░\──/░░║
╚════════╝
"""
cardZero = """
╔════════╗
║░░/──\░░║
║░/ ── \░║
║░││░░││░║
║░││░░││░║
║░││░░││░║
║░││░░││░║
║░\ ── /░║
║░░\──/░░║
╚════════╝
"""
cardPlusTwo = """
╔════════╗
║░║░░░░░░║
║═╬═░░░░░║
║░║░░__░░║
║░░░/_ \░║
║░░░░░//░║
║░░░░//░░║
║░░░/ ─┐░║
║░░░───┘░║
╚════════╝
"""
cardWild = """
╔════════╗
║░┌┐░░┌┐░║
║░││░░││░║
║░││░░││░║
║░││░░││░║
║░││┌┐││░║
║░││││││░║
║░\└┘└┘/░║
║░░\/\/░░║
╚════════╝
"""
cardWildPlusFour = """
╔════════╗
║░║░░░║║░║
║═╬═░░╚╬═║
║░║░░░░║░║
║░┌┐░░┌┐░║
║░││░░││░║
║░││┌┐││░║
║░\└┘└┘/░║
║░░\/\/░░║
╚════════╝
"""
cardSkip = Fore.GREEN + """
╔════════╗
║░░/──\░░║
║░/ ─┐ \░║
║░││░/ │░║
║░││/ ││░║
║░││ /││░║
║░│ /░││░║
║░\ └─ /░║
║░░\──/░░║
╚════════╝
""" + Style.RESET_ALL

cardDeckDraw = """

"""

gameruleStack = False
userDeck = []
botDeck = []
cardSelector = 0
gameDeck = []

wildCards = [cardWild, cardWild, cardWild, cardWild, cardWildPlusFour, cardWildPlusFour, cardWildPlusFour, cardWildPlusFour,]
redCards = [cardOne, cardOne, cardTwo, cardTwo, cardThree, cardThree, cardFour, cardFour, cardFive, cardFive, cardSix, cardSix, cardSeven, cardSeven, cardEight, cardEight, cardNine, cardNine, cardZero, cardZero, cardSkip, cardSkip, cardPlusTwo, cardPlusTwo]
greenCards = [cardOne, cardOne, cardTwo, cardTwo, cardThree, cardThree, cardFour, cardFour, cardFive, cardFive, cardSix, cardSix, cardSeven, cardSeven, cardEight, cardEight, cardNine, cardNine, cardZero, cardZero, cardSkip, cardSkip, cardPlusTwo, cardPlusTwo]
blueCards = [cardOne, cardOne, cardTwo, cardTwo, cardThree, cardThree, cardFour, cardFour, cardFive, cardFive, cardSix, cardSix, cardSeven, cardSeven, cardEight, cardEight, cardNine, cardNine, cardZero, cardZero, cardSkip, cardSkip, cardPlusTwo, cardPlusTwo]
yellowCards = [cardOne, cardOne, cardTwo, cardTwo, cardThree, cardThree, cardFour, cardFour, cardFive, cardFive, cardSix, cardSix, cardSeven, cardSeven, cardEight, cardEight, cardNine, cardNine, cardZero, cardZero, cardSkip, cardSkip, cardPlusTwo, cardPlusTwo]

gameDeck = redCards + greenCards + blueCards + yellowCards + wildCards
random.shuffle(gameDeck)

def on_press(key):
    global cardSelector
    if key == keyboard.Key.up:
        if cardSelector < 6:
            cardSelector += 1
        print('beep', cardSelector)
    if key == keyboard.Key.down:
        if cardSelector > 0:
            cardSelector -= 1
        print("boop", cardSelector)
    if key == keyboard.Key.esc:
        listener.stop()
    
    
with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

for i in gameDeck:
    print(i)
