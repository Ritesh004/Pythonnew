x=65
i=1
n=1
while i<=5:
    k=1
    while k<=6-i:
        print("",end=" ")
        k+=1
    j=1
    while j<=i:
        if j==i:
            print(chr(x),end=" ")
        else:
            print(" ",end=" ")
        if j==i:
            print(n,end=" ")
        else:
            print(" ",end=" ")
        n+=1
        x+=1
        j+=1
    print()
    i+=1
