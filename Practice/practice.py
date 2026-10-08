# for i in range(1, 11):
#     print(i)

# for i in range(10):
#     print(i)

# for _ in range(5):
#     print("Keep Practicing")

# for i in range(50, 56):
#     print(i)

# for i in range(1, 7):
#     print("Lap", i)

# for i in range(2, 21, 2):
#     print(i)

# for i in range(1, 20, 2):
#     print(i, end=" ")
# print()
#
# for i in range(5, 51, 5):
#     print(i, end=" ")
# print()
#
# for i in range(7, 71, 7):
#     print(i, end=" ")
# print()
#
# for i in range(100, 161, 10):
#     print(i, end=" ")

# for i in range(10, 0, -1):
#     print(i, end=" ")

# for i in range(5, -1, -1):
#     print(i, end=" ")

# for i in range(20, 1, -2):
#     print(i, end=" ")

# for i in range(30, 4, -5):
#     print(i, end=" ")

# sum = 0
# for i in range(1, 6):
#     sum = sum + i
# print(sum)


# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(sum, " Total itrations: ", i)

# sum = 0
# for i in range(2, 21, 2):
#     sum = sum + i
# print(sum)

# fact = 1
# for i in range(1, 6):
#     fact = fact * i
# print(fact)

# for i in range(1, 6):
#     print(i**2, end=" ")
# count = 0
# for i in range(1, 31, 3):
#     count += 1
# print(count)

# for i in range(1, 31):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, end=" ")

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, " is even")
#     else:
#         print(i, " is odd")


# for i in range(1, 21):
#     if i % 4 != 0:
#         print(i, end=" ")

# for i in range(1,16):
#     if i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)

# sum_e = 0
# sum_o = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         sum_e = sum_e + i
#     else:
#         sum_o = sum_o + i
# print("addition of even no. is: ", sum_e)
# print("addition of odd no, is: ", sum_o)


# count = 0
# for i in range(1, 51):
#     if i % 6 == 0:
#         count += 1
# print(count)

#
# sum1 = 0
# sum2 = 0
# for i in range(1, 21):
#     if i <= 10:
#         sum1 += i
#     else:
#         sum2 += i
# print(sum1)
# print(sum2)
# diff = 0
# print("diff=", sum2 - sum1)

# sum = 0
# count = 0
# for i in range(1, 16):
#     sum += i
#     count += 1
# print(sum / count)


# sum = 0
# for i in range(1, 11):
#     if i % 2 == 0:
#         sum += i
#     else:
#         sum -= i
# print(sum)


# a = 0
# sum = 0
# for i in range(1, 6):
#     a = i**3
#     sum += a
# print(sum, end=" ")

# a = 0
# for i in range(1, 6):
#     a += i
#     print(a, end=" ")
#
# count = 0
# for i in range(1, 31):
#     if i % 10 == 3 or i % 10 == 9:
#         count += 1
# print(count)
#

# a = 1
# for i in range(1, 25):
#     if 24 % i == 0:
#         print(i)

# for i in range(1, 6):
#     print(2 * i)
# # for i in range(1, 6):
# #     print(3 * i)
#
# Print a 3 × 3 grid of stars *** using nested for loops.

# a = 29
# count = 0
# flage = True
# for i in range(2, a):
#     if a % i == 0:
#         flage = False
#         break
# if flage == True:
#     print("is prime")
# else:
#     print("not prime")

# Print all prime numbers between 2 and 50 using nested loops.

# for i in range(2, 51):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i, end=" ")

# problem -3
# Sum of digits: given integer x = 4827

# x = 4827
# sum = 0
# for i in range(4):
#     rem = x % 10
#     sum += rem
#     x //= 10
# print(sum)

# a = 0
# b = 1
# for _ in range(10):
#     print(a, end=" ")
#     a, b = b, a + b


# Problem -
# Compute cumulative product of odds while skipping any number ending in 5.

a = 1
for i in range(21):
    if i % 2 != 0 and i % 10 != 5:
        a *= i
print(a)

# Problem -
# Count how many numbers from 1 to 100 have an odd number of factors
