# 1. Extract digits from a string
# Given a string containing letters, digits, and symbols, return only the digits in their original order.
# Input: "ab3c09#x2"
# Output: "3092"

# s = "ab3c09#x2"
# for i in range(len(s)):
#     if s[i] in "1234567890":
#         print(s[i], end="")


# 2. Extract letters only
# Return only alphabetic characters from a mixed string. Preserve their order.
# Input: "Py@th0n_3!"
# Output: "Python"

# s = "Py@th0n_3!"
# a = ""
# for ch in s:
#     if ch.isalnum():
#         a += ch
# print(a)

# 3. Check whether a string contains only digits
# Print True if every character in the string is a digit; otherwise print False.
# Input: "2026"
# Output: True

# s = "2026"
# print(s.isdigit())


# 4. Find the position of the second occurrence
# Return the index of the second occurrence of a given character. Return -1 if it occurs fewer than two times.
# Input: s = "banana", ch = "a"
# Output: 3

# s = "banana"
# ch = "a"
# count = 0
# for i in range(len(s)):
#     if ch == s[i]:
#         count += 1
# print(count)


# 5. Find the last occurrence without rfind
# Find the last index of a target character without using rfind().
# Input: s = "mississippi", ch = "s"
# Output: 6

# s = "mississippi"
# ch = "s"
# for i in range(len(s)):
#     if s[i] == ch:
#         a = i
# print(a)
#

# 6. Swap the first and last characters
# Create a new string by swapping the first and last characters. If the string has fewer than two characters, return it
# unchanged.
# Input: "coding"
# Output: "godinc"

# s = "coding"
#
# if len(s) > 2:
#     print(s[-1] + s[1:-1] + s[0])
# else:
#     print(s)

# 7. Move all digits to the end
# Rearrange a string so letters and other non-digit characters come first, followed by digits. Keep relative order within each
# group.
# Input: "a1b2c3!"
# Output: "abc!123"

# s = "a1b2c3!"
# dig = ""
# other = ""
# for i in s:
#     if i.isdigit():
#         dig += i
#     else:
#         other += i
# print(other + dig)


# 8. Move all uppercase letters to the front
# Move uppercase letters to the beginning and all other characters after them, preserving relative order.
# Input: "aBcDeF1"
# Output: "BDFace1"

# s = "aBcDeF1"
# upper = ""
# lower = ""
# for i in s:
#     if i.isupper():
#         upper += i
#     else:
#         lower += i
# print(upper + lower)


# 9. Remove punctuation
# Remove punctuation marks from a sentence while keeping letters, digits, and spaces.
# Input: "Hi, there! It's 2026."
# Output: "Hi there Its 2026"

# s = "Hi, there! It's 2026."
# for i in s:
#     if i.isalnum() or i.isspace():
#         print(i, end="")


# 11. Capitalize the first letter of every word manually
# Convert each word so its first character is uppercase and the remaining characters are lowercase, without using title().
# Input: "pYTHON iS FUN"
# Output: "Python Is Fun"

# s = "pYTHON iS FUN"
# a = s.split()
# for i in a:
#     print(i.capitalize(), end=" ")

# 12. Find the longest word length
# Return the length of the longest word in a sentence. Ignore punctuation attached to words.
# Input: "Python makes coding enjoyable!"
# Output: 9

# s = "Python makes coding enjoyable"
# a = s.split()
# longest = 0
# for i in a:
#     if len(i) > longest:
#         longest = len(i)
# print(longest)

# 13. Find the shortest word
#
# Return the shortest word in a sentence. If multiple words tie, return the first one.
# Input: "Learn to code with care"
# Output: "to"

# s = "Learn to code with care"
# a = s.split()
# short = 10
# for i in a:
#     if len(i) < short:
#         short = len(i)
#         b = i
# print(b)


# 14. Reverse the order of characters in each word
# Reverse each word but keep the words in their original positions.
# Input: "code every day"
# Output: "edoc yreve yad"

# s = "code every day"
# a = s.split()
# for i in a:
#     print(i[::-1], end=" ")


# 15. Keep only the first occurrence of each word
# Remove repeated words from a sentence, keeping the first occurrence and preserving word order. Treat matching as
# case-sensitive.
# Input: "go now go home now"
# Output: "go now home"

# s = "go now go home now"
# a = s.split()
# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# print(" ".join(c))

# 16. Count words beginning with a vowel
# Count how many words in a sentence begin with a vowel, ignoring letter case.
# Input: "An owl is under a tree"
# Output: 5

# s = "An owl is under a tree"
# a = s.split()
# count = 0
# for i in a:
#     if i[0] in "AEIOUaeiou":
#         count += 1
# print(count)


