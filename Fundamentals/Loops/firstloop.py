# i=1
# while i<=5:
#     print('Hello')
#     i=i+1
# print('End')

# i=5
# while i>=1:
#     print('Hello')
#     i=i-1
# print('End')

i=int(input('Enter the number: '))
a=int(input('Enter the divisor:'))
b=int(input('Enter second divisor: '))

while i>0:
    if i%a==0 and i%b==0:
        print('The number',i,'is divisibal by both ',a,'and',b)
    i=i-1