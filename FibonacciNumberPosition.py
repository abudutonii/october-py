position=int(input('enter position:\n\t'))

def FibonacciPosition(position):
    fib=[0, 1]
    
    for x in range(position):
       fib+=[(fib[-1] + fib[-2])]
    #    print(fib[x])
       
    print(fib[x])

FibonacciPosition(position)
