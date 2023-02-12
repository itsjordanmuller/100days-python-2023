import random

result = ['''
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
      
 YOU FELL DOWN

  YOU  LOSE

      O
     /|\ 
     / \ 

==============
''', '''

 YOU MADE IT
 DOWN SAFELY

   YOU WIN

      O
     /|\ 
     / \ 
==============
''']

stages = ['''
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

==============
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

==============
''', '''
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
   \ /   /
    \   /
     \O/
     /|\ 
     / \ 

==============
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

==============
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

==============
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

==============
''']

stages = stages[::-1]

word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]

chosen_word = random.choice(word_list)
# print(chosen_word)

display = ["_"] * len(chosen_word)
print(display)

# while "_" in display:
#     guess = input("Choose a single letter: ").lower()
#     for i, letter in enumerate(chosen_word):
#         if letter == guess:
#             display[i] = letter
#     print(display)
# print("Game over, you won!")

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

lives = 6

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

while "_" in display and lives > 0:
    print(stages[6-lives])
    guess = input("Choose a single letter: ").lower()
    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left.")
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
    print(display)

if lives == 0:
    print(result[0])
else:
    print(result[1])

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.