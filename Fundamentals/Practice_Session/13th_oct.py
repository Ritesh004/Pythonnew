# 1. Print numbers between 1 and N that are divisible by 8

# n = int(input("Enter the number: "))
# for i in range(n):
#     if i % 8 == 0:
#         print(i, end=" ")


# 2. Print the first N multiples of 6

# n = int(input("Enter the number: "))
# for i in range(1, n + 1):
#     print(6 * i)

# 3. Find the sum of numbers from 1 to N that are divisible by 3

# n = int(input("Enter the Number: "))
# sum = 0
# for i in range(1, n + 1):
#     if i % 3 == 0:
#         sum += i
# print(sum)
#
# 4. Count how many numbers from 1 to N are divisible by 4

# n = int(input("Enter the number: "))
# count = 0
# for i in range(1, n + 1):
#     if i % 4 == 0:
#         count += 1
# print(count)

# 5. Print numbers from N down to 1 that are divisible by 3

# n = int(input("Enter the number: "))
# for i in range(n, 1, -1):
#     if i % 3 == 0:
#         print(i, end=" ")

# 6. Find the sum of all digits greater than 4

# n = 583267
# sum = 0
# for i in str(n):
#     if int(i) > 4:
#         sum += int(i)
# print(sum)

# 7. Count digits smaller than 4
# Input: n = 583214

# n = 583214
# count = 0
# for i in str(n):
#     if int(i) < 4:
#         count += 1
# print(count)

# 8. Count how many digits are divisible by 3
# Input: n = 936427

# n = 936427
# count = 0
# for i in str(n):
#     if int(i) % 3 == 0:
#         count += 1
# print(count)


# 9. Find the sum of the first and last digit
# Input: n = 58329

# n = 58329
# a = n % 10
# b = n
# while b >= 10:
#     b //= 10
#
# sum = a + b
# print(sum)

# 10. Find the product of the first and last digit
# Input: n = 4236

# n = 4236
# a = n % 10
# b = n
# while b >= 10:
#     b //= 10
# mul = a * b
# print(mul)

# 11. Check whether a number has more even digits than odd digits
# Input: n = 24861
# n = 24861
# a = n
# count1 = 0
# count2 = 0
# while a > 0:
#     x = a % 10
#     if x % 2 == 0:
#         count1 += 1
#     else:
#         count2 += 1
#     a = a // 10
# if count1 > count2:
#     print("yes")
# else:
#     print("No")

# 12. Check whether every digit is non-zero
# Input: n = 58321

# 13. Count the number of factors that are even
# Input: n = 24
# Output: 6
#
# 14. Count the number of factors that are odd
# Input: n = 18
# Output: 3
#
# 15. Find the sum of even factors of a number
# Input: n = 12
# Output: 24
