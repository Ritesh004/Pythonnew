n=100
while n<=999:
    i=n
    sum=0
    pow=3
    while i>0:
        dig=i%10
        sum=sum+dig**pow
        i=i//10
    if n==sum:
        print(n)
    n=n+1