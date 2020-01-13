friends = [1,2,3,4,5];
enemy = ["a","b","c","d","e"]

for f,x in zip(friends, enemy):
    print("friend",f,"enemy",x)

""" 
friend 1 enemy a
friend 2 enemy b
friend 3 enemy c
friend 4 enemy d
friend 5 enemy e 
"""

friends = [1,2,3,4,5];
enemy = ["a","b","c","d"]

for f,x in zip(friends, enemy):
    print("friend",f,"enemy",x)

""" 
friend 1 enemy a
friend 2 enemy b
friend 3 enemy c
friend 4 enemy d 
"""

n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff")

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')