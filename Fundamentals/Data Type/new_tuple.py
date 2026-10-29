# Tuple - Immutable and ordered                  26th Oct 2026
#
# numbers = (10, 20, 30, 40)
# Text = ("Python", "Java")
# mixed = (10, 20, "Python", True, 30)
# print(numbers)
# print(Text)
# print(mixed)
# print(type(numbers))


# Tuple declaration

# a = ()
# print(a)
#
# b = (10,)
# print(b)
#
# c = (10, 20, 30.3)
# print(c)


# using Tuple function
#
# a = tuple("Python")
# print(a)

# Indexing-- supports positive and negative indexing
# a = ("A", "B", "C", "D")
# print("Positive indexing")
# print(a[0])
# print(a[1])
# print(a[2])
#
# print("Negative indexing")
# print(a[-1])
# print(a[-2])
# print(a[-3])


# Slicing

# a = (10, 20, 30, 40, 50, 60)
# print(a[0:4])
# print(a[3:5])
# print(a[:6])
# print(a[3:])
# print(a[::2])
# print(a[::-1])


# Concatination

# a = (10, 20)
# b = (30, 40)
# print(a + b)

# Repetation

# a = (1, 2)
# print(a * 2)


# Membership

# a = (10, 20, 30)
# b = 20
# print(b in a)
# print(b not in a)


# Important Function of Tuple

# a = (10, 20, 30, 40, 10, 10, 30, 20, 10)
# print(a.count(10))

# index function
# prints first occurance of data
# print(a.index(30))

# print(max(a))
# print(min(a))
# print(len(a))
# print(sum(a))


# Python Tuple
#
# 1. Write a Python program to create a tuple of five numbers and print it.
#
# Input: 10, 20, 30, 40, 50
#
# 2. Write a Python program to create a tuple of five student names and print it.
#
# Input: "Amit", "Priya", "Rahul", "Sneha", "Rohit"
#
# 3. Write a Python program to create an empty tuple and print its type.
#
# Input: ()
#
# 4. Write a Python program to create a tuple containing only one item and print its type.
#
# Input: 10
#
# 5. Write a Python program to create a tuple without using parentheses and print it.
#
# Input: 10, 20, 30, 40
#
# 6. Write a Python program to convert the string "Python" into a tuple.
#
# Input: "Python"
#
# 7. Write a Python program to access the first and last elements of a tuple.
#
# Input: (10, 20, 30, 40, 50)
#
# 8. Write a Python program to access the third element of a tuple using positive indexing.
#
# Input: (100, 200, 300, 400, 500)
#
# 9. Write a Python program to access the last element of a tuple using negative indexing.
#
# Input: (5, 10, 15, 20, 25)
#
# 10. Write a Python program to print the first three elements of a tuple using slicing.
#
# Input: (10, 20, 30, 40, 50, 60)
#
# 11. Write a Python program to print the last three elements of a tuple using slicing.
#
# Input: (10, 20, 30, 40, 50, 60)
#
# 12. Write a Python program to reverse a tuple using slicing.
#
# Input: (1, 2, 3, 4, 5)
#
# 13. Write a Python program to print every second element of a tuple using slicing.
#
# Input: (10, 20, 30, 40, 50, 60)
#
# 14. Write a Python program to concatenate two tuples using the + operator.
#
# Input: tuple1 = (1, 2, 3)
#
# tuple2 = (4, 5, 6)
#
# 15. Write a Python program to repeat a tuple three times using the * operator.
#
# Input: (1, 2)
#
# 16. Write a Python program to check whether 20 exists in a tuple using the in operator.
#
# Input: (10, 20, 30, 40, 50)
#
# 17. Write a Python program to check whether 50 does not exist in a tuple using the not in operator.
#
# Input: (10, 20, 30, 40)
#
# 18. Write a Python program to find the length of a tuple using len().
#
# Input: (10, 20, 30, 40, 50)
#
# 19. Write a Python program to count how many times 10 appears in a tuple using count().
#
# Input: (10, 20, 10, 30, 10, 40)
#
# 20. Write a Python program to find the index of 30 in a tuple using index().
#
# Input: (10, 20, 30, 40, 50)
#
# 21. Write a Python program to find the minimum value in a tuple using min().
#
# Input: (45, 12, 78, 5, 34)
#
# 22. Write a Python program to find the maximum value in a tuple using max().
#
# Input: (45, 12, 78, 5, 34)
#
# 23. Write a Python program to calculate the sum of all numbers in a tuple using sum().
#
# Input: (10, 20, 30, 40, 50)
#
# 24. Write a Python program to create a tuple containing integers, strings, and Boolean values, then print the tuple and its data type.
#
# Input: 10, "Python", True, 25, "Java"
#
# 25. Write a Python program to print the first, middle, and last elements of a tuple using indexing.
#
# Input: (10, 20, 30, 40, 50)


