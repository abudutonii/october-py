'''In number theory, a perfect number is a positive integer that is equal to the sum of its divisors.'''

number = int(input('enter a number:\n\t'))

x=0
div=[]
while x!=number and x<number:
   x+=1
   if number%x==0:
       div+=[x]
div.pop()
if sum(div)==number:
   print(div, 'sums up to', sum(div))
   print('you entered a perfect number')
else:
   print('sike! not a perfect number')