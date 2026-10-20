# a
x = 0
while x < 15:
    x += 3
    print(x)

print("-"*50)

for x in range(3, 16, 3):
    print(x)

print("-"*50)

# b
k = 22
while k > 10:
    k -= 2
    print(k)

print("-"*50)

for k in range(20, 9, -2):
    print(k)

print("-"*50)

# c 
mot = "boucle"
for i in range(len(mot)):
    print(i, mot[i])

print("-"*50)

i = 0
while i < len(mot):
    print(i, mot[i])
    i += 1