print('Prime no from 1 to 10 are: ')
i=1
while i<=10:
    n=i
    count=0
    j=1
    while j<=n:
        if n%j==0:
            count+=1
        j=j+1
    if count==2:
        print(n,end=" ")

    i=i+1