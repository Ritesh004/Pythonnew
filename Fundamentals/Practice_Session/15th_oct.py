# for i in range(5):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# n = 4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j * i, end=" ")
#     print()

# n = 4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j**2, end=" ")
#     print()

# n = 4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(chr(64 + j) + str(j), end=" ")
#     print()

# n = 4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j == i:
#             print("*", end=" ")
#         else:
#             print(chr(64 + j), end=" ")
#     print()


# n = 4
#
# for i in range(1, n + 1):
#     a = 65
#     num = 1
#     for j in range(1, i + 1):
#         if j % 2 == 1:
#             print(num, end=" ")
#             num += 1
#         else:
#             print(chr(a), end=" ")
#             a += 1
#     print()


# n = 4
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(chr(64 + j) + str(j), end=" ")
#     print()

# for i in range(1, 5):
#     n = 1
#     for j in range(1, i + 1):
#         if i >= 2:
#             if j % 2 == 1:
#                 print(n, end=" ")
#                 n += 1
#             else:
#                 print("*", end=" ")
#         else:
#             print("*", end=" ")
#     print()


# for i in range(5):
#     for j in range(5):
#         if i == 0 or j == 0 or j == 4 or i == 4:
#             print(chr(65), end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#


# a = 65
# for i in range(6):
#     for j in range(i):
#         print(chr(a), end=" ")
#         a += 1
#     print()

# 7. Number-Star Square
# Input: n=4
# Output:
# 1 * 1 *
# * 1 * 1
# 1 * 1 *
# * 1 * 1


# 8. Alphabet Ladder
# Input: n=5
# Output:
# A
# B C
# D E F
# G H I J
# K L M N O
#
# n = 1
# for i in range(5):
#     for j in range(i):
#         if j % 2 == 1:
#             print(n, end=" ")
#             n += 1
#         else:
#             print("*", end=" ")
#
#     print()


# 9. Number-Star Pyramid
# Input: n=4
# Output:
# 1*
# 2 * 2
# 3 * * 3
# 4 * * * 4

# n = 4
#
# for i in range(1, n + 1):
#     print(i, end="")
#
#     if i == 1:
#         print("*", end="")
#     else:
#         for j in range(i - 1):
#             print(" *", end="")
#         print(" " + str(i), end="")
#
#     print()
#
# #
# 10. Alphabet Pyramid
# Input: n=4
# Output:
# A
# ABA
# ABCBA
# ABCDCBA

# 11. Hollow Alphabet Triangle
# Input: n=5
# Output:
# A
# A    B
# A       C
# A          D
# A B C D E
#
# 12. Continuous Alpha Numeric
# Input: n=4
# Output:
# A1
# B2 C3
# D4 E5 F6
# G7 H8 I9 J10
#
# 13. Zigzag Alpha Pattern
# Input: n=4
# Output:
# A
# B A
# C B A
# D C B A

# 7th
# i = 1
# while i <= 4:
#     j = 1
#     while j <= 4:
#         if (i + j) % 2 == 0:
#             print(1, end=" ")
#         else:
#             print("*", end=" ")
#         j += 1
#     print()
#     i += 1

# 10

for i in range(5):
    a = 65
    for j in range(i):
        if j == i or j == 1 or i == 5:
            print(chr(a), end=" ")
            a += 1
        else:
            print(" ", end=" ")
    print()
