import random

times = int(input('How many flips? '))

H, T = 0, 0

for i in range(times):
    face = random.randrange(2)
    if face==0:
        # print('Heads')
        H += 1
    else:
        # print('Tails')
        T += 1

print(f'Heads = {H}\nTails = {T}')