radius = float(input('enter radius of circle:\n'))

pi = 22/7
diameter, circumference, area = (radius * 2), (2 * radius * pi), (pi * (radius**2))

def unitChoice(unitlength='mm'):
    unit = int(input("Choose your system of measurement:\n1. metric\n2.imperial \n"))

    if (unit == 1):
        unitlength = int(input("What unit of length do you wish to use?\n1. millimetres\n2. centimetres\n3. metres\n4. kilometres \n"))
        if unitlength == 1:
            unitlength = "millimetres"
        elif unitlength == 2:
            unitlength = "centimetres"
        elif unitlength == 3:
            unitlength = "metres"
        elif unitlength == 4:
            unitlength = "kilometres"
        else:
            print("Invalid input!")
    elif (unit ==2):
        unitlength = int(input("What unit of length do you wish to use?\n1. inches\n2. feet \n"))
        if unitlength == 1:
            unitlength = "inches"
        elif unitlength == 2:
            unitlength = "feet"
        else:
            print("Invalid input!")

    return unitlength

unitLength = unitChoice()

print(f'for a circle of radius; {radius} {unitLength}')
print(f'the diameter is {diameter} {unitLength}')
print(f'the circumference is {circumference} {unitLength}')
print(f'the area is {area} square {unitLength}')