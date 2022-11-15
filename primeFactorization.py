number = int(input('Enter number: '))


def factors_of_number(number):

    factorsofnumber = []

    for i in range(number):
        if number%(i+1) == 0:
            factorsofnumber += [i+1]

    del factorsofnumber[0]
    return (factorsofnumber)



def is_prime(number):

    prime = []
    for i in range(1, number+1):
        if number%i==0:
            prime+=[i]
    if prime==[1,number]:
        return True
    else:
        return False


for i in factors_of_number(number):
    is_prime(i)
    if is_prime(i):
        print(i, end=" ")
print()