import random
# Create a deck of cards
deck = []
# Deck idea from https://www.youtube.com/watch?v=
# Unicode characters used for the suits on the cards.
for suit in ['\u2663', '\u2660', '\u2665', '\u2666']: 
    for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
        # Joins the rank and card suit using the unicode for visual appeal.
        # Creates a full deck index 0 to 51.
        deck.append(rank+suit)
# For loop to shuffle the deck.
for x in range(len(deck)):
    card1 = deck[x]
    r = random.randint(0, len(deck)-1)
    card2 = deck[r]
    deck[x] = card2
    deck[r] = card1

for card in deck:
    print(card, end=' ')
# Define a player name
print("Welcome to Blackjack!")

name = input("What is your name? ")

chips = 100

winS = 0
losseS = 0