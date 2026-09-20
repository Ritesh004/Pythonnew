# # #Q.21
# # print("\n Q.21")

# # n = (int(input("Enter your two digit number :")))

# # sum = n//10
# # rem = n%10
# # sum+=rem
# # print("Sum of two digit numbers is : ", sum)

# # #Q.22
# # print("\n Q.22")

# # n = (int(input("Enter your number")))
# # print("Last digit of your number is :", n%10)

# # #Q.23
# # print("\n Q.23")

# # h = (float(input("Enter the number of hours you want to convert into second")))
# # print("Total number of seconds after conversion is :", h*60*60)

# # #Q.24
# # print("\n Q.24")

# # a = (int(input("Enter total numbers of children:")))
# # b = (int(input("Enter total number of chocolates:")))
# # print("Each child will get", b//a, "chocolates")

# # #Q.25
# # print("\n Q.25")

# # a = (int(input("Enter total numbers of children:")))
# # b = (int(input("Enter total number of chocolates:")))
# # print("No. of remaining chocolates after equal distribution is: ", b%a)

# # #Q.26
# # print("\n Q.26")

# # a =list(map(float, input("Enter your markes one by one: ").split()))

# # print("total percentage obtained by student:", f"{((sum(a)/(len(a)*100)*100)):.2f}%")

# # #Q.27
# # print("\n Q.27")

# # from cmath import pi

# # r= (int(input("Enter the radius of circle: ")))

# # print("Area of circle: ",pi*r**2)
# # print("Circumferance of circle: ",2*pi*r)

# # #Q.28
# # print("\n Q.28")

# # a= (int(input('Enter the units of electricity consumed by you: ')))
# # b= 8.5 # electricity rate per unit

# # print("Your bill is : ", a*b)

# # #Q.29
# # print("\n Q.29")

# # a=(int(input("Enter you bill amount: ")))
# # b=(18/a)*100
# # c= a+b

# # print("Your total amount with 18% GST is: ",c)

# # #Q.30
# # print("\n Q.30")

# # a=(float(input("Enter you bill amount: ")))
# # b=(10/a)*100
# # c= b-a

# # print("Your total amount after 10% discount is: ",c)

# # #Q.31
# # print("\n Q.31")

# # a=10
# # b=20
# # a,b = b,a
# # print ("After swapping \n ",a ,"\n", b)

# # #Q.32
# # print("\n Q.32")

# # a=(int(input("Enter your number for addition of first and last digit of it : ")))
# # b=len(str(a))-1
# # c=10**b
# # d=a//c
# # e=a%10

# # print('sum of first and last digits of your numbers is : ', d+e)

# # #Q.33
# # print("\n Q.33")

# # list=[5000, 2000, 10000, 3500]
# # x=sum(list)
# # a= 2500 # shipping charges 

# # b= (18/x)*100  # taxes

# # print("Total cost of items including tax and shipping is : ",x+a+b)

# #Q.34
# print("\n Q.34")
# from cmath import pi
# r=15
# v=(4/3)*pi*r**3

# print("Volume of sphere is: ", v)

# #Q.35
# print("\n Q.35")

# p= 10000 #principal amount 
# r = 5 # interest rate

# a = (p*(1+(r/100))**2)-p  # error
# # b= 1-(r/100)
# # c=b**2
# # d=p

# print("Compound interest for two years for this amount is : ",a)

# #Q.36
# print("\n Q.36")

# d= 145 #distance
# t= 1.5

# s= d/t
# print("Average speed is : ", s)

# #Q.37
# print("\n Q.37")

# a= 10 # no of products 
# b = 2545   # amount

# print("Amount is : ", a*b)

# #Q.38
# print("\n Q.38")

# a= 56 # age

# b= 12 # months
# print("Age in months will be : ",a*b)

# #Q.39
# print("\n Q.39")

# a= 10 # kilometers
# b= 1000
# print("KM in M will be: ",a*b)

# #Q.40
# print("\n Q.40")

# a= 50
# b=1000

# print("Meters into centimeters is :", a*b)

# p= 10000 #principal amount 
# r = 5 # interest rate

# a = (p*(1+(r/100))**2)-p  # error
# # b= 1-(r/100)
# # c=b**2
# # d=p

# print("Compound interest for two years for this amount is : ",a)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(len(arr))