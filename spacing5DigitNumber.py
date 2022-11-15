fivedigit = int(input("enter a five-digit integer: "))

if (fivedigit>=9999) and (fivedigit<=100000):
    print("\nprocessing...")
else:
    print("wrong input")
    quit()

# first = fivedigit//10000
# second = (fivedigit//1000)%10
# third = (fivedigit//100)%100%10
# fourth = (fivedigit//10)%1000%100%10
# fifth = (fivedigit//1)%10000%1000%100%10

for i in str(fivedigit):
    print(i, end='\t')