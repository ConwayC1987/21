
def print_cards(cardList):
    for card in zip(*cardList):
        print(' '.join(card))


def print_card(*cards):
    for line in zip(*cards):
        print(' '.join(line))


def card_visual(card):
    suits = "Spades Diamonds Hearts Clubs".split()
    suit_symbols = ['♠','♦','♥','♣']
    suit_pairs = dict(zip(suits, suit_symbols))

    v = card.value
    s = suit_pairs 

    visual = [
        '╔══════╗',
       f'║{v:<3} ║',
       f'║      ║',
       f'║{s:>3} ║',
        '╚══════╝'
    ]

    return visual