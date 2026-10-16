# for i in range(4):
#     n = 1
#     a = 65
#     for j in range(4):
#         if j % 2 == 1:
#             print(n, end=" ")
#             n += 1
#         else:
#             print(chr(a), end=" ")
#             a += 1
#     print()

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if i >= 2:
#             if j % 2 == 1:
#                 print("#", end=" ")
#             else:
#                 print("*", end=" ")
#         else:
#             print("*", end=" ")
#     print()
#
# n = 1
# a = 65
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if i % 2 == 1:
#             print(chr(a), end=" ")
#         else:
#             print(n, end=" ")
#     if i % 2 == 1:
#         a += 1
#     else:
#         n += 1
#
#     print()

# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or i == 5 or j == 1 or j == 5:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# for i in range(4):
#     for j in range(4):
#         if (i + j) % 2 == 0:
#             print(chr(65), end=" ")
#         else:
#             print(1, end=" ")
#     print()

# n = 10
# for i in range(4, 0, -1):
#     for j in range(1, i + 1):
#         print(n, end=" ")
#         n -= 1
#     print()


# n = 68
# for i in range(4, 0, -1):
#     a = n
#     for j in range(1, i + 1):
#         print(chr(a), end=" ")
#         a -= 1
#     n -= 1
#     print()


# for i in range(4):
#     for j in range(4 - i):
#         if i == 2:
#             print("B", end=" ")
#         else:
#             print(chr(68 - i - j), end=" ")
#     print()

# n = 1
# a = 65
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(chr(a) + str(i * j), end=" ")
#     a += 1
#     print()

# i = 1
# while i <= 4:
#     j = 1
#     a = 65
#     while j <= i:
#         if j == i:
#             print("@", end=" ")
#         else:
#             print(chr(a), end=" ")
#             a += 1
#         j += 1
#     print()
#     i += 1

# for i in range(1, 5):
#     a = 65
#     for j in range(1, i + 1):
#         if i == j:
#             print("@", end=" ")
#         else:
#             print(chr(a), end=" ")
#             a += 1
#     print()


# 1. Binary Alpha Pattern
# Input: n=4
# Output:
# A
# 0 A
# 1 0 A
# 0 1 0 A
#
# 2. Character Wave
# Input: n=5
# Output:
# A
# A B
# A B C
# A B
# A
#
# 3 Number-Alpha Palindrome
# Input: n=4
# Output:
# 1
# 1A1
# 1A2A1
# 1A2B2A1
#


n = 4

for i in range(n):
    if i == 0:
        print(1)
    else:
        for j in range(1, i + 1):
            print(j, end="")
            if j < i:
                print(chr(64 + j), end="")

        for j in range(i, 0, -1):
            if j == i:
                print(chr(64 + j - 1), end="")
            print(j, end="")

        print()
