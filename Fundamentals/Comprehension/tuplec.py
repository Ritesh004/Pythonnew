# Python does not support tuple comprehension so we use generator expression.
# Syntax

# r=(expression for item in iterable)

# n = [1, 2, 3, 4, 5]
# r = (i * i for i in n)
# # for e in r:
# #     print(e, end=" ")
#
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))


# student marks processing

# m = [45, 60, 75, 80, 90]
# r = (i + 5 for i in m)
# for i in r:
#     print(i, end=" ")


# E-Commerce
# an online shopping application wants to calculate price after applying 10% discount

# p = [1000, 2000, 3000, 4000, 5000]
# r = (i - i * 0.10 for i in p)
# for i in r:
#     print(i, end=" ")


# Banking transaction procession

# t = [5000, 8000, 15000, 25000, 30000]
# r = (i for i in t if i > 10000)
# for i in r:
#     print(i, end=" ")

# generat a square from 1 to 5

# r = (i**2 for i in range(1, 6))
# for i in r:
#     print(i, end=" ")


# genrate even num from 1 to 10

# r = (i for i in range(1, 11) if i % 2 == 0)
# for i in r:
#     print(i, end=" ")


# r = (i**2 for i in range(1, 21) if i % 2 == 0)
# for i in r:
#     print(i, end=" ")
#


# r = (i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0)
# for i in r:
#     print(i, end=" ")
#


# Section 1: List Comprehension – 10 Questions
# Q1. Generate squares of numbers that are divisible by both 2 and 3.
#
# Input:
# numbers = [12, 15, 18, 20, 24, 27, 30, 36]
#
# r = [i**2 for i in numbers if i % 2 == 0 and i % 3 == 0]
# print(r, end=" ")


