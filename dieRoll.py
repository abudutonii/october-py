import random

rollnum = int(input('how many times do you want to roll? '))

frequencies = [0 for i in range(6)]

for i in range(rollnum):
    face = random.randrange(1,7)

    if face == 1:
        frequencies[0]+=1
    elif face == 2:
        frequencies[1]+=1
    elif face == 3:
        frequencies[2]+=1
    elif face == 4:
        frequencies[3]+=1
    elif face == 5:
        frequencies[4]+=1
    elif face == 6:
        frequencies[5]+=1

print(f'Face{"Frequency":>13}')
print(f'{1:>4}{frequencies[0]:>13}')
print(f'{2:>4}{frequencies[1]:>13}')
print(f'{3:>4}{frequencies[2]:>13}')
print(f'{4:>4}{frequencies[3]:>13}')
print(f'{5:>4}{frequencies[4]:>13}')
print(f'{6:>4}{frequencies[5]:>13}')

print(f'\nHighest: {max(frequencies)}\nLowest: {min(frequencies)}')