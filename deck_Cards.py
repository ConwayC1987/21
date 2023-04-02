deck = []
for suit in ['\u2663', '\u2660', '\u2665', '\u2666']:
    if suit in ['\u2663', '\u2660']:  # Clubs and Spades are black
        color = '\033[30m'  # set color to black
    else:  # Hearts and Diamonds are red
        color = '\033[31m'  # set color to red
    for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
        # Joins the rank and card suit using the unicode for visual appeal.
        # Creates a full deck index 0 to 51.
        deck.append(color + rank + suit + '\033[0m')  # add color to the card

# print the deck of cards
for card in deck:
    print(card)