s = input('enter text:\n')



countVows, countCons, countSpcs, countNums, countChar = 0, 0, 0, 0, 0



for i in s:
    if i.lower() in 'aeiou':
        countVows += 1
    elif i.lower() in 'bcdfghjklmnpqrstvwxyz':
        countCons += 1
    elif i == ' ':
        countSpcs += 1
    elif i in '1234567890':
        countNums += 1
    else:
        countChar += 1



print(f'''
there are {len(s)} characters in \'{s}\'
- {countVows} vowels, {countCons} consonants, {countNums} digits, {countSpcs} spaces and {countChar} other characters
''')