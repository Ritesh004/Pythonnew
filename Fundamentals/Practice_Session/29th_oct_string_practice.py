# 1. Count the Number of Vowels
# Write a program to count how many vowels (a, e, i, o, u) are present in a string.
# Input: s = "Programming"
# Output: 3

# s = "Programming"
# count = 0
# for i in s:
#     if i in "aeiou":
#         count += 1
# print(count)

# 2. Reverse a String
# Reverse the given string without using slicing (s[::-1]).
# Input: s = "python"
# Output: "nohtyp"

# s = "python"
# for i in range(len(s) - 1, -1, -1):
#     print(s[i], end="")

# 3. Check for a Palindrome
# Check whether a string reads the same forward and backward. Ignore letter case.
# Input: s = "Madam"
# Output: True

# s = "Madam"
# rev = ""
# for i in range(len(s) - 1, -1, -1):
#     rev += s[i]
# if rev.lower() == s.lower():
#     print(True)
# else:
#     print(False)


# 4. Count Words in a String
# Count the number of words in a sentence.
# Input: s = "Python is easy to learn"
# Output: 5

# s = "Python is easy to learn"
# count = 0
# words = s.split()
# count = len(words)
# print(count)

# 5. Character Frequency
# Count how many times a given character appears in a string.
# Input: s = "banana", ch = "a"
# Output: 3

# s = "banana"
# count = 0
# ch = "a"
# for i in range(len(s)):
#     if s[i] == ch:
#         count += 1
# print(count)

# 6. Remove All Spaces
# Create a new string after removing all spaces from the given string.
# Input: s = "learn python daily"
# # Output: "learnpythondaily"
# s = "learn python daily"
# a = s.replace(" ", "")
# print(a)

# 7. Find the First and Last Character
# Print the first and last character of a non-empty string.
# Input: s = "interview"
# Output: First = "i", Last = "w"

# s = "interview"
# first = s[0]
# last = s[-1]
# print("first:", first, " last:", last)
#
# 8. Count Uppercase and Lowercase Letters
# Count uppercase letters and lowercase letters separately.
# Input: s = "PyThOn"
# Output: Uppercase = 3, Lowercase = 3

# s = "PyThOn"
# upper = 0
# lower = 0
# for i in s:
#     if i.isupper():
#         upper += 1
#     else:
#         lower += 1
# print("Uppercase:", upper, " lowercase:", lower)


# 9. Check Whether Two Strings Are Anagrams
# Check whether two strings contain the same letters with the same frequencies. Ignore case.
# Input: s1 = "listen", s2 = "silent"

# s1 = "listen"
# s2 = "silent"
# if sorted(s1.lower()) == sorted(s2.lower()):
#     print(True)
# else:
#     print(False)


# 10. Find the Longest Word
# Find and print the longest word in a sentence. If there is a tie, print the first longest word.
# Input: s = "Python makes coding enjoyable"
# Output: "enjoyable"


# 11. Remove Duplicate Characters
# Remove repeated characters while preserving the first occurrence of each character.
# Input: s = "programming"
# Output: "progamin"
#
# 12. Find the First Non-Repeating Character
# Print the first character that occurs exactly once. If no such character exists, print None.
# Input: s = "aabbcddee"
# Output: "c"

# 13. Check Whether a String Contains Only Digits
# Check whether every character in the string is a digit.
# Input: s = "202610"
# Output: True
#
# 14. Count Occurrences of a Substring
# Count how many times a substring occurs in a string, including overlapping matches.
# Input: s = "aaaa", sub = "aa"
# Output: 3
#
# 15. Find the Most Frequent Character
# Find the character that appears most often. If there is a tie, print the one that appears first.
# Input: s = "success"
# Output: "s"
