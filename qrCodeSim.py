import random



for i in range(15):
    for j in range(15):
        j = random.randrange(1,3)
        if j==1:
            print('O', end=' ')
        else:
            print(' ', end=' ')
    print('')