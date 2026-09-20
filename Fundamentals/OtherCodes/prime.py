# n=int(input('Enter the number: '))
# count=0
# i=1
# while i<=n:
#     if n%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print('The number',n,'is prime')
# else:
#     print('The number',n,'is not prime')


n=int(input('Enter the number: '))
flag=True
i=2
while i<n:  # i<=n/2:   we can do this also
    if n%i==0:
        flag=False
    i=i+1

if flag==True:
    print('The number',n,' is prime')
else:
    print('The number',n,' is not prime')