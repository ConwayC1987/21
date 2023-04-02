import random
import os
# Create a deck of cards
deck = []
# Deck idea from https://www.youtube.com/watch?v=
# Unicode characters used for the suits on the cards.
for suit in ['\u2663', '\u2660', '\u2665', '\u2666']:
    if suit in ['\u2663', '\u2660']:  # Clubs and Spades are black
        color = '\033[30m'  # set color to black
    else:  # Hearts and Diamonds are red
        color = '\033[31m'  # set color to red
    for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
        # Joins the rank and card suit using the unicode for visual appeal.
        # Creates a full deck index 0 to 51.
        deck.append(color + rank + suit + '\033[0m')  # add color to the cards.
# For loop to shuffle the deck using the index.
for x in range(len(deck)):
    card1 = deck[x]
    r = random.randint(0, len(deck)-1)
    card2 = deck[r]
    deck[x] = card2
    deck[r] = card1

#for card in deck:
    #print(card, end=' ')


def clear_terminal():
    if os.name == 'nt':  # for windows
        os.system('cls')
    else:  # for mac and linux(here, os.name is 'posix')
        os.system('clear')


# Define a player name
print("\u001b[1mWelcome to \u001b[30mBlack\u001b[31mJack!")
name = input("\u001b[32mWhat is your name? ")

# Create and game option to view the game
while True:
    try:
        print("\u001b[42m\u001b[37;1mPlease read the rules first")
        print("\nPress 2 to read the rules or 1 to play\u001b[0m")
        Options = int(input("\n1.Play Game\n2.Rules\noption"))
        if Options == 1:
            PlayGame = True
            break

        if Options == 2:
            clear_terminal()
            print("""
            \u001b[41;1mThe rules are:\u001b[0m
            1.Aim of JackJack is to get 21 or as close to as possible. \n 
            2.Jacks, kings and queens are worth 10. Ace can be either 1 or 11.\n
            3.You get 2 cards face up and the dealer will recieve 1 card face down. \n
            4.You have a choice to hit or stand until you or the dealer goes bust. \n
            5.You will start with 100 chips and can bet each hand. \n
            6.You will be playing against the computer.""")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Add a class to make the cards
