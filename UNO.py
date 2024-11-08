import math
from colorama import Fore, Back, Style
from pynput import keyboard
from pynput.keyboard import Key
import time
import os
import random


# Here's a huge list of ASCII cards
# You have to scroll down to line 613 see the important code
cardOneGreen = Style.BRIGHT + Fore.GREEN + """
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
cardTwoGreen = Style.BRIGHT + Fore.GREEN + """
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
cardThreeGreen = Style.BRIGHT + Fore.GREEN + """
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
cardFourGreen = Style.BRIGHT + Fore.GREEN + """
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
cardFiveGreen = Style.BRIGHT + Fore.GREEN + """
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
cardSixGreen = Style.BRIGHT + Fore.GREEN + """
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
cardSevenGreen = Style.BRIGHT + Fore.GREEN + """
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
cardEightGreen = Style.BRIGHT + Fore.GREEN + """
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
cardNineGreen = Style.BRIGHT + Fore.GREEN + """
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
cardZeroGreen = Style.BRIGHT + Fore.GREEN + """
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
cardPlusTwoGreen = Style.BRIGHT + Fore.GREEN + """
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
cardSkipGreen = Style.BRIGHT + Fore.GREEN + """
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
"""
cardOneRed = Style.BRIGHT + Fore.RED + """
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
cardTwoRed = Style.BRIGHT + Fore.RED + """
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
cardThreeRed = Style.BRIGHT + Fore.RED + """
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
cardFourRed = Style.BRIGHT + Fore.RED + """
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
cardFiveRed = Style.BRIGHT + Fore.RED + """
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
cardSixRed = Style.BRIGHT + Fore.RED + """
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
cardSevenRed = Style.BRIGHT + Fore.RED + """
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
cardEightRed = Style.BRIGHT + Fore.RED + """
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
cardNineRed = Style.BRIGHT + Fore.RED + """
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
cardZeroRed = Style.BRIGHT + Fore.RED + """
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
cardPlusTwoRed = Style.BRIGHT + Fore.RED + """
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
cardSkipRed = Style.BRIGHT + Fore.RED + """
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
"""
cardOneBlue = Style.BRIGHT + Fore.BLUE + """
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
cardTwoBlue = Style.BRIGHT + Fore.BLUE + """
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
cardThreeBlue = Style.BRIGHT + Fore.BLUE + """
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
cardFourBlue = Style.BRIGHT + Fore.BLUE + """
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
cardFiveBlue = Style.BRIGHT + Fore.BLUE + """
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
cardSixBlue = Style.BRIGHT + Fore.BLUE + """
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
cardSevenBlue = Style.BRIGHT + Fore.BLUE + """
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
cardEightBlue = Style.BRIGHT + Fore.BLUE + """
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
cardNineBlue = Style.BRIGHT + Fore.BLUE + """
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
cardZeroBlue = Style.BRIGHT + Fore.BLUE + """
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
cardPlusTwoBlue = Style.BRIGHT + Fore.BLUE + """
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
cardSkipBlue = Style.BRIGHT + Fore.BLUE + """
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
"""
cardOneYellow = Style.BRIGHT + Fore.YELLOW + """
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
cardTwoYellow = Style.BRIGHT + Fore.YELLOW + """
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
cardThreeYellow = Style.BRIGHT + Fore.YELLOW + """
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
cardFourYellow = Style.BRIGHT + Fore.YELLOW + """
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
cardFiveYellow = Style.BRIGHT + Fore.YELLOW + """
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
cardSixYellow = Style.BRIGHT + Fore.YELLOW + """
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
cardSevenYellow = Style.BRIGHT + Fore.YELLOW + """
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
cardEightYellow = Style.BRIGHT + Fore.YELLOW + """
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
cardNineYellow = Style.BRIGHT + Fore.YELLOW + """
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
cardZeroYellow = Style.BRIGHT + Fore.YELLOW + """
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
cardPlusTwoYellow = Style.BRIGHT + Fore.YELLOW + """
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
cardSkipYellow = Style.BRIGHT + Fore.YELLOW + """
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
"""
cardWild = Style.BRIGHT + Fore.WHITE + """
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
cardWildPlusFour = Style.BRIGHT + Fore.WHITE + """
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

gameruleStack = False
userDeck = []
botDeck = []
gameDeck = []

gameDeck = [cardOneGreen, cardTwoGreen, cardThreeGreen, cardFourGreen, cardFiveGreen, cardSixGreen, cardSevenGreen, cardEightGreen, cardNineGreen, cardZeroGreen, cardPlusTwoGreen, cardSkipGreen, cardOneGreen, cardTwoGreen, cardThreeGreen, cardFourGreen, cardFiveGreen, cardSixGreen, cardSevenGreen, cardEightGreen, cardNineGreen, cardZeroGreen, cardPlusTwoGreen, cardSkipGreen, cardOneRed, cardTwoRed, cardThreeRed, cardFourRed, cardFiveRed, cardSixRed, cardSevenRed, cardEightRed, cardNineRed, cardZeroRed, cardPlusTwoRed, cardSkipRed, cardOneRed, cardTwoRed, cardThreeRed, cardFourRed, cardFiveRed, cardSixRed, cardSevenRed, cardEightRed, cardNineRed, cardZeroRed, cardPlusTwoRed, cardSkipRed, cardOneBlue, cardTwoBlue, cardThreeBlue, cardFourBlue, cardFiveBlue, cardSixBlue, cardSevenBlue, cardEightBlue, cardNineBlue, cardZeroBlue, cardPlusTwoBlue, cardSkipBlue, cardOneBlue, cardTwoBlue, cardThreeBlue, cardFourBlue, cardFiveBlue, cardSixBlue, cardSevenBlue, cardEightBlue, cardNineBlue, cardZeroBlue, cardPlusTwoBlue, cardSkipBlue, cardOneYellow, cardTwoYellow, cardThreeYellow, cardFourYellow, cardFiveYellow, cardSixYellow, cardSevenYellow, cardEightYellow, cardNineYellow, cardZeroYellow, cardPlusTwoYellow, cardSkipYellow, cardOneYellow, cardTwoYellow, cardThreeYellow, cardFourYellow, cardFiveYellow, cardSixYellow, cardSevenYellow, cardEightYellow, cardNineYellow, cardZeroYellow, cardPlusTwoYellow, cardSkipYellow, cardWild, cardWild, cardWild, cardWild, cardWildPlusFour, cardWildPlusFour, cardWildPlusFour, cardWildPlusFour]

#Shuffles gameDeck
random.shuffle(gameDeck)

# def addUserCards():
#    e

# #Card Input
# cardSelector = 0
# def on_press(key):
    
#     global cardSelector
#     if key == keyboard.Key.up:
#         if cardSelector < 6:
#             cardSelector += 1
#         print('beep', cardSelector)
#     if key == keyboard.Key.down:
#         if cardSelector > 0:
#             cardSelector -= 1
#         print("boop", cardSelector)
#     if key == keyboard.Key.enter:
#         os.system('cls')    
#     if key == keyboard.Key.esc:
#         listener.stop()
    
# with keyboard.Listener(on_press=on_press) as listener:
#         listener.join()


# #This is if you want to print the entire deck, uncomment it if you want to test it
# for n in gameDeck:
#     print(n)

#This is my attempt at making the loop to add seven gameDeck values to userDeck
loop = 0
while loop <= 6:
    userDeck += gameDeck[loop]
    loop += 1

# for i in userDeck:
#     print(i)