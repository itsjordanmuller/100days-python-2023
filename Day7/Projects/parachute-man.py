#Step 1 

import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#chosen_word = word_list[random.randint(0, (len(word_list)-1))]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Choose a single letter: ").lower()
if guess in chosen_word:
    print("That is one of the letters.")
else:
    print("That is not one of the letters.")