#
#
# Expected Output:
# [144, 324, 576, 900, 1296]
#
#
# Q2. Extract numbers whose last digit is 5 or 0 and calculate their cubes.
#
# Input:
# numbers = [15, 22, 30, 45, 52, 60, 75, 88]
#
#
#
# Expected Output:
# [3375, 27000, 91125, 216000, 421875]
#
#
# Q3. Generate the first character of each word and convert it into uppercase.
#
# Input:
# words = ["python", "java", "django", "machine", "learning"]
#
#
#
# Expected Output:
# ['P', 'J', 'D', 'M', 'L']
#
#
# Q4. Extract palindrome numbers from the given list.
#
# Input:
# numbers = [121, 234, 454, 567, 777, 890, 909, 123]
#
#
#
# Expected Output:
# [121, 454, 777, 909]
#
#
# Q5. Generate the difference between each number and 100, but only for numbers greater than 50.
#
# Input:
# numbers = [20, 60, 75, 40, 90, 100, 30]
#
#
#
# Expected Output:
# [40, 25, 10, 0]
#
#
# Q6. Generate words containing vowels at both the first and last positions.
#
# Input:
# words = ["apple", "orange", "umbrella", "india", "python", "elephant"]
#
#
#
# Expected Output:
# ['apple', 'orange', 'india']
#
#
# Q7. Generate numbers whose square is divisible by 4.
#
# Input:
# numbers = [3, 4, 5, 6, 7, 8, 9, 10]
#
#
#
# Expected Output:
# [16, 36, 64, 100]
#
#
# Q8. Extract words having more than two vowels.
#
# Input:
# words = ["education", "python", "beautiful", "computer", "apple", "sequoia"]
# r=[i in i for words if sum(1 for ch in word if ch in 'aeiou')>2]
# print(r)
#
#
# Expected Output:
# ['education', 'beautiful', 'sequoia']
#
#
# Q9. Generate the sum of digits of each number, but only for numbers greater than 100.
#
# Input:
numbers = [45, 123, 256, 78, 345, 99, 567]
r = [sum(int(i) for i in str(num)) for num in numbers if num > 100]
print(r)
#
#
# Expected Output:
# [6, 13, 12, 18]
#
#
# Q10. Generate numbers that are divisible by 2 but not divisible by 3, and calculate their squares.
#
# Input:
# numbers = [12, 14, 16, 18, 20, 22, 24, 26]
#
#
#
# Expected Output:
# [196, 256, 400, 484, 676]
#
#
#
# Section 2: Dictionary Comprehension – 10 Questions
# Q11. Create a dictionary containing each number and its square.
#
# Input:
# numbers = [2, 3, 4, 5, 6]
#
#
#
# Expected Output:
# {2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
#
#
#
# Q12. Reverse the keys and values of a dictionary.
#
# Input:
# data = {"A": 10, "B": 20, "C": 30, "D": 40}
#
#
#
# Expected Output:
# {10: "A", 20: "B", 30: "C", 40: "D"}
#
#
#
# Q13. Create a dictionary containing only students who scored above 60.
#
# Input:
# marks = {"Amit": 45, "Rahul": 75, "Sneha": 90, "Rohit": 55, "Priya": 80}
#
#
#
# Expected Output:
# {"Rahul": 75, "Sneha": 90, "Priya": 80}
#
#
#
# Q14. Create a dictionary where each word is a key and its length is the value.
#
# Input:
# words = ["Python", "Java", "Django", "Machine"]
#
#
#
# Expected Output:
# {"Python": 6, "Java": 4, "Django": 6, "Machine": 7}
#
#
#
# Q15. Create a dictionary containing only even values and their cubes.
#
# Input:
# data = {"A": 2, "B": 3, "C": 4, "D": 5, "E": 6}
#
#
#
# Expected Output:
# {"A": 8, "C": 64, "E": 216}
#
#
#
# Q16. Create a dictionary containing each character and its ASCII value.
#
# Input:
# characters = ["A", "B", "C", "D"]
#
#
#
# Expected Output:
# {"A": 65, "B": 66, "C": 67, "D": 68}
#
#
#
# Q17. Create a dictionary containing employee names and their updated salaries after a 15% increment.
#
# Input:
# employees = {"Amit": 20000, "Rahul": 30000, "Sneha": 40000}
#
#
#
# Expected Output:
# {"Amit": 23000.0, "Rahul": 34500.0, "Sneha": 46000.0}
#
#
#
# Q18. Create a dictionary containing words that start with vowels and their uppercase versions.
#
# Input:
# words = ["apple", "banana", "orange", "grapes", "umbrella", "mango"]
#
#
#
# Expected Output:
# {"apple": "APPLE", "orange": "ORANGE", "umbrella": "UMBRELLA"}
#
#
#
# Q19. Create a dictionary containing numbers as keys and their factorials as values.
#
# Input:
# numbers = [1, 2, 3, 4, 5]
#
#
#
# Expected Output:
# {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
#
#
#
# Q20. Create a dictionary containing only products whose prices are between 500 and 2000.
#
# Input:
# products = {"Mobile": 15000, "Mouse": 500, "Keyboard": 1200, "USB": 300, "Headphone": 1800}
#
#
#
# Expected Output:
# {"Mouse": 500, "Keyboard": 1200, "Headphone": 1800}
#
#
#
#
# Section 3: Set Comprehension – 10 Questions
# Q21. Generate unique squares from the given list.
#
# Input:
# numbers = [2, 3, 2, 4, 3, 5, 4, 6]
#
#
#
# Expected Output:
# {4, 9, 16, 25, 36}
#
#
#
# Q22. Generate unique even numbers from the list and calculate their cubes.
#
# Input:
# numbers = [2, 4, 3, 6, 8, 4, 10, 6]
#
#
#
# Expected Output:
# {8, 64, 216, 512, 1000}
#
#
#
# Q23. Generate unique characters from a string, excluding vowels.
#
# Input:
# text = "programming"
#
#
#
# Expected Output:
# {'p', 'r', 'g', 'm', 'n'}
#
#
#
# Q24. Generate unique first letters from a list of names.
#
# Input:
# names = ["Amit", "Ankit", "Rahul", "Rohit", "Sneha", "Sagar"]
#
#
#
# Expected Output:
# {'A', 'R', 'S'}
#
#
#
# Q25. Generate unique numbers divisible by both 2 and 5.
#
# Input:
# numbers = [10, 15, 20, 25, 30, 40, 45, 50]
#
#
#
# Expected Output:
# {10, 20, 30, 40, 50}
#
#
#
# Q26. Generate unique word lengths from the given list.
#
# Input:
# words = ["cat", "dog", "apple", "mango", "banana", "kiwi"]
#
#
#
# Expected Output:
# {3, 4, 5, 6}
#
#
#
# Q27. Generate unique positive numbers and calculate their squares.
#
# Input:
# numbers = [-2, 3, 4, -5, 3, 6, -4, 8]
#
#
#
# Expected Output:
# {9, 16, 36, 64}
#
#
#
# Q28. Generate unique numbers that are perfect squares from the given list.
#
# Input:
# numbers = [4, 9, 10, 16, 20, 25, 30, 36, 49]
#
#
#
# Expected Output:
# {4, 9, 16, 25, 36, 49}
#
#
#
# Q29. Generate unique vowels present in the given string.
#
# Input:
# text = "comprehension"
#
#
#
# Expected Output:
# {'o', 'e', 'i'}
#
#
#
# Q30. Generate unique numbers whose digit sum is greater than 5.
#
# Input:
# numbers = [12, 23, 31, 45, 51, 62, 72, 18]
#
#
#
# Expected Output:
# {23, 45, 62, 72, 18}
#
#
#
#
# Section 4: Generator Expression – 10 Questions
# Q31. Generate squares of numbers divisible by both 2 and 3 from 1 to 50.
#
# Input:
# numbers = range(1, 51)
#
#
#
# Expected Output:
# 36
# 144
# 324
# 576
# 900
# 1296
# 1764
# 2304
#
#
# Q32. Generate numbers whose reverse is equal to the original number.
#
# Input:
# numbers = [121, 234, 454, 567, 777, 890, 909, 123]
#
#
#
# Expected Output:
# 121
# 454
# 777
# 909
#
#
# Q33. Generate cubes of numbers whose squares are greater than 100.
#
# Input:
# numbers = range(1, 16)
#
#
#
# Expected Output:
# 1331
# 1728
# 2197
# 2744
# 3375
# 4096
# 4913
# 5832
# 6859
# 8000
# 9261
# 10648
#
#
# Q34. Generate only words containing more than 5 characters and convert them into uppercase.
#
# Input:
# words = ["python", "java", "programming", "django", "machine", "AI"]
#
#
#
# Expected Output:
# PYTHON
# PROGRAMMING
# MACHINE
#
#
# Q35. Generate numbers divisible by 4 or 6 and calculate their double.
#
# Input:
# numbers = range(1, 31)
#
#
#
# Expected Output:
# 8
# 12
# 16
# 24
# 32
# 36
# 40
# 48
# 56
# 60
#
#
# Q36. Generate the sum of digits for numbers greater than 100 and divisible by 3.
#
# Input:
# numbers = [105, 123, 150, 200, 225, 300, 345, 400]
#
#
#
# Expected Output:
# 6
# 6
# 6
# 9
# 12
#
#
# Q37. Generate numbers that contain exactly three digits and are divisible by 7.
#
# Input:
# numbers = range(100, 151)
#
#
#
# Expected Output:
# 105
# 112
# 119
# 126
# 133
# 140
# 147
#
#
# Q38. Generate factorials of only even numbers from 1 to 8.
#
# Input:
# numbers = range(1, 9)
#
#
#
# Expected Output:
# 2
# 24
# 720
# 40320
#
#
# Q39. Generate numbers whose digit sum is even.
#
# Input:
# numbers = [12, 23, 34, 45, 56, 67, 78, 89]
#
#
#
# Expected Output:
# 12
# 34
# 56
# 78
#
#
# Q40. Generate the square of numbers that are greater than the average value of the given list.
#
# Input:
# numbers = [10, 20, 30, 40, 50, 60, 70]
#
#
#
# Expected Output:
# 1600
# 2500
# 3600
# 4900
