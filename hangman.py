import random

def making_a_guess(guess, chosen_word, blank_list):
    correct_guess = False
    for index, letter in enumerate(chosen_word):
        if guess.lower() == letter:
            blank_list[index] = guess.lower()
            correct_guess = True
    return correct_guess

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]
chosen_word = list(random.choice(word_list))

blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)

update_display = 0

#----------------------------------------------------------------------------------------------

print(HANGMANPICS[update_display])
guess = input(f"Welcome to hangman.\n{blank}\nMake a guess? ")
correct_guess = making_a_guess(guess, chosen_word, blank_list)

if not correct_guess:
    update_display += 1

print(HANGMANPICS[update_display])
print(''.join(blank_list))

while update_display < 6:
    if blank_list == chosen_word:
        print("YOU WIN!")
        break
    guess = input("Make another guess? ")
    correct_guess = making_a_guess(guess, chosen_word, blank_list)
    
    if not correct_guess:
        update_display += 1
    
    print(HANGMANPICS[update_display])
    print(''.join(blank_list))

if update_display == 6:
    print("GAME OVER.")
