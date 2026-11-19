# Set comprehension
#
# Syntax
# new_set={expression for item in iterable}


# num = [1, 1, 2, 2, 3, 4, 5]
# r = {i * i for i in num}
# print(r)


# create a set of num

# num = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10]
# r = {i for i in num}
# print(r)


# with conditions Syntax
# new_set={expression for item in iterable if condition}

# get only even num

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# r = {i for i in num if i % 2 == 0}
# print(r)


# print unique char
# n = "programming"
# # r = {i for i in n}
# # print(r)
# print({i for i in n})


# with if else condition Syntax
# new_set={value_if_true if condition else value_if_false for item in iterable}


# print even and odd
# num = [1, 2, 3, 4, 5, 6]
# r = {"even" if i % 2 == 0 else "Odd" for i in num}
# print(r)


# Section A: Set Comprehension (20 Questions)
# Level 2 – Questions 1 to 10
# Q1. Extract Even Numbers
# Question: Given a list of numbers, create a set containing only even numbers.
#
# Input:
# numbers = [12, 15, 18, 21, 24, 27, 30]
#
#
#
# Expected Output:
# {12, 18, 24, 30}
#
#
#
# Q2. Find Squares Greater Than 50
# Question: Create a set containing the squares of numbers whose square is greater than 50.
#
# Input:
# numbers = [2, 4, 5, 6, 7, 8, 9]
#
#
#
# Expected Output:
# {64, 81, 49}
#
#
#
# Correction: The expected output should contain only squares greater than 50:
# {64, 81}
#
#
#
# Q3. Find Unique Characters
# Question: Extract all unique characters from the given string.
#
# Input:
# text = "programming"
#
#
#
# Expected Output:
# {'p', 'r', 'o', 'g', 'a', 'm', 'i', 'n'}
#
#
#
# Q4. Filter Names by Length
# Question: Create a set containing names having more than 5 characters.
#
# Input:
# names = ["Amit", "Rahul", "Sneha", "Priyanka", "Rohit", "Akshay"]
#
#
#
# Expected Output:
# {'Priyanka', 'Akshay'}
#
#
#
# Q5. Find Numbers Divisible by 3 and 5
# Question: Extract numbers divisible by both 3 and 5.
#
# Input:
# numbers = [10, 15, 20, 30, 45, 50, 60, 75]
#
#
#
# Expected Output:
# {15, 30, 45, 60, 75}
#
#
#
# Q6. Convert Words into Uppercase
# Question: Convert all words into uppercase and store them in a set.
#
# Input:
# words = ["python", "java", "python", "django", "java"]
#
#
#
# Expected Output:
# {'PYTHON', 'JAVA', 'DJANGO'}
#
#
#
# Q7. Extract Positive Numbers
# Question: Create a set containing only positive numbers.
#
# Input:
# numbers = [-10, 20, -5, 30, 0, 40, -15]
#
#
#
# Expected Output:
# {20, 30, 40}
#
#
#
# Q8. Find Unique Vowels
# Question: Extract all unique vowels from the given string.
#
# Input:
# text = "education"
#
#
#
# Expected Output:
# {'e', 'u', 'a', 'i', 'o'}
#
#
#
# Q9. Find Numbers Greater Than 100 After Squaring
# Question: Create a set of squares of numbers whose square is greater than 100.
#
# Input:
# numbers = [5, 8, 9, 10, 11, 12]
#
#
#
# Expected Output:
# {121, 144}
#
#
#
# Q10. Find Words Starting with A
# Question: Extract all words starting with the letter 'A'.
#
# Input:
# names = ["Amit", "Rahul", "Anjali", "Sneha", "Akshay", "Rohan"]
#
#
#
# Expected Output:
# {'Amit', 'Anjali', 'Akshay'}
#
#
#
#
# Level 3 – Questions 11 to 20
# Q11. Find Common Characters
# Question: Given two strings, create a set containing characters common to both strings.
#
# Input:
# str1 = "programming"str2 = "python"
#
#
#
# Expected Output:
# {'p', 'o', 'n'}
#
#
#
# Q12. Find Numbers Having More Than Two Factors
# Question: From the given list, extract numbers that have more than two factors.
#
# Input:
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
#
# Expected Output:
# {4, 6, 8, 9, 10}
#
#
#
# Q13. Extract Palindrome Words
# Question: Create a set containing words that read the same forward and backward.
#
# Input:
# words = ["madam", "python", "level", "java", "radar", "civic"]
#
#
#
# Expected Output:
# {'madam', 'level', 'radar', 'civic'}
#
#
#
# Q14. Find Unique Word Lengths
# Question: Create a set containing the lengths of all unique word lengths.
#
# Input:
# words = ["apple", "banana", "cat", "dog", "mango", "kiwi"]
#
#
#
# Expected Output:
# {3, 4, 5, 6}
#
#
#
# Q15. Extract Numbers with Digit Sum Greater Than 10
# Question: Extract numbers whose sum of digits is greater than 10.
#
# Input:
# numbers = [29, 35, 46, 52, 81, 99, 123]
#
#
#
# Expected Output:
# {29, 35, 46, 99, 123}
#
#
#
# Q16. Find Words Containing More Than Two Vowels
# Question: Extract words containing more than two vowels.
#
# Input:
# words = ["education", "apple", "sky", "beautiful", "computer"]
#
#
#
# Expected Output:
# {'education', 'beautiful'}
#
#
#
# Q17. Generate Multiples of Two Numbers
# Question: Create a set containing numbers from the given list that are divisible by either 4 or 6.
#
# Input:
# numbers = [12, 16, 18, 20, 24, 30, 35, 36]
#
#
#
# Expected Output:
# {12, 16, 18, 20, 24, 30, 36}
#
#
#
# Q18. Find Anagrams
# Question: Given two lists of words, find words in the first list that have at least one anagram in the second list.
#
# Input:
# list1 = ["listen", "hello", "earth", "cat"]list2 = ["silent", "world", "heart", "act"]
#
#
#
# Expected Output:
# {'listen', 'earth', 'cat'}
#
#
#
# Q19. Extract Numbers with All Unique Digits
# Question: Extract numbers in which no digit is repeated.
#
# Input:
# numbers = [123, 112, 456, 787, 908, 1223, 567]
#
#
#
# Expected Output:
# {123, 456, 908, 567}
#
#
#
# Q20. Find Words with Only Alphabetic Characters
# Question: Extract words containing only alphabetic characters. Ignore words containing numbers or special characters.
#
# Input:
# words = ["Python", "Java123", "Django", "AI@ML", "Coding", "Data45"]
#
#
#
# Expected Output:
# {'Python', 'Django', 'Coding'}
#
#
#
#
# Section B: Dictionary Comprehension (20 Questions)
# Level 2 – Questions 1 to 10
# Q1. Create Number and Square Dictionary
# Question: Create a dictionary where each number is a key and its square is the value.
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
# Q2. Create Number and Cube Dictionary
# Question: Create a dictionary where each number is a key and its cube is the value.
#
# Input:
# numbers = [1, 2, 3, 4, 5]
#
#
#
# Expected Output:
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
#
#
#
# Q3. Create Name and Length Dictionary
# Question: Create a dictionary where names are keys and their lengths are values.
#
# Input:
# names = ["Amit", "Rahul", "Sneha", "Priyanka"]
#
#
#
# Expected Output:
# {    'Amit': 4,    'Rahul': 5,    'Sneha': 5,    'Priyanka': 8}
#
#
#
# Q4. Filter Students with Marks Greater Than 60
# Question: Create a new dictionary containing only students who scored more than 60.
#
# Input:
# marks = {    "Amit": 75,    "Rahul": 45,    "Sneha": 90,    "Priya": 55,    "Akshay": 85}
#
#
#
# Expected Output:
# {    'Amit': 75,    'Sneha': 90,    'Akshay': 85}
#
#
#
# Q5. Convert Dictionary Values into Squares
# Question: Create a new dictionary with the same keys but square all values.
#
# Input:
# data = {    "A": 2,    "B": 3,    "C": 4,    "D": 5}
#
#
#
# Expected Output:
# {    'A': 4,    'B': 9,    'C': 16,    'D': 25}
#
#
#
# Q6. Swap Keys and Values
# Question: Create a new dictionary by swapping the keys and values.
#
# Input:
# data = {    "A": 10,    "B": 20,    "C": 30}
#
#
#
# Expected Output:
# {    10: 'A',    20: 'B',    30: 'C'}
#
#
#
# Q7. Convert Names into Uppercase
# Question: Create a dictionary where the original names are keys and uppercase names are values.
#
# Input:
# names = ["amit", "rahul", "sneha"]
#
#
#
# Expected Output:
# {    'amit': 'AMIT',    'rahul': 'RAHUL',    'sneha': 'SNEHA'}
#
#
#
# Q8. Create Even and Odd Dictionary
# Question: Create a dictionary where numbers are keys and their type (Even/Odd) is the value.
#
# Input:
# numbers = [10, 15, 20, 25, 30, 35]
#
#
#
# Expected Output:
# {    10: 'Even',    15: 'Odd',    20: 'Even',    25: 'Odd',    30: 'Even',    35: 'Odd'}
#
#
#
# Q9. Filter Even Values from Dictionary
# Question: Create a new dictionary containing only key-value pairs where the value is even.
#
# Input:
# data = {    "A": 10,    "B": 15,    "C": 20,    "D": 25,    "E": 30}
#
#
#
# Expected Output:
# {    'A': 10,    'C': 20,    'E': 30}
#
#
#
# Q10. Create Student Pass/Fail Dictionary
# Question: Create a dictionary where student names are keys and Pass/Fail is the value. Passing marks are 40 or above.
#
# Input:
# marks = {    "Amit": 75,    "Rahul": 30,    "Sneha": 85,    "Priya": 25}
#
#
#
# Expected Output:
# {    'Amit': 'Pass',    'Rahul': 'Fail',    'Sneha': 'Pass',    'Priya': 'Fail'}
#
#
#
#
# Level 3 – Questions 11 to 20
# Q11. Create Character Frequency Dictionary
# Question: Count how many times each character occurs in a string using dictionary comprehension.
#
# Input:
# text = "banana"
#
#
#
# Expected Output:
# {    'b': 1,    'a': 3,    'n': 2}
#
#
#
# Hint: Use set() and count().
# Q12. Create Word Frequency Dictionary
# Question: Count the frequency of each unique word in a sentence.
#
# Input:
# sentence = "python java python django java python"
#
#
#
# Expected Output:
# {    'python': 3,    'java': 2,    'django': 1}
#
#
#
# Hint: Use split(), set() and count().
# Q13. Find the Highest Marks Students
# Question: Create a dictionary containing students who scored more than 80 marks and increase their marks by 5.
#
# Input:
# marks = {    "Amit": 75,    "Rahul": 85,    "Sneha": 92,    "Priya": 65,    "Akshay": 88}
#
#
#
# Expected Output:
# {    'Rahul': 90,    'Sneha': 97,    'Akshay': 93}
#
#
#
# Q14. Create Number and Digit Sum Dictionary
# Question: Create a dictionary where each number is a key and the sum of its digits is the value.
#
# Input:
# numbers = [123, 456, 789, 234]
#
#
#
# Expected Output:
# {    123: 6,    456: 15,    789: 24,    234: 9}
#
#
#
# Hint: Use str() and sum().
# Q15. Create Dictionary of Prime Numbers
# Question: Create a dictionary containing only prime numbers as keys and their squares as values.
#
# Input:
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 11]
#
#
#
# Expected Output:
# {    2: 4,    3: 9,    5: 25,    7: 49,    11: 121}
#
#
#
# Hint: Use all() with a condition to check prime numbers.
# Q16. Create Dictionary of Vowel Counts
# Question: Create a dictionary where each word is a key and the number of vowels in that word is the value.
#
# Input:
# words = ["apple", "banana", "education", "python"]
#
#
#
# Expected Output:
# {    'apple': 2,    'banana': 3,    'education': 5,    'python': 1}
#
#
#
# Q17. Create Dictionary with Conditional Discount
# Question: Create a new dictionary where product names are keys and discounted prices are values. Apply a 10% discount if the price is above 1000; otherwise keep the original price.
#
# Input:
# products = {    "Laptop": 50000,    "Mouse": 500,    "Keyboard": 1500,    "Monitor": 8000}
#
#
#
# Expected Output:
# {    'Laptop': 45000.0,    'Mouse': 500,    'Keyboard': 1350.0,    'Monitor': 7200.0}
#
#
#
# Q18. Create Dictionary of Word Reversals
# Question: Create a dictionary where each word is a key and its reversed word is the value.
#
# Input:
# words = ["python", "java", "django", "coding"]
#
#
#
# Expected Output:
# {    'python': 'nohtyp',    'java': 'avaj',    'django': 'ognajd',    'coding': 'gnidoc'}
#
#
#
# Q19. Create Dictionary of Student Grades
# Question: Create a dictionary where student names are keys and grades are values based on marks.
#
# Conditions:
# - 90 and above = A
# - 75 to 89 = B
# - 60 to 74 = C
# - Below 60 = D
# Input:
# marks = {    "Amit": 95,    "Rahul": 82,    "Sneha": 70,    "Priya": 45,    "Akshay": 90}
#
#
#
# Expected Output:
# {    'Amit': 'A',    'Rahul': 'B',    'Sneha': 'C',    'Priya': 'D',    'Akshay': 'A'}
#
#
#
# Q20. Create Dictionary of Common Elements
# Question: Given two lists, create a dictionary where each common number is a key and its square is the value.
#
# Input:
# list1 = [10, 20, 30, 40, 50]list2 = [20, 30, 50, 60, 70]
#
#
#
# Expected Output:
# {    20: 400,    30: 900,    50: 2500}
