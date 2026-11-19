# 01. Sort tuple records by score
# Sort a tuple of (student_name, score) records in ascending order of score.
# Example: (("Asha", 82), ("Ravi", 67), ("Meera", 91), ("Kabir", 75))
# t = (("Asha", 82), ("Ravi", 67), ("Meera", 91), ("Kabir", 75))
# l1 = list(t)
# for i in range(len(l1)):
#     for j in range(i + 1, len(l1)):
#         if l1[i][1] > l1[j][1]:
#             l1[i], l1[j] = l1[j], l1[i]
# print(tuple(l1))

# 02. Sort records by two fields
# Sort employee records by department alphabetically, then by salary from low to high.
# Example: (("Aman", "IT", 50000), ("Riya", "HR", 42000), ("Dev", "IT", 45000), ("Mia", "HR", 48000))
# t = (
#     ("Aman", "IT", 50000),
#     ("Riya", "HR", 42000),
#     ("Dev", "IT", 45000),
#     ("Mia", "HR", 48000),
# )
# print("Alphabetically:", sorted(t))
# l1 = list(t)
# for i in range(len(l1)):
#     for j in range(i + 1, len(l1)):
#         if l1[i][2] > l1[j][2]:
#             l1[i], l1[j] = l1[j], l1[i]
# print(tuple(l1))


# 03. Top scorer with tie handling
# Return the name of the student with the highest score. If there is a tie, return the first matching name.
# Example: (("Aarav", 88), ("Diya", 95), ("Kabir", 91), ("Mia", 95))
# t=(("Aarav", 88), ("Diya", 95), ("Kabir", 91), ("Mia", 95))


# 04. Group records by category
# Group (category, item) pairs into a dictionary where each category maps to a tuple of its items, preserving order.
# Example: (("fruit", "apple"), ("veg", "carrot"), ("fruit", "mango"), ("veg", "beans"))
# t = (("fruit", "apple"), ("veg", "carrot"), ("fruit", "mango"), ("veg", "beans"))
# r = {}
# for i, j in t:
#     if i not in r:
#         r[i] = ()
#     r[i] += (j,)
# print(r)


# 05. Transpose nested tuples
# Transpose a rectangular tuple of tuples, turning rows into columns without using external libraries.
# Example: ((1, 2, 3), (4, 5, 6)); Expected: ((1, 4), (2, 5), (3, 6))

# t = ((1, 2, 3), (4, 5, 6))
# t1 = ()
#

# 06. Flatten one level of nested tuples
# Convert a tuple containing inner tuples into one flat tuple. Assume exactly one nesting level.
# Example: ((1, 2), (3, 4, 5), (6,)); Expected: (1, 2, 3, 4, 5, 6)

t = ((1, 2), (3, 4, 5), (6,))
r = []
for i in t:
    r.extend(i)
print(tuple(r))
