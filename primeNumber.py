def is_prime(num):
    
    prime = []
    for i in range(1, num+1):
        if num%i==0:
            prime+=[i]
    if prime==[1,num]:
        return True
    else:
        return False


for i in range(1, 205):
	if is_prime(i + 1):
		print(i + 1, end="\n")
print()