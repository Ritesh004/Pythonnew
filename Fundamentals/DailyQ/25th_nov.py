# Q.1.  From the list, select numbers that are divisible by 3 but not divisible by 5
# print("Q.1.")
# l = [9, 10, 12, 15, 18, 20, 21, 25, 27]
# abc = lambda a, b: list(i for i in l if i % a == 0 and i % b != 0)
# print(abc(3, 5))


# Q.2.  For each number, return its square if it is even; otherwise return its cube.
# print("Q.2.")
#
# abc = lambda l: list(i**2 if i % 2 == 0 else i**3 for i in l)
# print(abc([2, 3, 4, 5, 6]))


# Q.3. Select numbers whose first and last digits are the same
# print("Q.3.")

# abc = lambda l: list(i for i in l if str(i)[0] == str(i)[-1])
# print(abc([121, 234, 4554, 789, 909]))


# Q.4.  From the list of words, select palindromes (words that read the same forward and backward).
# print("Q.4.")
#
# abc = lambda l: list(i for i in l if i == i[::-1])
# print(abc(["level", "python", "madam", "world", "radar", "java"]))
#

# Q.5.  For each word, create a tuple containing the word and its length.
# print("Q.5.")
#
# abc = lambda l: list((i, len(i)) for i in l)
# print(abc(["apple", "python", "sql"]))


# Q.6.  Select numbers whose digit sum is greater than 10.
# print("Q.6.")
#
# abc = lambda l: [i for i in l if sum(int(d) for d in str(i)) > 10]
# print(abc([123, 245, 506, 111, 89]))


# Q.7.  For each number, return the number with its digits reversed.
# print("Q.7.")
#
# abc = lambda l: [int(str(i)[::-1]) for i in l]
# print(abc([123, 405, 780, 91]))


# Q.8.  Select names that contain at least two occurrences of the letter 'a' (case-insensitive).
# print("Q.8.")
#
# names = ["Akshay", "Rahul", "Ananya", "Priya", "Aarav"]
#
# result = list(filter(lambda n: n.count("a") >= 2, names))
# print(result)

# Q.9.  From a list of integers, keep only numbers that are greater than the previous number. Compare each item with its immediate predecessor; ignore the first item
# print("Q.9.")
#
# abc = lambda l: [l[i] for i in range(1, len(l)) if l[i] > l[i - 1]]
# print(abc([10, 15, 12, 20, 18, 25]))
#

# Q.10.  For each number, replace it with 'Even' or 'Odd' followed by the number.
# print("Q.10.")
#
# abc = lambda l: ["Even-" + str(i) if i % 2 == 0 else "Odd-" + str(i) for i in l]
# print(abc([12, 7, 20, 9]))


# Q.11. Select words that start and end with the same character, ignoring letter case.
# print("Q.11.")
#
# abc = lambda l: [i for i in l if i.lower()[0] == i.lower()[-1]]
# print(abc(["Level", "Python", "Radar", "Apple", "Area"]))


# Q.12. From the list of tuples (name, marks), select students who scored at least 75 and return only their names.
# print("Q.12.")
#
# abc = lambda l: [i[0] for i in l if i[1] >= 75]
# print(abc([("Amit", 72), ("Riya", 88), ("Karan", 75), ("Neha", 64)]))


# Q.13.  For each number, calculate the product of its non-zero digits.
# print("Q.13.")
#
# abc = lambda l: [__import__("math").prod(int(j) for j in str(i) if j != "0") for i in l]
# print(abc([123, 405, 26, 7003]))


# Q.14. Select strings that contain only alphabetic characters. Do not use regular expressions.
print("Q.14.")

abc = lambda l: [i for i in l if i.isalpha()]
print(abc(["Python", "Hello123", "DataScience", "SQL!", "Lambda"]))


# Q.15. From a list of numbers, select values that occur exactly once in the original list. Preserve their original order.
print("Q.15.")

abc = lambda l: [i for i in l if l.count(i) == 1]
print(abc([4, 7, 4, 9, 2, 7, 5, 9, 11]))
