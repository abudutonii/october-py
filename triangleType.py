length1 = int(input('enter length 1:\n'))
length2 = int(input('enter length 2:\n'))
length3 = int(input('enter length 3:\n'))

def triangleType(length1, length2, length3):
    if length1==length2==length3:
        print('the triangle is equilateral')
    elif length1==length2 and length2!=length3:
        print('the triangle is isoceles')
    elif length1==length3 and length2!=length3:
        print('the triangle is isoceles')
    elif length2==length3 and length1!=length3:
        print('the triangle is isoceles')
    else:
        print('the triangle is scalene')

triangleType(length1, length2, length3)