length1 = int(input('enter length 1:\n'))
length2 = int(input('enter length 2:\n'))
length3 = int(input('enter length 3:\n'))
triangleSides = length1, length2, length3

def is_triangle():
    a, b, c = triangleSides
    if a+b<=c or b+c<=a or a+c<=b:
        return False
    return True

def is_right_angled():
    a, b, c = triangleSides
    if not is_triangle():
        return False
    if a>a and a>b:
        return (a**2) == (b**2) + (c**2)
    if b>a and b>c:
        return (b**2) == (a**2) + (c**2)
    if c>a and c>b:
        return (c**2) == (a**2) + (b**2)

def triangleType():
    if is_triangle():
        if length1==length2==length3:
            print('\nthe triangle is equilateral')
        elif (length1==length2 and length2!=length3) or (length1==length3 and length2!=length3) or\
            (length2==length3 and length1!=length3):
            print('\nthe triangle is isoceles')
        else:
            print('\nthe triangle is scalene')
    else:
        print('\nnot a triangle!')
    
    if is_right_angled():
        print('it is also right-angled!')

def trianglePerimeter():
    return sum(triangleSides)

def triangleArea():
    a, b, c = triangleSides
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**.5

def print_triangle_details():
    if is_triangle():
        print()
        print(f'{"perimeter":<10} = {trianglePerimeter()}')
        print(f'{"area":<10} = {triangleArea():.2f}')

triangleType()
print_triangle_details()
