# n = 5
# i = 1
# while i <= n:
#     print(i, end=" ")
#     i += 1


# n = 5
# i = 1
# while i <= n:
#     print(n, end=" ")
#     n -= 1


# n = 20
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1


# n = 20
# i = 1
# while i <= n:
#     if i % 2 != 0:
#         print(i, end=" ")
#     i += 1

# n = 5
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# print(sum)


# n = 4
# i = 1
# while i <= 10:
#     print(n * i, end=" ")
#     i += 1


# n = 5043
# i = n
# count = 0
# while i != 0:
#     i = i // 10
#     count += 1
# print("Total digits in number are: ", count)

# n = 5043
# i = n
# sum = 0
# while i != 0:
#     sum += i % 10
#     i = i // 10
# print("Sum: ", sum)


# n = 5043
# i = n
# rev = 0
# while i != 0:
#     rem = i % 10
#     rev = rev * 10 + rem
#     i = i // 10
# print("Reverse no.: ", rev)


# n = 5043
# i = 1
# last_digit = n % 10
# print("Last digit:", last_digit)
# while n > 10:
#     n = n // 10
# print("first digit:", n)

# n = int(input("Enter the digit: "))
# i = 1
# while i <= n:
#     print("hi", end=" ")
#     i += 1


# while True:
#     n = int(input("Enter the number: "))
#     if n > 0:
#         print(n)
#         break


# n = int(input("Enter the number: "))
# i = 1
# fact = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("factorial: ", fact)


# n = int(input("Enter the number: "))
# i = 1
# count = 0
# while i <= n:
#     if n % i == 0:
#         count += 1
#     i += 1
# if count == 2:
#     print("The number is prime")
# else:
#     print("The number is not a prime")


# n = int(input("Enter the number: "))
# i = n
# rev = 0
# while i != 0:
#     rem = i % 10
#     rev = rev * 10 + rem
#     i //= 10
# if rev == n:
#     print("Palindrome")

# n = 153
# i = n
# sum = 0
# while i > 0:
#     digit = i % 10
#     sum += digit**3
#     i //= 10
# if sum == n:
#     print("Armstrong")
# else:
#     print("Not armstrong")


# n = 123645
# i = n
# max = 0
# digit = 0
# while i > 0:
#     digit = i % 10
#     if digit > max:
#         max = digit
#     i //= 10
# print("max digit:", max)


# n = 123645
# i = n
# min = 10
# while i > 0:
#     digit = i % 10
#     if digit < min:
#         min = digit
#     i //= 10
# print("min digit:", min)


# n = 1234567
# i = n
# ecount = 0
# ocount = 0
# while i != 0:
#     digit = i % 10
#     if digit % 2 == 0:
#         ecount += 1
#     else:
#         ocount += 1
#     i //= 10
# print("Even no.:", ecount)
# print("Odd no.:", ocount)


# a = 0
# b = 1
# i = 1
# while i <= 10:
#     print(a, end=" ")
#     a, b = b, a + b
#     i += 1


# n = 4
#
# base = 3
# a = base
# i = 1
# while i <= n:
#     a *= base
#     i += i
# print(a)

# 26. Decimal to binary
# Convert a positive decimal integer to binary using repeated division by 2.
# Sample / expected result: n = 10 → 1010
#
# 27. Perfect number
# Check whether a positive number equals the sum of its proper divisors.
# Sample / expected result: n = 6 → Perfect number
