# List Comprehension []

# Syntax
# [Expresion for variable in iterable condition if condition]


# 1 print squares of numbers

# num = [1, 2, 3, 4, 5]
# result = [i**2 for i in num]
# print(result)

# 2 print even num only

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# r = [i for i in l if i % 2 == 0]
# print(r)


# print string in uppercase

# l = ["rahul", "amit", "priya"]
# r = [i.upper() for i in l]
# print(r)


# List comprerhension with if else
# Syntax
# [exxpression_if if condition else expression_else for variable in iterable]


# l = [1, 2, 3, 4, 5]
# r = ["even" if i % 2 == 0 else "odd" for i in l]
# print(r)


# find nums greater than 50

# l = [25, 60, 45, 80, 35, 90, 50, 75]
# r = [i for i in l if i >= 50]
# print(r)


# find the length of each word

# l = ["Python", "Java", "Machine", "AI", "Developer"]
# r = [len(i) for i in l]
# print(r)


# replace negative values with zero


# l = [10, -5, 20, -15, 30, -2, 40]
# r = [0 if i < 0 else i for i in l]
# print(r)


# find num divisible by 3 and 5

# l = [10, 15, 20, 30, 45, 50, 60, 75]
# r = [i for i in l if i % 3 == 0 and i % 5 == 0]
# print(r)
#


# extract names starting with A


# l = ["Akash", "Rahul", "Amit", "Rohit", "Anjali", "Sneha"]
# r = [i for i in l if i.startswith("A")]
# print(r)


