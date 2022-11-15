number = int(input("enter an integer: \n\t"))

def oddOrEven(number):
    test = (number%2)

    if (test == 0):
        print("the integer is even")
    else:
        print("the integer is odd")

oddOrEven(number)