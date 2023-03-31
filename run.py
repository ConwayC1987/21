# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

# Create a deck of cards
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
values = ['Ace', '2', '3' '4', '5', '6', '7', '8', '9', '10']
deck = [(suit, value) for suit in suits for value in values]

# Shuffle deck
random.shuffle(deck)

name = input("Enter your name:")

chips = 100

wins = 0
losses = 0

