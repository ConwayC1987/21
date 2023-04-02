import random
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
        deck.append(color + rank + suit + '\033[0m')  # add color to the card
        
# For loop to shuffle the deck using the index.
for x in range(len(deck)):
    card1 = deck[x]
    r = random.randint(0, len(deck)-1)
    card2 = deck[r]
    deck[x] = card2
    deck[r] = card1

for card in deck:
    print(card, end=' ')
# Define a player name
print("Welcome to \u001b[30mBlack\u001b[31mJack!")
print("The rules are:")
print("Aim of JackJack is to get 21 or as close to as possible.")
print("Jacks, kings and queens are worth 10. Ace can be either 1 or 11.")
print("You get 2 cards face up and the dealer will recieve 1 card face down.")
print("You have a choice to hit or stand until you or the dealer goes bust.")
print("You will start with 100 chips and can bet each hand.")
print("You will be playing against the computer.")

name = input("What is your name? ")

chips = 100

winS = 0
losseS = 0