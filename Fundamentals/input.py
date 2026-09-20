# name=input('Enter your name:')
# age=int(input("Enter your age:"))

# print('Name: ',name, '\n Age: ',age)

# Q.1
print('Adition')
a=int(input('Enter first no:'))
b=int(input('Enter second no:'))

result=a+b
print("Addition of two nums :",result)

#Q.2
print('Substraction')
a=int(input('Enter first no:'))
b=int(input('Enter second no:'))

sub=a-b
print("Subtraction of two nums :",sub)

#Q.3
print('Multiplication')
a=int(input('Enter first no:'))
b=int(input('Enter second no:'))

mul=a*b
print("Multiplication of two nums :",mul)

#Q.4
print('Division')
a=int(input('Enter first no:'))
b=int(input('Enter second no:'))

div=a/b
print("Division of two nums :",div)

#Q.5
print('Modulus')
a=int(input('Enter first no:'))
b=int(input('Enter second no:'))    

mod=a%b
print("Modulus of two nums :",mod)

#Q.6
print('Floor Division')
a=int(input('Enter first no:'))
b=int(input('Enter second no:'))   

fdiv=a//b
print("Floor Division of two nums :",fdiv)

#Q.7
print('Square')
a=int(input('Enter first no:'))


sqr= a**2
print("square of 10 :",sqr)

#Q.8
print('Cube')
a=int(input('Enter first no:'))


cube=a**3
print("cube of 10 :",cube)

#Q.9
print('Exponent')
a=int(input('Enter first no:'))
b=int(input('Enter second no:'))   

exp=a**b
print("Exponent of two nums :",exp)

#Q.10

from cmath import pi


l=(float(input("Enter Length of Rectangle: ")))
b=(float(input("Enter Breadth of Rectangle: ")))

print("Area of Rectangle = ",l*b)

#Q.11

l=(float(input("Enter Length of Rectangle: ")))
b=(float(input("Enter Breadth of Rectangle: ")))

print("Perimeter of Rectangle = ",2*(l+b))

#Q.12
 
r=(float(input("Enter Radius of Circle: ")))
print("Area of Circle = ",pi*r**2)

#Q.13

p=(float(input('Enter principal value: ')))
r=(float(input('Enter interest rate : ')))
t=(float(input('Enter time in years: ')))

print('Simple Interest of your given values is : ',(p*r*t)/100)

#Q.14

a=(int(input("Enter marks of first subject: ")))
b=(int(input("Enter marks of first subject: ")))
c=(int(input("Enter marks of first subject: ")))
d=(int(input("Enter marks of first subject: ")))
e=(int(input("Enter marks of first subject: ")))

print("Total marks are : ", a+b+c+d+e)

#Q.15

a =list(map(int,input("Enter your numbers:").split()))

print(sum(a))

#Q.16

a=int(input('Enter no of days:'))

hour = a*24
print("After converting days in to hours the result is : ", hour)

#Q.17

a=int(input('Enter no of hours:'))
min = a*60
print("After converting hours in to minutes the result is : ", min)

#Q.18

a=(int(input("Enter price of first item : ")))
b=(int(input("Enter price of second item: ")))
c=(int(input("Enter price of third item: ")))
d=(int(input("Enter price of fourth item: ")))
e=(int(input("Enter price of fifth item: ")))

print("Total marks are : ", a+b+c+d+e)

#Q.19

s=int(input('Enter first no:'))
b=int(input('Enter second no:'))

print("Salary without bonus :", s)
print("Salary with bonus :", s+b)
