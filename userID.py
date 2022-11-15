import random

letters = ['a', 'b', 'c','d', 'e', 'f', 'g', 'z']
generate_users = []

for i in range(8000):
    username = random.choice(letters).upper() + random.choice(letters).upper() + str(random.randrange(1,10)) + str(random.randrange(1,10))
    generate_users += [username]
generate_users.sort()

userIDs = []

for j in generate_users:
    if j not in userIDs:
        userIDs += [j]
userIDs.reverse()

print(f'Generated {len(userIDs)} unique IDs\n')
# print(userIDs) ##Uncomment to view IDs