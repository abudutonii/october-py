numbers = [i+1 for i in range(9)]

print(f'{"Number":>6}{"Square":>9}{"Cube":>10}')
for j in numbers:
    print(f'{j:>6}{j**2:>9} {j**3:>9}')