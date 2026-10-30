# # 1. Create a dictionary containing five student names and their marks. Display the dictionary.
# marks={
#     'ABC':90,
#     'DEF':89,
#     'GHI':86,
#     'JKL':78,
#     'MNO':96
# }
# print(marks)
# print()
# # 2. Create a dictionary containing five countries and their capitals. Display each country and its capital using a loop.
# capitals = {
#     "India": "New Delhi",
#     "Russia": "Mosscow",
#     "USA": "Washington D.C.",
#     "Germany": "Berlin",
#     "Spain": "Madrid",
# }
# for key in capitals:
#     print(key,capitals[key])
# for key, value in capitals.items():
#     print(f"{key} : {value}")
# 3. Create a dictionary containing five products and their prices. Display all the keys and values separately.

# 4. Create a dictionary containing student details such as name, age, and course. Access and display each value using its key.
# 5. Create a dictionary containing five fruits and their prices. Add a new fruit with its price to the dictionary.
# 6. Create a dictionary containing five students and their marks. Update the marks of one student.
# 7. Create a dictionary containing five employee names and their salaries. Remove one employee using the pop() method.
# 8. Create a dictionary containing five programming languages and their creators. Remove the last inserted item using the popitem() method.
# 9. Create a dictionary containing five cities and their populations. Check whether a particular city exists in the dictionary.
# 10. Create a dictionary containing five student names and their marks. Display only the names of the students.
# 11. Create a dictionary containing five products and their prices. Display only the prices of all products.
# 12. Create a dictionary containing duplicate values. Count how many times a particular value occurs.
# 13. Create a dictionary containing five students and their marks. Find the total number of items in the dictionary without manually counting them.
# 14. Create a dictionary containing five students and their marks. Display the student who scored the highest marks.
# 15. Create a dictionary containing five students and their marks. Display the student who scored the lowest marks.
# 16. Create a dictionary containing five students and their marks. Display only the students who scored more than 60 marks.
# 17. Create a dictionary containing five numbers as keys and their squares as values.
# 18. Create a dictionary containing numbers from 1 to 10 as keys and their cubes as values using dictionary comprehension.
# 19. Create a dictionary containing numbers from 1 to 20 as keys and their values as even or odd using dictionary comprehension.
# 20. Create a dictionary containing five student names and their marks. Create a new dictionary containing only students who scored 75 or more marks.
# 21. Create two dictionaries containing student details. Merge both dictionaries into a single dictionary.
# 22. Create a dictionary containing five employees and their salaries. Increase every employee's salary by 10% and update the dictionary.
# 23. Create a dictionary containing five words and their meanings. Search for a word and display its meaning if it exists; otherwise, display an appropriate message.
# 24. Create a dictionary containing five student names and their marks. Display each student's name and marks in alphabetical order of their names.
# 25. Create a dictionary containing five products and their prices. Sort the dictionary items by price in ascending order.
# 26. Create a dictionary containing five student names and their marks. Find the average marks of all students.
# 27. Create a dictionary containing five characters as keys and their frequencies as values. Display the character with the highest frequency.
# 28. Create a nested dictionary containing details of three students, including their names, ages, and marks. Access and display each student's details.
# 29. Create a nested dictionary containing details of three employees, including their IDs, names, and salaries. Update the salary of one employee using the employee's ID.
# 30. Write a Python program to count the frequency of each word in a given sentence and store the words and their frequencies in a dictionary.


# logical Questions dictionary

# marks = {"Rahul": 78, "Amit": 92, "Sneha": 80, "Priya": 89}
# highest = 0
# topper = ""
# for i in marks:
#     if marks[i] > highest:
#         highest = marks[i]
#         topper = i
# print("Highest:", highest)
# print("topper:", topper)


# count no. of students passed
# marks = {"Rahul": 35, "Amit": 75, "Sneha": 28, "Priya": 60, "Raj": 45}
# count = 0
# for i in marks:
#     if marks[i] >= 40:
#         count += 1
# print(count)

# calculate total and avg marks
# marks = {"Rahul": 80, "Amit": 90, "Sneha": 70, "Priya": 60}
# total = 0
# avg = 0
# for i in marks:
#     total += marks[i]
# avg = total / len(marks)
# print("Total Marks:", total)
# print("Average marks:", avg)