# Level 2 – Basic to Intermediate (Questions 1–15)
# Q1. Find the Square of Numbers
#
# Write a program to calculate the square of every number in the given list.
#
# Input:
# numbers = [2, 4, 6, 8, 10, 12]
#
#
#
# Q2. Extract Even Numbers
#
# Write a program to extract all even numbers from the list.
#
# Input:
# numbers = [11, 24, 35, 42, 56, 63, 78, 89]
#
#
#
# Q3. Extract Odd Numbers
#
# Write a program to extract all odd numbers from the list.
#
# Input:
# numbers = [10, 15, 22, 33, 40, 51, 64, 77, 82]
#
#
#
# Q4. Find Numbers Greater Than 50
#
# Write a program to extract all numbers greater than 50.
#
# Input:
# numbers = [25, 60, 45, 80, 35, 90, 50, 75, 100]
#
#
#
# Q5. Convert Names into Uppercase
#
# Write a program to convert all names into uppercase.
#
# Input:
# names = ["akshay", "rahul", "rohit", "sneha", "priya"]
#
#
#
# Q6. Find the Length of Each Word
#
# Write a program to calculate the length of every word.
#
# Input:
# words = ["Python", "Java", "Machine", "AI", "Developer", "Data"]
#
#
#
# Q7. Find the Cube of Each Number
#
# Write a program to calculate the cube of every number.
#
# Input:
# numbers = [1, 2, 3, 4, 5, 6]
#
#
#
# Q8. Extract Numbers Divisible by 5
#
# Write a program to extract all numbers divisible by 5.
#
# Input:
# numbers = [12, 15, 20, 23, 35, 41, 50, 65, 72, 80]
#
#
#
# Q9. Replace Negative Numbers with Zero
#
# Write a program to replace negative numbers with zero and keep positive numbers unchanged.
#
# Input:
# numbers = [10, -5, 20, -15, 30, -2, 40, -8]
#
#
#
# Q10. Find Numbers Between 20 and 60
#
# Write a program to extract numbers greater than 20 and less than 60.
#
# Input:
# numbers = [10, 25, 35, 60, 45, 75, 55, 80, 15]
#
#
#
# Q11. Convert Words into Lowercase
#
# Write a program to convert all words into lowercase.
#
# Input:
# words = ["PYTHON", "JAVA", "MACHINE", "LEARNING", "DATA"]
#
#
#
# Q12. Find the First Character of Each Word
#
# Write a program to extract the first character from every word.
#
# Input:
# words = ["Python", "Java", "Machine", "Developer", "Cloud"]
#
#
#
# Q13. Calculate the Double of Each Number
#
# Write a program to multiply every number by 2.
#
# Input:
# numbers = [5, 10, 15, 20, 25, 30]
#
#
#
# Q14. Extract Names Starting with A
#
# Write a program to extract all names starting with the letter A.
#
# Input:
# names = ["Akshay", "Rahul", "Amit", "Rohit", "Anjali", "Sneha", "Ajay"]
#
#
#
# Q15. Classify Numbers as Even or Odd
#
# Write a program to replace even numbers with "Even" and odd numbers with "Odd".
#
# Input:
# numbers = [10, 15, 22, 33, 40, 51, 64, 77]
#
#
#
#
# Level 3 – Logical and Advanced Coding (Questions 16–30)
# Q16. Find Numbers Divisible by Both 3 and 5
#
# Write a program to extract numbers divisible by both 3 and 5.
#
# Input:
# numbers = [10, 15, 20, 30, 45, 50, 60, 75, 90, 100]
#
#
#
# Q17. Find the Cube of Odd Numbers
#
# Write a program to extract odd numbers and calculate their cubes.
#
# Input:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
#
# Q18. Find Squares of Numbers Greater Than 10
#
# Write a program to extract numbers greater than 10 and calculate their squares.
#
# Input:
# numbers = [5, 12, 8, 15, 20, 3, 25, 30, 7]
#
#
#
# Q19. Replace Even Numbers with Their Squares and Odd Numbers with Their Cubes
#
# Write a program to apply the following logic:
# - If the number is even, calculate its square.
# - If the number is odd, calculate its cube.
# Input:
# numbers = [2, 3, 4, 5, 6, 7, 8, 9]
#
#
#
# Q20. Extract Words Having More Than 5 Characters
#
# Write a program to extract words containing more than 5 characters.
#
# Input:
# words = ["Python", "Java", "Machine", "AI", "Developer", "SQL", "Programming"]
#
#
#
# Q21. Find Numbers Whose Square Is Greater Than 100
#
# Write a program to extract only those numbers whose square is greater than 100.
#
# Input:
# numbers = [5, 8, 10, 12, 3, 15, 6, 20, 9]
#
#
#
# Q22. Extract Positive Even Numbers
#
# Write a program to extract numbers that are both positive and even.
#
# Input:
# numbers = [-10, 12, -15, 20, 25, -30, 40, 55, 60, -8]
#
#
#
# Q23. Replace Numbers Greater Than 50 with 100
#
# Write a program with the following conditions:
# - If a number is greater than 50, replace it with 100.
# - Otherwise, keep the original number.
# Input:
# numbers = [10, 60, 25, 80, 45, 90, 30, 55]
#
#
#
# Q24. Extract Words Ending with 'n'
#
# Write a program to extract all words ending with the letter 'n'.
#
# Input:
# words = ["Python", "Java", "Machine", "Developer", "Design", "Information", "Cloud"]
#
#
#
# Q25. Find the Sum of Digits of Each Number
#
# Write a program to calculate the sum of digits of every number using list comprehension.
#
# Input:
# numbers = [123, 456, 789, 234, 567]
#
#
#
# Q26. Extract Numbers Between 1 and 100 That Are Divisible by 7
#
# Write a program to extract all numbers divisible by 7 from the given list.
#
# Input:
# numbers = [14, 25, 35, 42, 50, 63, 70, 81, 91, 100]
#
#
#
# Q27. Convert Negative Numbers into Positive Numbers
#
# Write a program to convert all negative numbers into positive numbers and keep positive numbers unchanged.
#
# Input:
# numbers = [10, -20, 30, -40, 50, -60, 70, -80]
#
#
#
# Q28. Extract Palindrome Words
#
# Write a program to extract words that read the same forward and backward.
#
# Input:
# words = ["madam", "python", "level", "java", "radar", "hello", "noon"]
#
#
#
# Q29. Find Numbers Whose Last Digit Is 5
#
# Write a program to extract all numbers whose last digit is 5.
#
# Input:
# numbers = [15, 22, 35, 40, 55, 67, 75, 80, 95, 100]
#
#
#
# Q30. Apply Multiple Conditions on Student Marks
#
# Write a program using list comprehension to extract marks of students who:
# - Scored more than or equal to 60.
# - Scored less than or equal to 90.
# - Have marks divisible by 5.
# Input:
# marks = [45, 50, 60, 65, 72, 75, 80, 85, 90, 95, 100]
