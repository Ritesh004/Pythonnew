n=int(input('Enter the number: '))
sum =0
pow=len(str(n))
i=n
while i>0:
    dig=i%10
    sum+=dig**pow
    i=i//10
print(sum)
if n==sum:
    print(n,'is armstrong number')
else:
    print(n,'is not armstrong number')