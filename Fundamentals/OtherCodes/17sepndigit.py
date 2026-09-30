# Q.1 Take a two-digit number and print its tens digit and units digit separately.

# n=int(input('Enter two digit no.: '))
# i=n
# while i>0:
#     rem=i%10
#     print(rem)
#     i=i//10

# Q.2 Take a two-digit number and find the sum of its digits.

# n=int(input('Enter two digit no.: '))
# i=n
# a=0
# while i>0:
#     rem=i%10
#     print(rem)
#     a+=rem
#     i=i//10
# print('Sum= ',a)

# Q.3 Take a two-digit number and find the product of its digits.

# n=int(input('Enter two digit no.: '))
# i=n
# a=1
# while i>0:
#     rem=i%10
#     print(rem)
#     a*=rem
#     i=i//10
# print('Product of two digit no is: ',a)

# Q.4 Take a two-digit number and find the difference between its digits.

# n=int(input('Enter two digit no.: '))
# i=n
# a=i%10
# while i>0:
#     rem=i%10
#     print(rem)
#     i=i//10
# a=rem-a
# print('Difference between two digit no is: ',a)

# Q.5 Take a two-digit number and print the number obtained by reversing its digits.

# n=int(input('Enter two digit no.: '))
# i=n
# while i>0:
#     rem=i%10
#     print(rem,end='')
#     i=i//10

# Q.6 Take a two-digit number and check whether both digits are equal.


# n=int(input('\n Enter two digit no.: '))
# i=n%10
# a=n//10
# if a==i:
#     print('Both digits in no are equal')
# else:
#     print('Both digits in no are not equal')

# Q.7 Take a two-digit number and check whether the first digit is greater than the second digit.

# n=int(input('\n Enter two digit no.: '))
# i=n%10
# a=n//10
# if a>n:
#     print('First digit is greater')
# else:
#     print('Second digit is greater')

# Q.8 Take a two-digit number and check whether the sum of its digits is even or odd.

# n=int(input('Enter two digit no.: '))
# i=n
# a=0
# while i>0:
#     rem=i%10
#     print(rem)
#     a+=rem
#     i=i//10
# print('Sum= ',a)
# if a%2==0:
#     print('Sum of its digits is even')
# else:
#     print('Sum of its digits is odd')

# Q.9 Take a two-digit number and check whether the product of its digits is divisible by 3.

# n=int(input('Enter two digit no.: '))
# i=n
# a=1
# while i>0:
#     rem=i%10
#     print(rem)
#     a*=rem
#     i=i//10
# print('Product of two digit no is: ',a)
# if a%3==0:
#     print('Product of two digit no is divisibal by 3')
# else:
#     print('Product of two digit no is not divisibal by 3')

# Q.10 Take a two-digit number and calculate the square of each digit.

# n=int(input('Enter two digit no.: '))
# i=n
# while i>0:
#     rem=i%10
#     print('Square of digit',rem,' is: ',rem**2)
#     i=i//10

# Q.11 Take a two-digit number and calculate the cube of each digit.

# n=int(input('Enter two digit no.: '))
# i=n
# while i>0:
#     rem=i%10
#     print('Cube of digit',rem,' is: ',rem**3)
#     i=i//10

# Q.12 Take a two-digit number and find the sum of the squares of its digits.

# n=int(input('Enter two digit no.: '))
# i=n
# a=0
# b=0
# while i>0:
#     rem=i%10
#     a=rem**2
#     print('Square of digit',rem,' is:',a)
#     b+=a
#     i=i//10
# print('Sum of square of two digit is:',b)

# Q.13 Take a two-digit number and find the sum of the cubes of its digits.

# n=int(input('Enter two digit no.: '))
# i=n
# a=0
# b=0
# while i>0:
#     rem=i%10
#     a=rem**3
#     print('Square of digit',rem,' is:',a)
#     b+=a
#     i=i//10
# print('Sum of square of two digit is:',b)

# Q.14 Take a two-digit number and multiply its first digit by 5 and second digit by 10.

# n = int(input("Enter two digit no: "))
# i = n // 10
# print("First digit multiply by 5 is :", i * 5)
# a = n % 10
# print("Second digit multiply by 10 is :", a * 10)

# Q.15 Take a two-digit number and add 10 to the first digit and 20 to the second digit.

# n = int(input("Enter two digit no: "))
# i = n // 10
# print("First digit after adding 10 is :", i + 10)
# a = n % 10
# print("Second digit after adding 20 is :", a + 20)

# Q.16 Take a three-digit number and print its hundreds, tens, and units digits separately.


# Q.17 Take a three-digit number and find the sum of its digits.

n = int(input("Enter three digit number: "))
i = n
sum = 0
while i > 0:
    dig = i % 10
    sum += dig
    i = i // 10
print("The sum of three-digit numbers digit is: ", sum)

# Take a three-digit number and find the product of its digits.
# Take a three-digit number and find the difference between its first and last digit.D
# Take a three-digit number and reverse its digits.
# Take a three-digit number and find the sum of the squares of its digits.
# Take a three-digit number and find the sum of the cubes of its digits.
# Take a three-digit number and check whether its first digit is greater than its last digit.
# Take a three-digit number and check whether the sum of its digits is even or odd.
# Take a three-digit number and print only its middle digit.
# Take a three-digit number and print only its first and last digits.
# Take a three-digit number and interchange its first and last digits.
# Take a three-digit number and multiply its hundreds digit by its units digit.
# Take a three-digit number and calculate (first digit + second digit) * third digit.
# Take a three-digit number and calculate first digit * second digit + third digit.
