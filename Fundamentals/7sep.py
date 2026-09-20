# Q.1

# a = int(input('Enter the number: '))
# if a>=0 :
#     print('the number is positive')
# else:
#     print('the number is negative')

# Q.2

# a= int(input('Enter the number: '))
# if a%2==0 :
#     print('the number is even')
# else:
#     print('the number is odd')

# Q.3

# a= int(input('Enter your age: '))
# if a>=18:
#     print('You are eligibal for voting')
# else:
#     print('You are not eligibal for voting')

# Q.4

# a = int(input('Enter your marks: '))
# if a>=40:
#     print('Pass')
# else:
#     print('Fail')

# Q.5

# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))
# if a>b:
#     print(a,' is greater')
# elif a==b:
#     print('Both no. are equal')
# else:
#     print(b,' is greater')

# Q.6

# a = int(input('Enter the number: '))
# if a>0 :
#     print('the number is positive')
# elif a==0:
#     print('the number is Zero')
# else:
#     print('the number is negative')

# Q.7

# a=int(input('Enter your marks: '))
# if a>=90:
#     print('Grade A')
# elif 74<a<90:
#     print('Grade B')
# elif 59<a<75:
#     print('Grade C')
# elif 39<a<60:
#     print('Grade D')
# else:
#     print('Fail')

# Q.8

# a=int(input('Enter number: '))
# b=int(input('Enter number: '))
# c=int(input('Enter number: '))

# if a>b and b>c :
#     print(a,' is largest')
# elif b>a and a>c:
#     print(b, 'is largest')
# else:
#     print(c, 'is largest')

# Q.9

# a=int(input('Enter the Temperature: '))
# if a>35:
#     print('Very Hot')
# elif 24<a<35:
#     print('Hot')
# elif 14<a<25:
#     print('Normal')
# else:
#     print('Cold')

# Q.10

a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=input('Enter the operator: ')

if c == '+':
    result= a+b
    print(result)
elif c == '-':
    result= a-b
    print(result)
elif c == '*':
    result= a*b
    print(result)
elif c == '/':
    result= a/b
    print(result)
elif c == '//':
    result= a//b
    print(result)
elif c == '/' and b==0:
    print('Cant divide by 0')
elif c == '//' and b==0:
    print('Cant divide by 0')
elif c == '%':
    result= a%b
    print(result)
elif c == '**':
    result= a+b
    print(result)