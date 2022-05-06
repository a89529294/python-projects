import random
import string

print('H A N G M A N')
mode = 'init'
won = 0
lost = 0

while mode != 'exit':
    mode = input(
        'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    print()
    choice = random.choice(['python', 'swift', 'java', 'javascript'])
    attempts = 8
    correct_guesses = set()
    incorrect_guesses = set()
    if mode == 'play':
        while attempts:
            mask = ''
            for x in choice:
                if x in correct_guesses:
                    mask += x
                else:
                    mask += '-'
            print(mask)

            if mask == choice:
                print(f'You guessed the word {choice}!')
                print('You survived!')
                won += 1
                break

            letter = input('Input a letter:')
            if len(letter) != 1:
                print('Please, input a single letter.')
            elif letter not in string.ascii_lowercase:
                print('Please, enter a lowercase letter from the English alphabet.')
            elif letter in choice:
                if letter in correct_guesses:
                    print('You\'ve already guessed this letter.')
                else:
                    correct_guesses.add(letter)
            else:
                if letter in incorrect_guesses:
                    print('You\'ve already guessed this letter.')
                else:
                    incorrect_guesses.add(letter)
                    print('That letter doesn\'t appear in the word.')
                    attempts -= 1
            print()
        if attempts == 0:
            print('You lost!')
            lost += 1

    elif mode == 'results':
        print(f'You won: {won} times.')
        print(f'You lost: {lost} times.')
    elif mode == 'exit':
        break
