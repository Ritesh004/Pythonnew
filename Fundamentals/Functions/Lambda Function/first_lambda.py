# lambda function
#
#
# add = lambda a, b: a + b
# result = add(10, 20)
# print(result)


# abc = lambda a, b: max(a, b)
# result = abc(15, 25)
# print(result)


# maximum = lambda a, b: a if a > b else b
# print(maximum(15, 25))


# find the len of string

# abc = lambda a: len(a)
# print(abc("python"))


# check num whether is positive negative or zero

# abc = lambda a: "positive" if a > 0 else "negative" if a < 0 else "zero"
# print(abc(-10))

# find the sum of digits of num

# add = lambda a: sum(int(d) for d in str(a))
# print(add(12345))


# check the num is divisibal by 3 and 5


# abc = lambda a: "yes" if a % 3 == 0 and a % 5 == 0 else "No"
# print(abc(15))


# find the string is pallindrome or not

# abc = lambda a: "pallindrome" if a[::-1] == a else "Not pallindrome"
# print(abc("madam"))


# count vowels from string

# abc = lambda a: sum(1 for i in a.lower() if i in "aeiou")
# print(abc("programming"))


# find second largest number from list

abc = lambda a: max(i for i in a if i != max(a))
print(abc([10, 20, 40, 30, 50]))
