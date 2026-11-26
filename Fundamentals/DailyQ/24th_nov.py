# Q.1. Check Palindrome Number
# print('Q.1.')
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
# print('Q.2.')


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
# print('Q.3.')


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
# print('Q.4.')


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

# print('Q.5.')

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
# print('Q.6.')

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
# print('Q.7.')


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
# print('Q.8.')


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
# print('Q.9.')


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
# print('Q.10.')


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


# -----------------Section B – Number Logic & Mathematical Operations------------------------------------------

# Q.11. Check Harshad Number
# print('Q.11.')


# def is_harshad(num):
#
#     digit_sum = 0
#     temp = num
#     while temp > 0:
#         digit_sum += temp % 10
#         temp //= 10
#     return num % digit_sum == 0
#
#
# result = is_harshad(18)
# print(result)


# Q.12.  Check Automorphic Number
# print('Q.12.')


# def is_automorphic(num):
#
#     square = num * num
#     temp = num
#
#     while temp > 0:
#         if temp % 10 != square % 10:
#             return False
#         temp //= 10
#         square //= 10
#     return True
#
#
# result = is_automorphic(25)
# print(result)


# Q.13.  Find GCD of Two Numbers
# print('Q.13.')


# def find_gcd(a, b):
#     for i in range(min(a, b), 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i
#
#
# result = find_gcd(24, 36)
# print(result)


# Q.14. Find LCM of Two Numbers


# Q.15.  Calculate Power
# print('Q.15.')


# def calculate_power(base, exponent):
#     total = 1
#     for _ in range(exponent):
#         total *= base
#     return total
#
#
# result = calculate_power(3, 4)
# print(result)


# ------------------------Section C – Series & Combined Operations------------------------------------------


# Q.16.  Generate Fibonacci Series
# print('Q.16.')


# def fibonacci(n):
#     series = []
#     a, b = 0, 1
#     for _ in range(n):
#         series.append(a)
#         a, b = b, a + b
#     return series
#
#
# result = fibonacci(7)
# print(result)


# Q.17.  Find Factorial
# print('Q.17.')


# def factorial(num):
#     fact = 1
#     for i in range(2, num + 1):
#         fact *= i
#     return fact
#
#
# result = factorial(5)
# print(result)


# Q.18. Count Digits
# print('Q.18.')


# def count_digits(num):
#     num = abs(num)
#     if num == 0:
#         return 1
#
#     count = 0
#     while num > 0:
#         count += 1
#         num //= 10
#     return count
#
#
# result = count_digits(90752)
# print(result)


# Q.19. Sum of Even and Odd Digits
# print('Q.19.')


# def digit_sums(num):
#     digits = [int(d) for d in str(abs(num))]
#     even_sum = sum(d for d in digits if d % 2 == 0)
#     odd_sum = sum(d for d in digits if d % 2 != 0)
#     return (even_sum, odd_sum)
#
#
# result = digit_sums(123456)
# print(result)


# Q.20. Check Co-Prime Numbers
print("Q.20.")


def are_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1


result = are_coprime(8, 15)
print(result)
