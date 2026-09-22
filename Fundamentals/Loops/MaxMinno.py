# n=int(input('Enter the number: '))
# max=0 
# i=n
# while i>0:
#     dig=i%10
#     if dig>max:
#         max=dig
#     i=i//10
# print('Max number is: ',max)

n=int(input('Enter the no.: '))
min=n%10
i=n
while i>0:
    dig=i%10
    if dig<min:
        min=dig
    i=i//10
print('Minimum number is:',min)