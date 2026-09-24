# i=99
# while i>=11:
#     print(i,end=' ')
#     i=i-1

print('Pallindrome no from 11 to 99 are:')
n=11
while n<=99:
    i=n
    rev=0
    while i>0:
        rem=i%10
        rev=rev*10+rem
        i=i//10
    if n == rev:
        print(rev,end=" ")
    n=n+1