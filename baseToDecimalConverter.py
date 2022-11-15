baseInput = input('enter number to be converted:\n')
baseNumber = int(input('enter base number:\n'))

def baseConveter(baseInput, baseNumber):
    baseList = []
    baseListConverted = []

    for i in baseInput:
        if i.lower() == 'a':
            baseList += [10]
        elif i.lower() == 'b':
            baseList += [11]
        elif i.lower() == 'c':
            baseList += [12]
        elif i.lower() == 'd':
            baseList += [13]
        elif i.lower() == 'e':
            baseList += [14]
        elif i.lower() == 'f':
            baseList += [15]
        else:
            baseList += [int(i)]

    for x in baseList:
        if x>=baseNumber:
            print('invalid input!')
            quit()

    pos= -1
    for x in baseList[::-1]:
        pos += 1
        x = int(x)
        baseListConverted += [x*(baseNumber**pos)]

    print (f'= {sum(baseListConverted)} (base10)')

baseConveter(baseInput, baseNumber)