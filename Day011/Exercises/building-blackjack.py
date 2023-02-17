import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def play_game():
    print(logo)
    print("------------------  HOUSE RULES  ------------------\n1. The deck is unlimited in size.\n2. There are no jokers.\n3. The Jack/Queen/King all count as 10.\n4. The the Ace can count as 11 or 1.\n5. Cards are not removed from the deck as they are drawn.\n6. The computer is the dealer.\n---------------------  START  ---------------------")
    player_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        draw_card = input("Do you want to draw another card? Type 'y' or 'n': ")
        if draw_card == "y":
            player_cards.append(deal_card())
        else:
            game_over = True

play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y"
while play_again == "y":
    play_game()