# Q.1. Check Palindrome Number

#
# def check(num):
#     og = num
#     rev = 0
#
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num //= 10
#     return og == rev
#
#
# result = check(121)
# print(result)


# Q.2. Check Armstrong Number


# def arm(num):
#     a = len(str(num))
#     total = 0
#     temp = num
#
#     while temp > 0:
#         digit = temp % 10
#         total += digit**a
#         temp //= 10
#
#     return num == total
#
#
# result = arm(153)
# print(result)


# Q.3. Check Prime Number


# def prime(num):
#     i = 1
#     count = 0
#     while i <= num:
#         if num % i == 0:
#             count += 1
#         i += 1
#     return count <= 2
#
#
# result = prime(29)
# print(result)


# Q.4. Check Perfect Number


# def is_perfect(num):
#
#     total = 1
#     i = 2
#     while i * i <= num:
#         if num % i == 0:
#             total += i
#             if i != num // i:
#                 total += num // i
#         i += 1
#     return total == num
#
#
# print(is_perfect(28))


# Q.5. Check Strong Number


# def is_strong(num):
#
#     fact = [1] * 10
#     for i in range(1, 10):
#         fact[i] = fact[i - 1] * i
#
#     original = num
#     total = 0
#     while num > 0:
#         total += fact[num % 10]
#         num //= 10
#     return total == original
#
#
# print(is_strong(145))

# Q.6.  Reverse a Number

#
# def reverse(num):
#     og = num
#     rev = 0
#
#     while og > 0:
#         digit = og % 10
#         rev = rev * 10 + digit
#         og //= 10
#
#     return rev
#
#
# result = reverse(48261)
# print(result)


# Q.7.  Sum of Digits


# def sum(num):
#     total = 0
#     while num > 0:
#         total += num % 10
#         num //= 10
#     return total
#
#
# result = sum(5832)
# print(result)


# Q.8. Count Even Digits


# def even(num):
#     count = 0
#     a = 0
#     while num > 0:
#         a = num % 10
#         if a % 2 == 0:
#             count += 1
#         num //= 10
#     return count
#
#
# result = even(1234568)
# print(result)


# Q.9. Find Largest Digit


# def largest(num):
#     l = 0
#     a = 0
#     while num > 0:
#         a = num % 10
#         if a > l:
#             l = a
#         num //= 10
#     return l
#
#
# result = largest(583921)
# print(result)


# Q.10. Find Second-Largest Unique Digit


# def second_largest_digit(num):
#     num = abs(num)
#     largest = second = -1
#
#     while num > 0:
#         d = num % 10
#         if d > largest:
#             second = largest
#             largest = d
#         elif largest > d > second:
#             second = d
#         num //= 10
#     return second
#
#
# result = second_largest_digit(998531)
# print(result)
