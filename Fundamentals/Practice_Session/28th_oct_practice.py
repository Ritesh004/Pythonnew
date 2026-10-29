# n = [16, 17, 4, 3, 5, 2]
# a = []
# max = float("-inf")
#
# for i in range(len(n) - 1, -1, -1):
#     if n[i] > max:
#         a.append(n[i])
#         max = n[i]
# print(a)


# 1. Replace each value with its sign
# Create a new list where each positive number becomes 1, each negative number becomes -1, and each zero stays 0.
#
# a = [5, -3, 0, 8, -1]
# b = []
# for i in a:
#     if i > 0:
#         b.append(1)
#     elif i < 0:
#         b.append(-1)
#     else:
#         b.append(0)
# print(b)


# 02. Count values between two limits
# Count how many list elements fall within the inclusive range low to high.
# Input: values = [2, 8, 5, 11, 7, 3]

# a = [2, 8, 5, 11, 7, 3]
# low = 4
# high = 8
# count = 0
# for i in a:
#     if i > low and i <= high:
#         count += 1
# print(count)


# 03. Remove all occurrences of a chosen value
# Return a new list containing every element except the chosen value. Preserve the original order.
# Input: values = [3, 1, 3, 5, 2, 3], target = 3


# a = [3, 1, 3, 5, 2, 3]
# t = 3
# b = []
# for i in a:
#     if i != t:
#         b.append(i)
# print(b)


# 04. Insert a value after every matching element
# Return a new list with marker inserted immediately after every occurrence of target.
# Input: values = [2, 5, 2, 7], target = 2, marker = 0
# Output: [2, 0, 5, 2, 0, 7]

# values = [2, 5, 2, 7]
# v = []
# target = 2
# marker = 0
# for i in values:
#     v.append(i)
#     if i == target:
#         v.append(marker)
# print(v)


# 05. Find the index of the last occurrence
# Return the index of the final occurrence of target. Return -1 if target is not present.
# Input: values = [4, 7, 2, 7, 9], target = 7
# Output: 3

# 06. Count adjacent changes
# Count how many times two neighboring elements are different.
# Input: [1, 1, 3, 3, 2, 5, 5]
# Output: 3


# 07. Check whether every element is unique
# Return True if no value appears more than once; otherwise return False. Do not use set().
# Input: [4, 7, 1, 9]
# Output: True


# 08. Find the first repeated value
# Scan from left to right and return the first value whose current occurrence has appeared earlier. Return None if no
# value repeats.
# Input: [6, 2, 4, 2, 6]
# Output: 2


# 09. Create a list of elements at odd indexes
# Return a new list containing elements at indexes 1, 3, 5, and so on.
# Input: [10, 20, 30, 40, 50, 60]
# Output: [20, 40, 60]

# a = [10, 20, 30, 40, 50, 60]
# b = []
# for i in range(len(a)):
#     if i % 2 == 1:
#         b.append(a[i])
# print(b)


# 10. Swap each neighboring pair
# Swap elements in pairs. If the list has an odd number of elements, leave the final element in place.
# Input: [1, 2, 3, 4, 5]
# Output: [2, 1, 4, 3, 5]
# 11. Find the middle element(s)
# Return the middle element for an odd-length list, or the two middle elements for an even-length list.
# Input: [8, 3, 6, 1, 9, 4]
# Output: [6, 1]
# 12. Count how many elements are greater than the previous element
# Starting from the second element, count values that are greater than the element immediately before them.
# Input: [2, 5, 3, 4, 4, 8]
# Output: 3
