# --------------------------------Tuple-----------------------------------------------------

# 01. Create a tuple
# Create a tuple named fruits containing apple, banana, and mango. Print the tuple.
# Expected output: ("apple", "banana", "mango")

# fruits = ("apple", "banana", "mango")
# print(fruits)

# 02. Access an element
# Given the tuple below, print the second element.
# Input: (10, 20, 30, 40)
# Expected output: 20
# t = (10, 20, 30, 40)
# print(t[1])


# 03. Access the last element
# Print the last element of a tuple using negative indexing.
# Input: (5, 10, 15, 20, 25)
# Expected output: 25
# t = (5, 10, 15, 20, 25)
# print(t[-1])


# 4. Find the length
# Find and print the total number of elements in the tuple.
# Input: ("red", "blue", "green", "yellow")
# Expected output: 4

# t = ("red", "blue", "green", "yellow")
# print(len(t))


# 05. Check whether an item exists
# Check whether 30 is present in the tuple. Print Found if it exists; otherwise print Not Found.
# Input: (10, 20, 30, 40)
# Expected output: Found
# t = (10, 20, 30, 40)
# for i in t:
#     if i == 30:
#         print("Found")


# 06. Count an element
# Count how many times the number 2 appears in the tuple.
# Input: (2, 4, 2, 6, 2, 8)
# Expected output: 3

# t = (2, 4, 2, 6, 2, 8)
# print(t.count(2))


# 7. Find the index
# Find the index position of the word python in the tuple.
# Input: ("java", "python", "c", "html")
# Expected output: 1

# t = ("java", "python", "c", "html")
# print(t.index("python"))


# 08. Join two tuples
# Join the two given tuples and print the result.
# Input: (1, 2, 3) and (4, 5)
# Expected output: (1, 2, 3, 4, 5)

# t1 = (1, 2, 3)
# t2 = (4, 5)
# print(t1 + t2)

# 09. Repeat a tuple
# Repeat the tuple two times using the repetition operator.
# Input: ("Hi", "Hello")
# Expected output: ("Hi", "Hello", "Hi", "Hello")
# t = ("Hi", "Hello")
# print(t * 2)


# 10. Slice a tuple
# Print elements from index 1 up to, but not including, index 4.
# Input: (10, 20, 30, 40, 50, 60)
# Expected output: (20, 30, 40)

# t = (10, 20, 30, 40, 50, 60)
# print(t[1:4])

# 11. Reverse a tuple
# Print the tuple in reverse order using slicing.
# Input: (1, 2, 3, 4, 5)
# Expected output: (5, 4, 3, 2, 1)

# t = (1, 2, 3, 4, 5)
# print(t[::-1])

# 12. Find maximum and minimum
# Find and print the largest and smallest values in the tuple.
# Input: (14, 3, 27, 8, 19)
# Expected output: Maximum: 27; Minimum: 3

# t = (14, 3, 27, 8, 19)
# print("Maximum:", max(t))
# print("Minimum:", min(t))
#

# 13. Calculate the sum
# Find the sum of all numbers in the tuple.
# Input: (5, 10, 15, 20)
# Expected output: 50

# t = (5, 10, 15, 20)
# print(sum(t))
#

# 14. Convert a list into a tuple
# Convert the given list into a tuple and print the result.
# Input: [2, 4, 6, 8]
# Expected output: (2, 4, 6, 8)

# t = [2, 4, 6, 8]
# print(tuple(t))
#

# 15. Convert a tuple into a list
# Convert the given tuple into a list and print the result.
# Input: ("pen", "pencil", "eraser")
# Expected output: [pen, pencil, eraser]

# t = ("pen", "pencil", "eraser")
# print(list(t))
#

# 16. Unpack a tuple
# Unpack the tuple into variables a, b, and c. Print each variable on a separate line.
# Input: (100, 200, 300)
# Expected output: 100, 200, 300 on separate lines

# t = (100, 200, 300)
# for i in t:
#     print(i)


# 17. Create a single-element tuple
# Create a tuple containing only the number 7. Print the tuple and its type.
# Expected output: (7,) and tuple

# t = (7,)
# print(t)
# print(type(t))


# 18. Count even numbers
# Use a for loop to count how many even numbers are present in the tuple.
# Input: (3, 8, 12, 5, 7, 10)
# Expected output: 3
#
# t = (3, 8, 12, 5, 7, 10)
# count = 0
# for i in t:
#     if i % 2 == 0:
#         count += 1
# print(count)


# 19. Count positive and negative numbers
# Use a for loop and conditions to count positive and negative numbers. Ignore zero.
# Input: (-2, 5, 0, -7, 9, 4)
# Expected output: Positive: 3; Negative: 2
# t = (-2, 5, 0, -7, 9, 4)
# pc = 0
# nc = 0
# for i in t:
#     if i > 0:
#         pc += 1
#     elif i < 0:
#         nc += 1
# print("Positive:", pc)
# print("Negative:", nc)
#

# 20. Count values greater than 10
# Use a for loop to count how many tuple elements are greater than 10.
# Input: (4, 12, 18, 7, 10, 25)
# Expected output: 3
# t = (4, 12, 18, 7, 10, 25)
# c = 0
# for i in t:
#     if i > 10:
#         c += 1
# print(c)
#

# 21. Create a tuple of squares
# Create a new tuple containing the square of each number. Use a for loop and tuple conversion.
# Input: (2, 3, 4, 5)
# Expected output: (4, 9, 16, 25)
#
# t = (2, 3, 4, 5)
# t1 = ()
# for i in t:
#     t1 += (i**2,)
# print(t1)


# 22. Find repeated values
# Print each distinct value that appears more than once. Do not print a repeated value more than once.
# Input: (2, 4, 2, 5, 4, 7, 2)
# Expected output: 2 and 4
#
# 23. Compare two tuples
# Check whether two tuples contain the same elements in the same order.
# Input: (1, 2, 3) and (1, 2, 3)
# Expected output: Equal
#
# 24. Find the second largest distinct value
# Find the second-largest distinct number. Do not use sort() or sorted().
# Input: (12, 45, 23, 67, 45)
# Expected output: 45
