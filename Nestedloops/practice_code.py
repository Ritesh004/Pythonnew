# i=99
# while i>=11:
#     print(i,end=' ')
#     i=i-1

# print('Pallindrome no from 11 to 99 are:')
# n=11
# while n<=99:
#     i=n
#     rev=0
#     while i>0:
#         rem=i%10
#         rev=rev*10+rem
#         i=i//10
#     if n == rev:
#         print(rev,end=" ")
#     n=n+1

# n=11
# while n<=99:
#     i=n
#     rev=0
#     while i>0:
#         rem=i%10
#         rev=rev*10+rem
#         i=i//10
#     print(rev,end=' ')
#     n=n+1


# n=100
# while n<=999:
#     i=n
#     sum=0
#     pow=3
#     while i>0:
#         dig=i%10
#         sum=sum+dig**pow
#         i=i//10
#     if n==sum:
#         print(n)
#     n=n+1


n=1
while n<=10:
    i=n
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j=j+1
    if count==2:
        print(i)
    n=n+1