# create a new dict with only even values
# num = {"a": 12, "b": 15, "c": 20, "d": 25, "e": 30}
# even = {}
# for i in num:
#     if num[i] % 2 == 0:
#         even[i] = num[i]
# print(even)


# count the frequency of each characters
# text = "programming"
# frequency = {}
# for i in text:
#     if i in frequency:
#         frequency[i] = frequency[i] + 1
#     else:
#         frequency[i] = 1
# print(frequency)


# replace value with key

# num = {"a": 12, "b": 15, "c": 20, "d": 25, "e": 30}
# result = {}
# for i in num:
#     result[num[i]] = i
# print(result)


# group num into even odd

# num = [12, 15, 18, 21, 24, 27, 30]
# result = {"even": [], "odd": []}
# for i in num:
#     if i % 2 == 0:
#         result["even"].append(i)
#     else:
#         result["odd"].append(i)
# print(result)


# Python Dictionary – 20 Coding Practice Questions
# Level 1 – 10 Questions
# Q1. Create a Dictionary
# Create a dictionary containing the names of 4 students and their ages. Print the dictionary.
#
# Input:
# students = {    "Rahul": 21,    "Amit": 22,    "Sneha": 20,    "Priya": 23}
#
#
#
# Output:
# {'Rahul': 21, 'Amit': 22, 'Sneha': 20, 'Priya': 23}
#
#
# Q2. Access a Specific Value
# Write a program to access and print the price of the product "Laptop".
#
# Input:
# products = {    "Laptop": 55000,    "Mobile": 20000,    "Tablet": 15000,    "Mouse": 500}
#
#
#
# Output:
# Laptop Price: 55000
#
#
# Q3. Add a New Key-Value Pair
# Write a program to add "Orange": 60 to the given dictionary.
#
# Input:
# fruits = {    "Apple": 100,    "Banana": 40,    "Mango": 80}
#
#
#
# Output:
# {'Apple': 100, 'Banana': 40, 'Mango': 80, 'Orange': 60}
#
#
# Q4. Update an Existing Value
# Write a program to update the price of "Mobile" from 15000 to 18000.
#
# Input:
products = {"Laptop": 55000, "Mobile": 15000, "Mouse": 500}
products["Mobile"] = 18000
print(products)
#
#
# Output:
# {'Laptop': 55000, 'Mobile': 18000, 'Mouse': 500}
#
#
# Q5. Delete a Specific Key
# Write a program to remove "Banana" from the given dictionary.
#
# Input:
# fruits = {    "Apple": 100,    "Banana": 40,    "Mango": 80,    "Orange": 60}
#
#
#
# Output:
# {'Apple': 100, 'Mango': 80, 'Orange': 60}
#
#
# Q6. Print All Dictionary Keys
# Write a program to print all the keys from the given dictionary using a loop.
#
# Input:
# employee = {    "name": "Akash",    "age": 25,    "salary": 35000,    "city": "Pune"}
#
#
#
# Output:
# name
# age
# salary
# city
#
#
# Q7. Print All Dictionary Values
# Write a program to print all the values from the given dictionary using a loop.
#
# Input:
# employee = {    "name": "Rahul",    "age": 24,    "salary": 40000,    "city": "Mumbai"}
#
#
#
# Output:
# Rahul
# 24
# 40000
# Mumbai
#
#
# Q8. Check Whether a Key Exists
# Write a program to check whether "Python" exists as a key in the given dictionary.
#
# Input:
# courses = {    "Java": 3000,    "Python": 2500,    "C++": 2000,    "SQL": 1500}
#
#
#
# Output:
# Python is Available
#
#
# Q9. Count Dictionary Elements
# Write a program to count the total number of key-value pairs in the dictionary without using the len() function.
#
# Input:
# data = {    "a": 10,    "b": 20,    "c": 30,    "d": 40,    "e": 50}
#
#
#
# Output:
# Total Elements: 5
#
#
# Q10. Print Keys with Their Values
# Write a program to display each employee's name and department using a loop.
#
# Input:
# employees = {    "Rahul": "IT",    "Sneha": "HR",    "Amit": "Finance",    "Priya": "Marketing"}
#
#
#
# Output:
# Rahul : IT
# Sneha : HR
# Amit : Finance
# Priya : Marketing
#
#
#
# Level 2 – 10 Questions
# Q11. Find the Product with the Lowest Price
# Write a program to find the product having the lowest price without using the built-in min() function.
#
# Input:
# products = {    "Laptop": 55000,    "Mouse": 500,    "Keyboard": 1200,    "Monitor": 12000}
#
#
#
# Output:
# Cheapest Product: Mouse
# Price: 500
#
#
# Q12. Separate Positive and Negative Values
# Write a program to create a new dictionary containing separate positive and negative numbers.
#
# Input:
# numbers = {    "a": 10,    "b": -5,    "c": 20,    "d": -15,    "e": 30}
#
#
#
# Output:
# {    'Positive': {'a': 10, 'c': 20, 'e': 30},    'Negative': {'b': -5, 'd': -15}}
#
#
#
# Q13. Calculate the Total Salary Department-Wise
# Write a program to calculate the total salary of employees belonging to each department.
#
# Input:
# employees = {    "Rahul": {"department": "IT", "salary": 40000},    "Amit": {"department": "HR", "salary": 30000},    "Sneha": {"department": "IT", "salary": 45000},    "Priya": {"department": "HR", "salary": 35000}}
#
#
#
# Output:
# {    'IT': 85000,    'HR': 65000}
#
#
#
# Q14. Find Keys Having Values Greater Than 50
# Write a program to display only the keys whose values are greater than 50.
#
# Input:
# data = {    "A": 25,    "B": 75,    "C": 90,    "D": 40,    "E": 60}
#
#
#
# Output:
# ['B', 'C', 'E']
#
#
#
# Q15. Remove Duplicate Values
# Write a program to create a new dictionary by keeping only the first occurrence of each value.
#
# Input:
# data = {    "a": 10,    "b": 20,    "c": 10,    "d": 30,    "e": 20}
#
#
#
# Output:
# {'a': 10, 'b': 20, 'd': 30}
#
#
#
# Q16. Find the Difference Between Two Dictionaries
# Write a program to find the keys that are present in the first dictionary but not in the second dictionary.
#
# Input:
# dict1 = {    "Python": 90,    "Java": 80,    "SQL": 85,    "HTML": 75}dict2 = {    "Python": 90,    "SQL": 85,    "CSS": 70}
#
#
#
# Output:
# {'Java': 80, 'HTML': 75}
#
#
#
# Q17. Calculate Subject-Wise Total Marks
# Write a program to calculate the total marks obtained by each subject across all students.
#
# Input:
# students = {    "Rahul": {"Math": 80, "Science": 70},    "Amit": {"Math": 90, "Science": 85},    "Sneha": {"Math": 75, "Science": 95}}
#
#
#
# Output:
# {    'Math': 245,    'Science': 250}
#
#
#
# Q18. Find Employees Eligible for a Bonus
# Write a program to create a new dictionary containing employees whose salary is greater than 40000 and experience is at least 2 years.
#
# Input:
# employees = {    "Rahul": {"salary": 50000, "experience": 3},    "Amit": {"salary": 35000, "experience": 4},    "Sneha": {"salary": 45000, "experience": 2},    "Priya": {"salary": 60000, "experience": 1}}
#
#
#
# Output:
# {    'Rahul': {'salary': 50000, 'experience': 3},    'Sneha': {'salary': 45000, 'experience': 2}}
#
#
#
# Q19. Find Common Keys with Different Values
# Write a program to find the keys that exist in both dictionaries but have different values.
#
# Input:
# dict1 = {    "A": 10,    "B": 20,    "C": 30,    "D": 40}dict2 = {    "A": 10,    "B": 25,    "C": 35,    "E": 50}
#
#
#
# Output:
# {    'B': (20, 25),    'C': (30, 35)}
#
#
#
# Q20. Convert a List of Tuples into a Dictionary
# Write a program to convert the given list of tuples into a dictionary.
#
# Input:
# data = [    ("Python", 90),    ("Java", 85),    ("SQL", 80),    ("HTML", 75)]
#
#
#
# Output:
# {    'Python': 90,    'Java': 85,    'SQL': 80,    'HTML': 75}
