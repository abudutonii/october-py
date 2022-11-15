numberToLoop =int(input('enter a number to check:\n'))
showLoopValues = input('show loop values? y/n\n')

def loop421(numberToLoop):
    count=0
    numberToLoopValues=[numberToLoop]

    while (numberToLoop!=1.) or (numberToLoop!=1):
        count += 1

        if numberToLoop%2==0:
            numberToLoop/=2
            print('halved =', int(numberToLoop))
        elif numberToLoop%2==1:
            numberToLoop=(3*numberToLoop)+1
            print('tripled, plus 1 =', int(numberToLoop))

        numberToLoopValues+=[int(numberToLoop)]

    print()
    print(f'looped: {count} times')
    if showLoopValues.lower() == 'y':
        print(numberToLoopValues)

print()
loop421(numberToLoop)