n=int(input('Enter the number: '))

if n%2==0:
    if n%5==0:
        print(n,'is divisibal by both 2 and 5')
    else:
        print('It is only divisibal by 2')
else:
    print('It is neither divisibal by 2 nor by 5 ')