from random import choice
import random
from words import word_list

word = random.choice(word_list)


# def get_word():
#     word = random.choice(word_list)
#     return word.upper()


guessed = []
wrong = []

tries = 7

while tries > 0:

    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + ' _ '
    if out == word:
        break

    print('Guess Letter:', out)
    print(tries, 'chances left')
    guess = input()

    if guess in guessed or guess in wrong:
        print('Correct Guess!', guess)
    elif guess in word:
        print('yes')
        guessed.append(guess)
    else:
        print('Incorrect! Try Again!')
        tries = tries-1
        wrong.append(guess)

    print()

if tries:
    print('you guessed', word)
else:
    print('You ran out of lives! Word was', word)
