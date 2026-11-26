# def abc():
#     print("Hello! Hi")
#
#
# abc()


# def abc():
#     print("Welcome to Python!")
#
#
# print("Start")
# abc()
# print("End")

# Parameters VS Arguments


# def greet(name):  # Parameters
#     print("Hello", name)
#
#
# greet("Rahul")  # Arguments
# greet("Priya")

# Even and odd num check


# def check():
#     num = 8
#     if num % 2 == 0:
#         print("EVEN")
#     else:
#         print("ODD")
#
#
# check()

# Find the largest num

#
# def largest():
#     num = [45, 78, 23, 90, 56]
#     l = 0
#     for i in num:
#         if i > l:
#             l = i
#     print(l)
#
#
# largest()

# Calculate sum of list elements:


# def sum():
#     num = [10, 20, 30, 40, 50]
#     a = 0
#     for i in num:
#         a += i
#     print(a)
#
#
# sum()


# count vowels in a string


# def count():
#     s = "programming"
#     c = 0
#     for i in s:
#         if i in "aeiou":
#             c += 1
#     print("Total vowels:", c)
#
#
# count()


# Check pallindrome


# def check():
#     s = "madam"
#
#     if s == s[::-1]:
#         print("Pallindrome")
#     else:
#         print("Not Pallindrome")
#
#
# check()


# Parameterized Functions


# def add(a, b):
#     print(a + b)
#
#
# add(10, 20)


# check num is even or odd
# def check(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
#
#
# check(25)


# Claculate factorial


# def fact(num):
#     n = 1
#     for i in range(1, num + 1):
#         n *= i
#     print(n)
#
#
# fact(5)


# count vowels


# def count(s):
#     c = 0
#     for i in s:
#         if i in "aeiou":
#             c += 1
#     print("Total Vowels:", c)
#
#
# count("programming")


# Part A: Parameterized Functions (10 Questions)
# Instruction: Create a function that accepts the required values through parameters and performs the given operation.
# Q1. Find the Second Smallest and Second Largest
# Question: Write a parameterized function to find the second smallest and second largest distinct numbers from a given list without using sort() or max().
#
# Input:
# numbers = [45, 12, 78, 23, 90, 34, 56]


# def abc(num):
#     s = 100
#     l = 0
#

