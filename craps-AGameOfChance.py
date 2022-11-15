import random

def rolldice():
    die1, die2 = random.randrange(1,7), random.randrange(1,7)
    return (die1, die2)

def dispDice(dice):
    die1, die2 = dice
    print(f'Rolled {die1} + {die2} = {sum(dice)}')

dieValues = rolldice()
dispDice(dieValues)
gameStatus = ''

if sum(dieValues)==7 or sum(dieValues)==11:
    print('Win!')
    gameStatus = 'Won'
elif sum(dieValues)==2 or sum(dieValues)==3 or sum(dieValues)==12:
    print('Craps! You Lose!')
    gameStatus = 'Lost'
else:
    point=sum(dieValues)
    print(f'Point is {point}')
    gameStatus = 'Continue'
    while gameStatus == 'Continue':
        rolldice()
        dispDice(dieValues)
        if sum(dieValues) == point:
            print('Win!')
            gameStatus = 'Won'
        elif sum(dieValues) == 7 or sum(dieValues)==2 or sum(dieValues)==3 or sum(dieValues)==12:
            print('Craps! You Lose!')
            gameStatus = 'Lost'
        else:
            dispDice(dieValues)
            gameStatus = 'Continue'
