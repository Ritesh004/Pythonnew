# i = 1
# while i > 0:
#     if i % 7 == 0:
#         break
#     else:
#         print(i, end=" ")
#     i += 1

#
# n = 9875
#
# while n >= 10:
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n //= 10
#     n = sum
# print(sum)


# n = 43000
# count = 0
# while n > 10:
#     if n % 10 == 0:
#         count += 1
#     n //= 10
# print(count)


# n = int(input("Enter binary number: "))
# base = 1
# decimal = 0
# temp = n
# while temp > 0:
#     digit = temp % 10
#     decimal += digit * base
#     base *= 2
#     temp //= 10
# print(decimal)


# 05 First repeated digit from the right
# Scan a positive integer from right to left and report the first digit encountered for the second time.
# Sample / expected result: Input: 128321 → Output: 2
#
# 06 Check increasing digits
# Check whether every digit is greater than the digit immediately before it, reading left to right.
# Sample / expected result: Input: 13579 → Output: Increasing
#
# n = 13579
# prev = 10
# flag = True
#
# while n > 0:
#     digit = n % 10
#
#     if digit >= prev:
#         flag = False
#         break
#
#     prev = digit
#     n = n // 10
#
# if flag:
#     print("Increasing")
# else:
#     print("Not Increasing")


#
# 07 Product of digits
# Calculate the product of all digits of a positive integer.
# Sample / expected result: Input: 234 → Output: 24
#
# 08 Count digits greater than 5
# Count how many digits in a number are greater than 5.
# Sample / expected result: Input: 586729 → Output: 4
#
# 09 Print digits as words in reverse order
# For a number containing digits 0–9, print each digit as a word in reverse order.
# Sample / expected result: Input: 204 → Output: Four Zero Two
#
#
#
#
#
#
#


# n = int(input("Enter the number: "))
# dig = 0
# pro = 1
# while n > 0:
#     dig = n % 10
#     pro *= dig
#     n //= 10
# print(pro)

# 10 Smallest power of 2 greater than N
# Starting from 1, repeatedly double a value until it becomes greater than the given number.
# Sample / expected result: Input: 20 → Output: 32
#
# 11 HCF by repeated subtraction
# Find the HCF of two positive integers by subtracting the smaller from the larger until both are equal.
# Sample / expected result: Input: 18, 12 → Output: 6
#
# 12 Alternating sum
# Calculate 1 − 2 + 3 − 4 + ... up to n using a while loop.
# Sample / expected result: Input: 6 → Output: -3
#
#

total = 0
i = 1
n = int(input("Enter the number: "))
while i <= n:
    if i % 2 == 0:
        total -= i
    else:
        total += i
    i += 1
print(total)
