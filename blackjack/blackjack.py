import random

from art import logo

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if start_game == 'y':
    print(logo)

    def deal_card():
        return random.choice(cards)

    user_cards = []
    computer_cards = []

    # user_choose = input("Type 'y' to get another card, type 'n' to pass: ")