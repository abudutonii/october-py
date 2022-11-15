import random



print('''
Guess a letter. Each correctly guessed letter shows all positions in empty puzzle.
You have 6 wrong tries. Enter "help" or "hint" for hints.
''')

complete = {
    'i am inevitable' : 'MCU quote',
    'i am iron-man' : 'MCU quote',
    'the quick brown fox jumps over the lazy dog' : 'All the letters',
    'i want it that way' : '\'90s song by The Backstreet Boys',
    'i have a dream!' : 'World Speech',
    'one small step for man, one giant leap for mankind' : 'On the Moon',
    'spongebob squarepants' : 'Nickelodeon Character',
    'romeo and juliet' : 'Famous fictional couple',
    'every action has an equal and opposite reaction' : 'Newton\'s Law',
    'william shakespeare' : 'The Bard',
    'mickey mouse' : 'Walt Disney'
}

answer, hint = [x for x in complete.keys()], [y for y in complete.values()]
hangman = random.choice(answer).casefold()
puzzle = []
guessed = []
game_status = 'On'.casefold()
failcount = 0



for i in hangman:
    if i.casefold() in 'qwertyuiopasdfghjklzxcvbnm':
        puzzle += '_'
    else:
        puzzle += i

print (''.join(puzzle))



def guess(guessed, puzzle):
    global failcount

    guessedLetter = input('\nGuess Letter: ')
    if guessedLetter.casefold() == 'hint' or guessedLetter.casefold() == help:
        hints(hangman)
        guessedLetter = input('\nGuess Letter: ')
    
    indices = []
    for a, b in enumerate(hangman):
        if b == guessedLetter.casefold():
            indices += [a]

    for i in indices:
        puzzle[i] = guessedLetter.capitalize()
    
    if guessedLetter.casefold() not in hangman:
        print('Oops!')
        failcount += 1
    
    guessed += [guessedLetter.capitalize()]

    return guessed, puzzle



def hints(hangman):
    print(f'Hint: {complete[hangman]}')



while '_' in puzzle:
    guess(guessed, puzzle)
    print(''.join(puzzle))
    if failcount == 1:
        print(f'Guessed: {", ".join(guessed).strip()} ({failcount} error)')
    elif failcount > 1:
        print(f'Guessed: {", ".join(guessed).strip()} ({failcount} errors)')

    if failcount == 6:
        print('\nHangman! You Lose!')
        game_status = 'lost'.casefold()
        break
game_status = 'won'.casefold()
print('\nYOU WON !!!')