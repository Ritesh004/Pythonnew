# 16. Find Word-Boundary Matches
# Return the indexes where target starts as a complete word, not as part of a larger word.
# Input: s = "cat scatter catfish cat", target = "cat"
# Output: [0, 21]

# s = "cat scatter catfish  cat"
# t = "cat"
# index = 0
# op = []
# a = s.split(" ")
# for i in a:
#     if i == t:
#         op.append(index)
#     index += len(i) + 1
# print(op)


# 17. Longest Palindromic Substring
# Find the longest contiguous substring that is a palindrome. If tied, return the first one.
# Input: s = "babad"
# Output: "bab"


# 18. Minimum Deletions to Make Anagrams
# Find the minimum total number of character deletions needed to make two strings anagrams.
# Input: s1 = "cde", s2 = "abc"
# Output: 4

# s1 = "cde"
# s2 = "abc"
# count = 0
# for i in s1:
#     if i in s2:
#         s2 = s2.replace(i, "", 1)
#     else:
#         count += 1
# count += len(s2)
# print(count)

# for i in s1:
#     if i not in s2:
#         count += 1
# for i in s2:
#     if i not in s1:
#         count += 1
# print(count)


# 19. Validate an Identifier
# Check a Python-style identifier: it starts with a letter or underscore and contains only letters, digits, or underscores.
# Input: s = "_score2"
# Output: True

# s = "_score2"
# op = s.isidentifier()
# print(op)

# 20. Expand Encoded Repetition
# Decode a string where each single-digit count is followed by a character to repeat.
# Input: s = "3a2b4c"
# Output: "aaabbcccc"
#
# 21. Longest Word Made of Letters
# Ignore words containing digits or punctuation. Return the longest word made only of letters; if tied, return the first.
# Input: s = "AI-tools are useful, Python123 is powerful"
# Output: "powerful"
#
# 22. Rearrange by Character Type
# Place lowercase letters first, uppercase letters second, digits third, and other characters last. Preserve order within each
# category.
# Input: s = "aB3!cD1?"
# Output: "acBD31!?"

# s = "aB3!cD1?"
# a = s.split(" ")
# b = list(a[0])
# c = []
#
# for i in b:
#     if i.islower():
#         c.append(i)
# for i in b:
#     if i.isupper():
#         c.append(i)
# for i in b:
#     if i.isnumeric():
#         c.append(i)
# for i in b:
#     if i not in c:
#         c.append(i)
# d = "".join(c)
# print(d)

# 23. Words Follow a Pattern
# Check whether each word in a sentence follows the same one-to-one pattern as the pattern string.
# Input: pattern = "abba", words = "dog cat cat dog"
# Output: True
#
# 24. Common Prefix Length
# Find the length of the longest prefix of s1 that is also a prefix of s2.
# Input: s1 = "interview", s2 = "internet"
# Output: 5

# s1 = "interview"
# s2 = "internet"
# count = 0
# for i in range(len(s1)):
#     for j in range(len(s2)):
#         if i == j and s1[i] == s2[j]:
#             count += 1
# print(count)


#
# 25. Simplify a File Path
# Simplify an absolute Unix-style path by removing . and resolving .. where possible.
# Input: path = "/home/user/../docs/./file"
# Output: "/home/docs/file"

# path = "/home/user/../docs/./file"
#
# r = []
# for i in path.split("/"):
#     if i == "..":
#         if r:
#             r.pop()
#     elif i != "." and i != "":
#         r.append(i)
#
# print("/" + "/".join(r))
