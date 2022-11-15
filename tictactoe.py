import random




######### Definitions #########

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
gameOn = True
numberOfGames, gamesPlayed = 1, 0
player1, player2, currentPlayer = 'Player 1', 'Player 2', ''
players = [player1, player2]
wins = [0, 0, None]




######### Game Functions #########

def displayBoard(board):
    print(board[0], board[1], board[2], sep='  ')
    print(board[3], board[4], board[5], sep='  ')
    print(board[6], board[7], board[8], sep='  ', end='\n\n')

def resetBoard():
    global board
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    print()

def playerNames():
    global player1, player2
    player1 = input('Enter your name: ')
    player2 = input('Enter your name: ')
    if player1 == '' or player2 == '':
        if player1 == '':
            player1 = 'Player 1'
        if player2 == '':
            player2 = 'Player 2'
    if player1 != '' or player2 != '':
        player1, player2 = player1.title(), player2.title()
        #Special Greetings
        if player1.upper() in ['TEE', 'TONII', 'ABUDU', 'GERVANZ'] or player2.upper() in ['TEE', 'TONII', 'ABUDU', 'GERVANZ']:
            if player1.upper() in ['TEE', 'TONII', 'ABUDU', 'GERVANZ']:
                player1 = 'My Lord'
            if player2.upper() in ['TEE', 'TONII', 'ABUDU', 'GERVANZ']:
                player2 = 'My Lord'
            print('Welcome, My Lord')    
    return player1, player2

def firstPlayer():
    global currentPlayer, player1, player2
    firstPlayerId = random.choice(players)
    if firstPlayerId == players[0]:
        currentPlayer = player1
    elif firstPlayerId == players[1]:
        currentPlayer = player2
    print (f'{currentPlayer} goes first')
    
def playerTurn(currentPlayer):
    print (f'{currentPlayer}\'s turn')
    position = int(input('Choose a position from 1-9: '))
    if board[position-1] != '-':
        position = int(input('Position already taken! Choose a position from 1-9, not taken:\n'))
        if board[position-1] != '-':
            print('Skipping turn!')
        if currentPlayer==player1:
            board[position-1]='X'
        elif currentPlayer==player2:
            board[position-1]='O'
    else:
        if currentPlayer==player1:
            board[position-1]='X'
        elif currentPlayer==player2:
            board[position-1]='O'
    displayBoard(board)

def switchPlayer():
    global currentPlayer
    if currentPlayer==player1:
        currentPlayer=player2
    elif currentPlayer==player2:
        currentPlayer=player1

def numberOfGamesToPlay():
    global numberOfGames
    numberOfGames = input('How many games do you wish to play: ')
    if numberOfGames == '':
        numberOfGames = 1
    else:
        numberOfGames = int(numberOfGames)
    print()




######### All The Checks - Win or Tie #########

def checkRows():
    global gameOn
    if board[0] == board[1] == board[2] != '-':
        gameOn = False
    elif board[3] == board[4] == board[5] != '-':
        gameOn = False
    elif board[6] == board[7] == board[8] != '-':
        gameOn = False

def checkColumns():
    global gameOn
    if board[0] == board[3] == board[6] != '-':
        gameOn = False
    elif board[1] == board[4] == board[7] != '-':
        gameOn = False
    elif board[2] == board[5] == board[8] != '-':
        gameOn = False

def checkDiags():
    global gameOn
    if board[0] == board[4] == board[8] != '-':
        gameOn = False
    elif board[2] == board[4] == board[6] != '-':
        gameOn = False

def checkWin():
    checkRows()
    checkColumns()
    checkDiags()
    if gameOn == False:
        wins[2] = 'Won'
        print('\n')
        print(f'----- !!! {currentPlayer.upper()} WON !!! -----\n')

def checkTie():
    global gameOn
    if gameOn == True:
        gameOn = False
        wins[2] = 'Tied'
        print ('-----  Tie -----')

def checkBoard():
    if '-' in board:
        checkWin()
    else:
        checkWin()
        checkTie()




######### Actual GamePlay #########

playerNames()
numberOfGamesToPlay()

while gamesPlayed != numberOfGames:
    firstPlayer()
    displayBoard(board)

    while gameOn:
        playerTurn(currentPlayer)
        checkBoard()
        switchPlayer()
        
    gamesPlayed+=1

    if wins[2] == 'Won':
        if currentPlayer == player1:
            wins[1] += 1
        elif currentPlayer == player2:
            wins[0] += 1
    elif wins[2] == 'Tied':
        wins[1] += 0
        wins[0] += 0

    gameOn = True
    
    resetBoard()

if numberOfGames > 1:
    print()
    print('- G A M E   S U M M A R Y -')
    if wins[0] == 1 or wins[1] == 1:
        if wins[0] == 1:
            print(f'{player1} won: {wins[0]} round')
        if wins[1] == 1:
            print(f'{player2} won: {wins[1]} round')
    if wins[0] != 1 or wins[1] != 1:
        if wins[0] != 1:
            print(f'{player1} won: {wins[0]} rounds')
        if wins[1] != 1:
            print(f'{player2} won: {wins[1]} rounds')
    print()
    if wins[0] > wins[1]:
        print(f'----- !!! {player1.upper()} IS THE ULTIMATE CHAMPION !!! -----\n')
    elif wins[0] < wins[1]:
        print(f'----- !!! {player2.upper()} IS THE ULTIMATE CHAMPION !!! -----\n')
    elif wins[0] == wins[1]:
        print('It seems you are both equally matched!\n')