#
#
# Expected Output:
# Second Smallest: 23
# Second Largest: 78
#
#
# Q2. Find Words Having Unique Characters
# Question: Write a function that accepts a list of words and displays only those words in which every character appears exactly once.
#
# Input:
# words = ["python", "apple", "world", "hello", "java", "lamp"]
#
#
#
# Expected Output:
# ['python', 'world', 'java', 'lamp']
#
#
# Q3. Find the Difference Between Even and Odd Sum
# Question: Write a parameterized function that accepts a list of numbers, calculates the sum of even numbers and odd numbers separately, and displays their difference.
#
# Input:
# numbers = [10, 15, 20, 25, 30, 35, 40]
#
#
#
# Expected Output:
# Even Sum: 100
# Odd Sum: 75
# Difference: 25
#
#
# Q4. Find Duplicate Elements and Their Frequency
# Question: Write a function that accepts a list and displays only duplicate elements along with their frequency without using the count() method.
#
# Input:
# numbers = [10, 20, 10, 30, 20, 40, 10, 50, 30]
#
#
#
# Expected Output:
# 10 : 3
# 20 : 2
# 30 : 2
#
#
# Q5. Find the Longest and Shortest Word
# Question: Write a function that accepts a list of words and identifies the longest and shortest words without using max() or min().
#
# Input:
# words = ["Python", "AI", "Programming", "Java", "Machine"]
#
#
#
# Expected Output:
# Longest Word: Programming
# Shortest Word: AI
#
#
# Q6. Find Armstrong Numbers Within a Range
# Question: Write a parameterized function that accepts a starting number and ending number and displays all Armstrong numbers within that range.
#
# Input:
# start = 100end = 500
#
#
#
# Expected Output:
# Armstrong Numbers: [153, 370, 371, 407]
#
#
# Q7. Rearrange List Elements
# Question: Write a function that accepts a list and rearranges all zero elements to the end while maintaining the original order of other elements.
#
# Input:
# numbers = [0, 10, 0, 20, 30, 0, 40, 50]
#
#
#
# Expected Output:
# [10, 20, 30, 40, 50, 0, 0, 0]
#
#
# Q8. Find the Most Frequent Character
# Question: Write a function that accepts a string and identifies the character having the highest frequency. Ignore spaces.
#
# Input:
# word = "programming language"
#
#
#
# Expected Output:
# Most Frequent Character: g
# Frequency: 4
#
#
# Q9. Check Anagram Strings
# Question: Write a function that accepts two strings and checks whether both strings are anagrams or not. Ignore uppercase and lowercase differences.
#
# Input:
# str1 = "Listen"str2 = "Silent"
#
#
#
# Expected Output:
# Both Strings Are Anagrams
#
#
# Q10. Student Grade Management System
# Question: Write a parameterized function that accepts a student name and marks in five subjects. Calculate total marks, percentage, and grade.
#
# Grade Criteria:
# - 90 and above: A+
# - 80–89: A
# - 70–79: B
# - 60–69: C
# - Below 60: Fail
# Input:
# name = "Rahul"marks = [85, 90, 78, 92, 88]
#
#
#
# Expected Output:
# Student Name: Rahul
# Total Marks: 433
# Percentage: 86.6
# Grade: A
#
#
#
# Part B: Non-Parameterized Functions (10 Questions)
# Instruction: Create a function without passing any arguments. Define the required input data inside the function and perform the given operation.
# Q11. Find Perfect Numbers from a List
# Question: Write a non-parameterized function to identify all perfect numbers from a predefined list.
#
# A perfect number is a number whose sum of proper divisors is equal to the number itself.
#
# Input:
# numbers = [6, 12, 28, 15, 496, 20]
#
#
#
# Expected Output:
# Perfect Numbers: [6, 28, 496]
#
#
# Q12. Find Words Starting and Ending With the Same Character
# Question: Write a non-parameterized function to identify words that start and end with the same character.
#
# Input:
# words = ["level", "python", "radar", "apple", "madam", "world"]
#
#
#
# Expected Output:
# ['level', 'radar', 'madam']
#
#
# Q13. Find Pairs Whose Sum Equals a Target
# Question: Write a non-parameterized function to identify all unique pairs of numbers whose sum is equal to the given target.
#
# Input:
# numbers = [2, 4, 3, 5, 7, 8, 1, 9]target = 10
#
#
#
# Expected Output:
# (2, 8)
# (3, 7)
# (1, 9)
#
#
# Q14. Find the Longest Consecutive Sequence
# Question: Write a non-parameterized function to find the longest consecutive sequence of numbers from a predefined list. The numbers need not be in sorted order.
#
# Input:
# numbers = [100, 4, 200, 1, 3, 2, 5, 8]
#
#
#
# Expected Output:
# Longest Consecutive Sequence: [1, 2, 3, 4, 5]
# Length: 5
#
#
# Q15. Separate Words Based on Vowel Count
# Question: Write a non-parameterized function to separate words containing more than two vowels from the remaining words.
#
# Input:
# words = ["education", "python", "beautiful", "computer", "apple", "sequoia"]
#
#
#
# Expected Output:
# More Than Two Vowels:
# ['education', 'beautiful', 'sequoia']
#
# Two or Fewer Vowels:
# ['python', 'computer', 'apple']
#
#
# Q16. Find the Sum of Digits of Each Number
# Question: Write a non-parameterized function to calculate the sum of digits of each number greater than 100 from a predefined list.
#
# Input:
# numbers = [45, 123, 256, 78, 345, 99, 567]
#
#
#
# Expected Output:
# [6, 13, 12, 18]
#
#
# Q17. Find the Difference Between Two Dictionaries
# Question: Write a non-parameterized function to compare two dictionaries and display keys whose values are different in both dictionaries.
#
# Input:
# dict1 = {    "A": 80,    "B": 90,    "C": 70,    "D": 85}dict2 = {    "A": 80,    "B": 75,    "C": 70,    "D": 95}
#
#
#
# Expected Output:
# Different Values:
# B: 90, 75
# D: 85, 95
#
#
# Q18. Find Numbers Having Equal First and Last Digits
# Question: Write a non-parameterized function to identify numbers whose first and last digits are equal.
#
# Input:
# numbers = [121, 345, 454, 789, 232, 5675, 808]
#
#
#
# Expected Output:
# [121, 454, 232, 808]
#
#
# Q19. Find the Longest Word Without Repeated Characters
# Question: Write a non-parameterized function to identify the longest word in which no character is repeated.
#
# Input:
# words = ["python", "apple", "world", "hello", "lamp", "computer"]
#
#
#
# Expected Output:
# Longest Word: computer
# Length: 8
#
#
# Q20. Product Sales Analysis
# Question: Write a non-parameterized function to analyze product sales. Calculate the total sales amount, identify the highest-selling product based on quantity, and calculate the total quantity sold.
#
# Input:
# products = {    "Laptop": [50000, 5],    "Mobile": [20000, 10],    "Tablet": [15000, 8],    "Keyboard": [1000, 15]}
#
#
#
# Here, each value represents [price, quantity].
#
# Expected Output:
# Total Sales Amount: 595000
# Total Quantity Sold: 38
# Highest Selling Product: Keyboard
# Highest Quantity: 15


# non return type function - this function does not used to the return keyword its just perform a action using a print statement

# non return with non parameter
# print a greenting msg


# def greet():
#     print("Hello, Hi!")
#
#
# greet()


# def square(num):
#     print("Square:", num * num)
#
#
# square(5)


# Return type function - uses return keyword and return value to the caller


# def add(a, b):
#     total = a + b
#     return total
#
#
# result = add(10, 20)
# print(result)


# def greet():
#     return "Hello, Students!"
#
#
# msg = greet()
# print(msg)


# def calculate():
#     a, b = 10, 20
#     return a + b, a - b, a * b
#
#
# add, sub, mul = calculate()
# print(add)
# print(sub)
# print(mul)


# check the num is pallindrome or not


# def check(num):
#     og = num
#     rev = 0
#
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num //= 10
#     if og == rev:
#         return "Pallindrome"
#     else:
#         return "Not Pallindreome"
#
#
# result = check(121)
# print(result)


# armstrong num
#
#
# def arm(num):
#     a = len(str(num))
#     total = 0
#     temp = num
#
#     while temp > 0:
#         digit = temp % 10
#         total += digit**a
#         temp //= 10
#
#     if num == total:
#         return "Armstrong"
#     else:
#         return "not Armstrong"
#
#
# result = arm(153)
# print(result)


# reverse num


# def reverse(num):
#     og = num
#     rev = 0
#
#     while og > 0:
#         digit = og % 10
#         rev = rev * 10 + digit
#         og //= 10
#
#     return rev
#
#
# result = reverse(12345)
# print(result)


# lambda function
#

add = lambda a, b: a + b
result = add(10, 20)
print(result)
