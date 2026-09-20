n=int(input('Enter the number: '))
i=n
rev=0
while i>0:
    rem=i%10
    rev=rev*10+rem
    i=i//10

if n==rev:
    print('The no. is pallindrome.')
else:
    print('The no. is not pallindrome.')