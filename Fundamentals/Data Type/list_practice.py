# # 1. Create a list containing 10 integers and display all the elements of the list.
# print("Q.1")
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l)
# print()
# # 2. Create a list of 5 student names and display each name using a loop.
# print("Q.2")
#
# l1 = ["DEF", "XYZ", "ABC", "LMN", "GHI"]
# for i in l1:
#     print(i, end=" ")
# print()
# # 3. Create a list of 10 numbers and calculate the sum of all elements without using the sum() function.
# print("Q.3")
#
# lx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum(lx))
# # 4. Create a list of numbers and find the largest element without using the max() function.
# print("Q.4")
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# largest = x[0]
# for i in x:
#     if i > largest:
#         largest = i
# print("The largest number is: ", largest)
# print()
# # 5. Create a list of numbers and find the smallest element without using the min() function.
# print("Q.5")
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("The minmum value is: ")
# print(min(x))
# print()
# # 6. Create a list of numbers and count how many elements are present without using the len() function.
# print("Q.6")
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# count = 0
# for i in x:
#     count += 1
# print("The lenth of list is:", count)
# print()
# # 7. Create a list of integers and count how many numbers are even and how many are odd.
# print("Q.7")
# x = [1, 2, 3, 4, 5, 7, 3, 6, 7, 8, 9, 10]
# count1 = 0
# count2 = 0
# for i in x:
#     if i % 2 == 0:
#         count1 += 1
#     else:
#         count2 += 1
# print("Even:", count1)
# print("Odd:", count2)
# print()
# # 8. Create a list of numbers and display only the positive elements.
# print("Q.8")
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in l:
#     if i % 2 == 0:
#         print(i, end=" ")
# print()

# # 9. Create a list of numbers and display only the negative elements.
# print("Q.9")
# l = [1, 2, -1, -2, 3, 4, -9, -10, 5, 7, 6]
# for i in l:
#     if i < 0:
#         print(i, end=" ")
# print()

# # 10. Create a list of integers and calculate the average of all elements.
# print("Q.10")
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# print(sum(l) / len(l))
# print()
#
# # 11. Create a list of numbers and search for a given element. Display whether the element is present in the list.
# print("Q.11")
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# if 9 in l:
#     print("Yes")
# else:
#     print("No")
# print()

# # 12. Create a list of numbers and count how many times a given element occurs without using the count() method.
# print("Q.12")
# l = [1, 2, 5, 4, 5, 6, 5, 8]
#
# a = int(input("Enter the number:"))
# count = 0
# for i in l:
#     if a == i:
#         count += 1
# print("The number occured", count, "times")
# print()
# # 13. Create a list of numbers and remove all duplicate elements while preserving the original order.
# print("Q.13")
# l = [1, 1, 2, 3, 4, 3, 5, 6, 7, 4, 8, 9]
# for i in l:
#     if l.count(i) > 1:
#         l.remove(i)
# print(l)
# print()
# # 14. Create a list of integers and create a new list containing only the unique elements.
# print("Q.14")
# l = [1, 1, 2, 3, 4, 5, 3, 6, 7, 8, 5, 6, 0, 10]
# a = []
# for i in l:
#     if l.count(i) < 2:
#         a.append(i)
# print(a)
# print()
# # 15. Create a list of numbers and reverse the list without using the reverse() method or slicing.
# print("Q.15")
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# a = 0
# b = len(l) - 1
# while a < b:
#     l[a], l[b] = l[b], l[a]
#     a += 1
#     b -= 1
# print(l)
# # 16. Create a list of numbers and sort the elements in ascending order without using the sort() method.
# print("Q.16")
# l = [64, 34, 25, 12, 22, 11]
# n = len(l)
# for i in range(n):
#     for j in range(n - 1):
#         if l[j] > l[j + 1]:
#             l[j], l[j + 1] = l[j + 1], l[j]
# print(l)
# # 17. Create a list of numbers and sort the elements in descending order without using the sort() method.
# print("Q.17")
# l = [64, 34, 25, 12, 22, 11]
# n = len(l)
# for i in range(n):
#     for j in range(n - 1):
#         if l[j] < l[j + 1]:
#             l[j], l[j + 1] = l[j + 1], l[j]
# print(l)
# # 18. Create a list of integers and create two separate lists containing even and odd numbers.
# print("Q.18")
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = []
# odd = []
# for i in l:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)
# # 19. Create a list of numbers and create a new list containing the squares of all elements.
# print("Q.19")
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# a = []
# for i in l:
#     a.append(i**2)
# print(a)
# 20. Create a list of integers and create a new list containing the cubes of all elements.
print("Q.20")
l = [1, 2, 3, 4, 5, 6, 7, 8]
a = []
for i in l:
    a.append(i**3)
print(a)
# 21. Create a list of numbers and replace every negative number with zero.

# 22. Create a list of integers and replace every even number with its square.

# 23. Create a list of numbers and remove all occurrences of a given element without using the remove() method.

# 24. Create a list of integers and find the second-largest element without using the sort() or sorted() functions.

# 25. Create a list of integers and find the second-smallest element without using the sort() or sorted() functions.

# 26. Create a list of numbers and display the elements along with their indexes without using the enumerate() function.

# 27. Create a list of numbers and separate the elements at even indexes and odd indexes into two different lists.

# 28. Create a list of integers and move all zeros to the end while maintaining the order of the remaining elements.

# 29. Create two lists of integers and combine them into a single list without using the extend() method.

# 30. Create two lists and find the common elements between them without using sets.

# 31. Create two lists of integers and find the elements that are present in the first list but not in the second list.

# 32. Create two lists and check whether both lists contain exactly the same elements in the same order.

# 33. Create a list of integers and check whether the list is sorted in ascending order.

# 34. Create a list of integers and rotate all elements one position to the left.

# 35. Create a list of integers and rotate all elements one position to the right.

# 36. Create a list of integers and move the first element to the end of the list.

# 37. Create a list of integers and find all pairs of elements whose sum is equal to a given number.

# 38. Create a list of integers and find the frequency of every element without using the count() method.

# 39. Create a list of student marks and display the marks that are greater than the average marks.

# 40. Create a list of student marks and count how many students passed and failed, considering 40 as the passing mark.

# 41. Create a list of employee salaries and increase every salary by 10%.

# 42. Create a list of product prices and create a new list containing only prices greater than ₹500.

# 43. Create a list of words and find the word with the maximum length without using the max() function.

# 44. Create a list of strings and display only those strings that start with a vowel.

# 45. Create a list of strings and create a new list containing the first character of every string.

# 46. Create a list of words and count how many words contain more than five characters.

# 47. Create a nested list containing the marks of three students in three subjects each. Calculate the total marks of every student.

# 48. Create a nested list containing integers and convert it into a single flat list.

# 49. Create a list of integers and split it into two lists: one containing the first half and the other containing the second half.

# 50. Create a list of integers and find the longest consecutive sequence of increasing elements present in the list.
