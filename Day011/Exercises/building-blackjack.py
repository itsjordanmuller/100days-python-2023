import random

from art import logo
print(logo)
print("------------------  HOUSE RULES  ------------------\n1. The deck is unlimited in size.\n2. There are no jokers.\n3. The Jack/Queen/King all count as 10.\n4. The the Ace can count as 11 or 1.\n5. Cards are not removed from the deck as they are drawn.\n6. The computer is the dealer.\n---------------------  START  ---------------------")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    print(random.choice(cards))

deal_card()

def play_game():
    game_over = False

    while not game_over:
        play_game()

        print(logo)
        print("------------------  HOUSE RULES  ------------------\n1. The deck is unlimited in size.\n2. There are no jokers.\n3. The Jack/Queen/King all count as 10.\n4. The the Ace can count as 11 or 1.\n5. Cards are not removed from the deck as they are drawn.\n6. The computer is the dealer.\n---------------------  START  ---------------------")

play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y"
while play_again == "y":
    play_game()