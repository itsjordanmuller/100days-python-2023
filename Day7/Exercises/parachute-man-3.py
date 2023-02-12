import random

stages = ['''
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/





      0
     /|\ 
     / \ 

=========
''', '''
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
      |
      |
      O
     /|\ 
     / \ 

=========
''', '''
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
   \     /
    \   /
     \O/
     /|\ 
     / \ 

=========
''', '''
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
   \ / \ /
    \   /
     \O/
     /|\ 
     / \ 

=========
''', '''
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
   \ / \|/
    \   /
     \O/
     /|\ 
     / \ 

=========
''', '''
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
   \|/ \|/
    \   /
     \O/
     /|\ 
     / \ 

=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = ["_"] * len(chosen_word)
print(display)

while "_" in display:
    guess = input("Choose a single letter: ").lower()
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
    print(display)
print("Game over, you won!")

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.