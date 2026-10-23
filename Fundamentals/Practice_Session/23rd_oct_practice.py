# n = [11, 22, 33, 44, 55]
# a = len(n) // 2
# print(n[a])


# n = [15, 25, 35, 45, 55]
# a = len(n) - 2
# print(n[a])


# n = [10, 20, 30, 40]
# a = len(n) - 1
# n[a] = 90
# print(n)


# n = [2, 4, 6, 8, 10, 12]
# print(n[:4])


# n = [5, 10, 15, 20, 25, 30, 35]
# print(n[2:6])


# n = [1, 2, 3, 4, 5, 6, 7, 8]
# print(n[::2])


# n = [9, 8, 7, 6, 5]
# n.reverse()
# print(n)


# count = 0
# n = [7, 3, 7, 5, 7, 9]
# for i in n:
#     if i == 7:
#         count += 1
# print(count)


# n = [20, 40, 60, 80]
# n.append(100)
# print(n)


# n = [10, 20, 30, 40]
# n.insert(1, 50)
# print(n)


# n = [5, 15, 25, 35, 45]
# n.remove(25)
# print(n)


# n = [30, 60, 90, 120]
# print(n.index(90))


# n = [14, 3, 27, 8, 19]
# n.sort()
# print(n)


# n = [14, 3, 27, 8, 19]
# n.sort(reverse=True)
# print(n)


# n = [12, 7, 15, 20, 9, 18]
# a = []
# for i in n:
#     if i % 2 != 0:
#         a.append(i)
# print(a)

#
# n = [18, 42, 11, 67, 29]
# print(max(n))
# print(min(n))


# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
# print(list1+list2)


# list = [6, 3, 9, 1]
# for i in list:
#     if i == 9:
#         print("found")


# n = 5
# a = []
# for i in range(1, n + 1):
#     a.append(i**2)
# print(a)


a = 0
b = 0
l = [8, 3, 12, 12, 5, 9]
for i in l:
    if i > a:
        b = a
        a = i
    elif i < a and i > b:
        b = i
print(b)


# # 1. Initialize two variables to negative infinity instead of just 'a = 0'
# largest = float("-inf")
# second_largest = float("-inf")
#
# l = [8, 3, 12, 12, 5, 9]
#
# for i in l:
#     # 2. When you find a new largest number, shift the old one down
#     if i > largest:
#         second_largest = largest
#         largest = i
#     # 3. Check if the number fits strictly between the largest and second largest
#     elif i < largest and i > second_largest:
#         second_largest = i
#
# # 4. Print the second largest variable instead of the largest
# print(second_largest)


# 14. Separate even and odd values
# Keep the original order in both lists.
# Input: [7, 2, 9, 4, 6, 3]
# Output:
# Even: [2, 4, 6]
# Odd: [7, 9, 3]
#
# 15. Remove duplicates, preserve order
# Do not use a set.
# Input: [3, 1, 3, 2, 1, 4]
# Output: [3, 1, 2, 4]
