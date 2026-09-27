i = 1
while i <= 10:
    j = 1
    n = i
    count = 0
    while j <= i:
        if n % j == 0:
            count = count + 1
        j = j + 1

    if count == 2:
        print(i)
    i = i + 1
