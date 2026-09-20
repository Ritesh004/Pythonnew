#even
n=123453245
# print('Even')
# i=n
# while i>0:
#     rem=i%10
#     if rem%2==0:
#         print(rem,end=" ")
#     i=i//10

# print('Odd')
# i=n
# while i>0:
#     rem=i%10
#     if rem%2!=0:
#         print(rem,end=" ")
#     i=i//10
sum=0
count=0
i=n
while i>0:
    rem=i%10
    sum+=rem
    count+=1
    i=i//10
print('sum: ',sum)
print('Count :',count)