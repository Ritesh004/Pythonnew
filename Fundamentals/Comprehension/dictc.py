# Syntax Dictionary comprehension
#
# new_dict={key_expression: vale_expression for item in iterable}
#
# syntax with condition
#
# new_dict={key:value for item in iterable if cndition}
#

# num = [1, 2, 3, 4, 5]
# r = {i: i * i for i in num}
# print(r)


# create a dict of num with their cubes

# num = [1, 2, 3, 4, 5]
# r = {i: i**3 for i in num}
# print(r)


# create a dict of even num
#
# num = [1, 2, 3, 4, 5, 6, 7, 8]
# r = {i: i for i in num if i % 2 == 0}
# print(r)


# create dict of names and their length

# name = ["Amit", "Rahul", "Sneha"]
# r = {i: len(i) for i in name}
# print(r)
#


# filter students with more than 50 marks

# marks = {"Amit": 85, "Rahul": 45, "Sneha": 90, "Priya": 35}
# r = {i: e for i, e in marks.items() if e > 50}
# print(r)


# convert dict values into squares

dict = {"A": 2, "B": 3, "C": 4}
r = {i: e**2 for i, e in dict.items()}
print(r)
