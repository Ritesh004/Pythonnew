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
i = 1
ch = 65
while i in range(5):
    j = 1
    while j in range(5):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print(chr(ch), end=" ")
        ch += 1
        j += 1
    print()
    i += 1
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
