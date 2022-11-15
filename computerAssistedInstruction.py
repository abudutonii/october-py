import random



how_many = int(input('How many questions? '))
test_type = input(f'\nWhat type of test would you like to take?\n1. (A)ddition\n2. (S)ubtraction\n3. (M)ultiplication\n4. (D)ivision\n5. (R)andom\n- ')
difficulty = input('\nDifficulty level\n1. Level 1\n2. Level 2\n- ')
score_type = input('\n1. (R)apid Fire Mode (Scored)\n2. (Z)en Mode (Unscored)\n- ')
count, right = 0, 0



def feedback(grey):
    feedback_right = ['Very Good!', 'Nice Work!', 'Keep it up!']
    feedback_nright = [['No.', 'Wrong.'], ['Please try again!', 'Keep Trying!', 'Try once more!']]

    if grey == 'right':
        print(f'{random.choice(feedback_right)}\n')
    if grey == 'nright0':
        print(f'{random.choice(feedback_nright[0])}')
    if grey == 'nright1':
        print(f'{random.choice(feedback_nright[0])} {random.choice(feedback_nright[1])}')

def declareNumber(count):
    print(f'\n-- Number {count+1} --')



def AdditionTest(difficulty, score_type):
    global right

    if int(difficulty)==1:
        x = random.randrange(1, 10)
        y = random.randrange(1, 10)
    elif int(difficulty)==2:
        x = random.randrange(1, 100)
        y = random.randrange(1, 100)

    if int(score_type)==1 or score_type.casefold()=='r' or score_type.casefold()=='s':
        question = int(input(f'What is {x} + {y}? '))
        if question == (x+y):
            feedback('right')
            right += 1
        elif question != (x+y):
            feedback('nright0')
            print(f'Correct answer: {x+y}')

    elif int(score_type)==2 or score_type.casefold()=='z' or score_type.casefold()=='u':
        question = int(input(f'What is {x} + {y}? '))
        if question == (x+y):
            feedback('right')
        else:
            while question != (x+y):
                feedback('nright1')
                question = int(input(f'What is {x} + {y}? '))
                if question == (x+y):
                    feedback('right')

def SubtractionTest(difficulty, score_type):
    global right

    if int(difficulty)==1:
        x = random.randrange(1, 10)
        y = random.randrange(1, 10)
        if x<y:
            x, y = y, x
    elif int(difficulty)==2:
        x = random.randrange(1, 100)
        y = random.randrange(1, 100)

    if int(score_type)==1 or score_type.casefold()=='r' or score_type.casefold()=='s':
        question = int(input(f'What is {x} - {y}? '))
        if question == (x-y):
            feedback('right')
            right += 1
        elif question != (x-y):
            feedback('nright0')
            print(f'Correct answer: {x-y}')

    elif int(score_type)==2 or score_type.casefold()=='z' or score_type.casefold()=='u':
        question = int(input(f'What is {x} - {y}? '))
        if question == (x-y):
            feedback('right')
        else:
            while question != (x-y):
                feedback('nright1')
                question = int(input(f'What is {x} - {y}? '))
                if question == (x-y):
                    feedback('right')

def MultiplicationTest(difficulty, score_type):
    global right

    if int(difficulty)==1:
        x = random.randrange(2, 10)
        y = random.randrange(2, 10)
    elif int(difficulty)==2:
        x = random.randrange(2, 100)
        y = random.randrange(2, 100)

    if int(score_type)==1 or score_type.casefold()=='r' or score_type.casefold()=='s':
        question = int(input(f'What is {x} x {y}? '))
        if question == (x*y):
            feedback('right')
            right += 1
        elif question != (x*y):
            feedback('nright0')
            print(f'Correct answer: {x*y}')

    elif int(score_type)==2 or score_type.casefold()=='z' or score_type.casefold()=='u':
        question = int(input(f'What is {x} x {y}? '))
        if question == (x*y):
            feedback('right')
        else:
            while question != (x*y):
                feedback('nright1')
                question = int(input(f'What is {x} x {y}? '))
                if question == (x*y):
                    feedback('right')

def DivisionTest(difficulty, score_type):
    global right

    if int(difficulty)==1:
        x = random.randrange(1, 10)
        y = random.randrange(1, 10)
        while x%y!=0 or x/y==1 or x/y==x:
            x = random.randrange(1, 10)
            y = random.randrange(1, 10)
    elif int(difficulty)==2:
        x = random.randrange(1, 100)
        y = random.randrange(1, 100)
        while x%y!=0 or x/y==1 or x/y==x:
            x = random.randrange(1, 100)
            y = random.randrange(1, 100)

    if int(score_type)==1 or score_type.casefold()=='r' or score_type.casefold()=='s':
        question = float(input(f'What is {x} / {y}? '))
        if question == (x/y):
            feedback('right')
            right += 1
        elif question != (x/y):
            feedback('nright0')
            print(f'Correct answer: {x/y}')

    elif int(score_type)==2 or score_type.casefold()=='z' or score_type.casefold()=='u':
        question = float(input(f'What is {x} / {y}? '))
        if question == (x/y):
            feedback('right')
        else:
            while question != (x/y):
                feedback('nright1')
                question = float(input(f'What is {x} / {y}? '))
                if question == (x/y):
                    feedback('right')

def RandomTest(difficulty, score_type):
    global right

    testType = random.randrange(1,4)
    if testType == 1:
        AdditionTest(difficulty, score_type)
    elif testType == 2:
        SubtractionTest(difficulty, score_type)
    elif testType == 3:
        MultiplicationTest(difficulty, score_type)
    elif testType == 4:
        DivisionTest(difficulty, score_type)



def score(right, how_many):
    percentage = (right/how_many)*100
    scoremessageA = [['Damn.', 'Splendid.', 'Brilliant.'], ['That\'s really great!', 'Wonderful work!', 'Brilliant work!']]
    scoremessageB = [['Wow.', 'Cool.'], ['That\'s Great!', 'Wonderful!', 'Beautiful!']]
    scoremessageC = [['Sheesh.', 'Bruh.'], ['That\'s not so good!', 'You can do better!', 'Please try harder next time!']]
    
    if percentage >= 70:
        print(f'You got {right} out of {how_many}! That\'s {percentage}%!\n{random.choice(scoremessageA[0])} {random.choice(scoremessageA[1])}')
    elif 35 <= percentage < 70:
        print(f'You got {right} out of {how_many}! That\'s {percentage}%!\n{random.choice(scoremessageB[0])} {random.choice(scoremessageB[1])}')
    elif percentage < 35:
        print(f'You got {right} out of {how_many}! That\'s {percentage}%!\n{random.choice(scoremessageC[0])} {random.choice(scoremessageC[1])}')



while count<how_many:

    declareNumber(count)

    if int(test_type) == 1 or test_type.casefold()=='a':
        AdditionTest(difficulty, score_type)
    elif int(test_type) == 2 or test_type.casefold()=='s':
        SubtractionTest(difficulty, score_type)
    elif int(test_type) == 3 or test_type.casefold()=='m':
        MultiplicationTest(difficulty, score_type)
    elif int(test_type) == 4 or test_type.casefold()=='d':
        DivisionTest(difficulty, score_type)
    elif int(test_type) == 5 or test_type.casefold()=='r':
        RandomTest(difficulty, score_type)
    
    count += 1



if int(score_type)==1 or score_type.casefold()=='r' or score_type.casefold()=='s':
    score(right, how_many)