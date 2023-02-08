print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input("Would you like to go left or right? ").lower()
if direction == "left":
    swim = input("You go to the left and come to a dock. There is an island out in the middle of the lake. Type 'Wait' to wait, or 'Swim' to swim across. ")
    if swim == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which do you choose? ")
        if door == "red":
            print("You enter a roomm full of fire and die. Game over.")
        elif door == "yellow":
            print("You find a pot of gold! You win!")
        else:
            print("A wizard greets you, to tell you that you've lost. He vaporizes you with his electricity spell. Game over.")
    elif swim == "swim":
        print("You try to swim across, but you drown and die. Game over.")
else:
    print("You go to the right and are eaten by a dragon. Game over.")