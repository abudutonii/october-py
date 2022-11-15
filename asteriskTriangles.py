for x in range (10):
   print(f'{"*"*x:<10}')
a=11
for x in range (10):
   a-=1
   print(f'{"*"*a:<10}')
a=11
for x in range (10):
   a-=1
   print(f'{"*"*a:>10}')
for x in range (10):
   print(f'{"*"*x:>10}')

a=11
for x in range (10):
   a-=1
   print(f'{"*"*x:<10}\t{"*"*a:<10}\t{"*"*a:>10}\t{"*"*x:>10}')