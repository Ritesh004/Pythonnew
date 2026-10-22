# Mixed Spiral Style
# Input: n=5
# Output:
# A B C D E
# P Q R S F
# O X Y T G
# N W V U H
# M L K J I

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(chr(65), end=" ")
#     print()

# n = 5
# a = [["" for j in range(n)] for i in range(n)]
#
# ch = 65  # ASCII value of 'A'
#
# top = 0
# bottom = n - 1
# left = 0
# right = n - 1
#
# while top <= bottom and left <= right:
#     # Left to right
#     for j in range(left, right + 1):
#         a[top][j] = chr(ch)
#         ch += 1
#     top += 1
#
#     # Top to bottom
#     for i in range(top, bottom + 1):
#         a[i][right] = chr(ch)
#         ch += 1
#     right -= 1
#
#     # Right to left
#     if top <= bottom:
#         for j in range(right, left - 1, -1):
#             a[bottom][j] = chr(ch)
#             ch += 1
#         bottom -= 1
#
#     # Bottom to top
#     if left <= right:
#         for i in range(bottom, top - 1, -1):
#             a[i][left] = chr(ch)
#             ch += 1
#         left += 1
#
# for i in range(n):
#     for j in range(n):
#         print(a[i][j], end=" ")
#     print()


#
# n = 5
# arr = [["" for j in range(n)] for i in range(n)]
#
# top = 0
# bottom = n - 1
# left = 0
# right = n - 1
# ch = 65
#
# while top <= bottom and left <= right:
#     for j in range(left, right + 1):
#         arr[top][j] = chr(ch)
#         ch += 1
#     top += 1
#     for i in range(top, bottom + 1):
#         arr[i][right] = chr(ch)
#         ch += 1
#     right -= 1
#     for j in range(right, left - 1, -1):
#         arr[bottom][j] = chr(ch)
#         ch += 1
#     bottom -= 1
#     for i in range(bottom, top - 1, -1):
#         arr[i][left] = chr(ch)
#         ch += 1
#     left += 1
# for row in arr:
#     print(*row)


# 1. Centered Number Mirror Pyramid
# Input: n = 4
# Expected Output:
#           1
#        2 3 2
#      3 4 5 4 3
#    4 5 6 7 6 5 4

# n = 4
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#
#     for j in range(i):
#         print(i + j, end=" ")
#
#     for j in range(i - 2, -1, -1):
#         print(i + j, end=" ")
#
#     print()

# 18. Alphabet Border Pattern
# Input: n = 5
# Output:
# A B C D E
# A       E
# A       E
# A       E
# A B C D E


# 19. Mixed Triangle
# Input: n = 4
# Output:
# 1
# A B
# 1 2 3
# A B C D
#
# 20. Special Character Pyramid
# Input: n = 4
# Output:
# &
# & &
# & & &
# & & & &
#
# 2. Centered Alphabet Mirror Pyramid
# Input: n = 4
# Expected Output:
#        A
#     B C B
#   C D E D C
# D E F G F E D
# Interview focus: Use row-based starting letters and mirror the row around its center.
#
#
# 3. Alpha-Numeric Hourglass
# Input: n = 4
# Expected Output:
# A1 B2 C3 D4
#     A1 B2 C3
#       A1 B2
#         A1
#      A1 B2
#    A1 B2 C3
# A1 B2 C3 D4
# Interview focus: Create a shrinking top half and an expanding bottom half.
#
# 4. Number-Symbol Sandglass
# Input: n = 4
# Expected Output:
# 1 # 2 # 3 # 4
#     1 # 2 # 3
#        1 # 2
#           1
#       1 # 2
#     1 # 2 # 3
# 1 # 2 # 3 # 4
# Interview focus: Alternate numbers and # while changing row width in both directions.
