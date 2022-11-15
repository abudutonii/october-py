args = input('enter numbers to multiply, divded by spaces: ')
args = args.split()



def product(*args):
    product_of_numbers = 1
    for i in args:
        product_of_numbers *= float(i)
    return product_of_numbers

print(product(*args))