import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare(player_score, computer_score):
    if player_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif player_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "Computer has a blackjack. You lose."
    elif player_score == 0:
        return "You have a blackjack! You win."
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose."

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
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            draw_card = input("Do you want to draw another card? Type 'y' or 'n': ")
            if draw_card == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    while computer_score < 17 and not game_over:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

play_again = "y"
while play_again == "y":
    play_game()
    play_again = input("Do you want to play again? Type 'y' or 'n': ")