# a = (10, 20, 30, 40)
# temp = list(a)
# temp.append(50)
# print(tuple(temp))


# Logical questions:


# num = (10, 20, 30, 40)
# temp = list(num)
# temp.append(50)
# print(tuple(temp))
# num = temp
# print(tuple(num))


# n = (12, 7, 8, 15, 20, 33)
# even = 0
# odd = 0
# for i in n:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even:", even)
# print("Odd:", odd)


# Find sum of numbers divisibel by 3
# n = (3, 10, 12, 17, 21, 25, 30)
# sum = 0
# for i in n:
#     if i % 3 == 0:
#         sum += i
# print("Sum of num divisible by 3 is:", sum)


# count how many numbers are greater than avg of tuple

# n = (10, 20, 30, 40, 50)
# count = 0
# avg = sum(n) / len(n)
# for i in n:
#     if i > avg:
#         count += 1
# print("Count of num greater than avg of tuple is:", count)


# Create a new tuple with only positive num

# n = (-5, 10, -2, 20, 0, 15)
# a = ()
# for i in n:
#     if i >= 0:
#         a += (i,)
# print(tuple(a))


# count how many times a given element appers in a tuple without using count()

# n = (10, 20, 10, 30, 10, 40)
# count = 0
# target = 10
# for i in n:
#     if i == target:
#         count += 1
# print("Count:", count)


# n = (10, 15, 20, 25, 30, 33, 40)
# for i in n:
#     if i % 2 == 0 and i % 5 == 0:
#         print(i, end=" ")
#


# 1. Write a program to find the sum of numbers at even index positions in a tuple.
#
# Input:
# numbers = (12, 25, 34, 47, 56, 69)
#
#
#
# Output:
# Sum: 102
#
#
# 2. Write a program to create a new tuple containing numbers greater than 25 and less than 70.
#
# Input:
# numbers = (10, 35, 75, 45, 20, 60, 80)
#
#
#
# Output:
# (35, 45, 60)
#
#
# 3. Write a program to find the difference between the sum of positive numbers and the sum of negative numbers in a tuple.
#
# Input:
# numbers = (10, -5, 20, -15, 30, -10)
#
#
#
# Output:
# Difference: 70
#
#
# 4. Write a program to check whether all elements in a tuple are unique.
#
# Input:
# numbers = (10, 20, 30, 40, 50)
#
#
#
# Output:
# All elements are unique
#
#
# 5. Write a program to create a tuple containing only the elements at odd index positions.
#
# Input:
# numbers = (11, 22, 33, 44, 55, 66, 77)
#
#
#
# Output:
# (22, 44, 66)
#
#
# 6. Write a program to find the sum of digits of every number in a tuple and print each number with its digit sum.
#
# Input:
# numbers = (12, 34, 56, 78)
#
#
#
# Output:
# 12 3
# 34 7
# 56 11
# 78 15
#
#
# 7. Write a program to find all pairs of elements in a tuple whose sum is equal to 10.
#
# Input:
# numbers = (2, 8, 3, 7, 4, 6, 5)
#
#
#
# Output:
# (2, 8)
# (3, 7)
# (4, 6)
#
#
# 8. Write a program to find the difference between the largest and smallest elements without using max() or min().
#
# Input:
# numbers = (34, 12, 67, 25, 9, 48)
#
#
#
# Output:
# Difference: 58
#
#
# 9. Write a program to create a new tuple containing numbers that appear more than once in the original tuple, without repeating them in the result.
#
# Input:
# numbers = (10, 20, 30, 20, 40, 10, 50, 30)
#
#
#
# Output:
# (10, 20, 30)
#
#
# 10. Write a program to check whether a tuple is sorted in ascending order.
#
# Input:
# numbers = (10, 20, 30, 45, 60)
#
#
#
# Output:
# Tuple is sorted in ascending order


# words = ("apple", "banana", "grapes", "orange")
# count = 0
# for i in words:
#     for j in i:
#         if j in "aeiou":
#             count += 1
# print(count)


words = ("python", "programmings", "code", "development")
