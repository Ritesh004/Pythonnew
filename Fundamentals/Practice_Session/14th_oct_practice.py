i = 1
while i <= 4:
    j = 1
    while j <= 4:
        print("*", end=" ")
        j += 1
    print()
    i += 1


i = 1
while i <= 4:
    j = 1
    while j <= 4:
        print(1, end=" ")
        j += 1
    print()
    i += 1


i = 1
while i <= 4:
    j = 1
    while j <= 4:
        print(i, end=" ")
        j += 1
    print()
    i += 1

i = 1
while i <= 4:
    j = 1
    while j <= 4:
        print(j, end=" ")
        j += 1
    print()
    i += 1


i = 1
while i <= 4:
    j = i
    while j <= 4:
        print("*", end=" ")
        j += 1
    print()
    i += 1


i = 1
while i <= 4:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

i = 1
while i <= 4:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1

i = 1
while i <= 4:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()
    i += 1

i = 1
while i <= 4:
    j = 1
    while j <= 5 - i:
        print(j, end=" ")
        j += 1
    print()
    i += 1

for i in range(1, 5):
    n = 1
    for j in range(1, i + 1):
        print(n, end=" ")
        n = n + 2
    print()

for i in range(1, 5):
    n = 2
    for j in range(1, i + 1):
        print(n, end=" ")
        n = n + 2
    print()

for i in range(1, 5):
    a = 65
    for j in range(i):
        print(chr(a), end=" ")
        a = a + 1
    print()

for i in range(4):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()


for i in range(4, -1, -1):
    a = 65
    for j in range(i):
        print(chr(a), end=" ")
        a = a + 1
    print()

for i in range(3):
    for j in range(5):
        print("*", end=" ")
    print()

for i in range(3):
    n = 1
    for j in range(5):
        print(n, end=" ")
        n += 1
    print()

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print(1, end=" ")
        else:
            print(" ", end=" ")
    print()

n = 1
for i in range(1, 5):
    for j in range(i):
        print(n, end=" ")
        n += 1
    print()

for i in range(4, -1, -1):
    for j in range(i):
        print(i, end=" ")
    print()


for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
