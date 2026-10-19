i=1
while i<=5:
    k=1
    while k<=5-i:
        print('',end=" ")
        k+=1
    j=1
    while j<=i:
        if j==1:
            print("(",end=" ")
        if j==i:
            print(")",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1