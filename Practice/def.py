# def main():
#     x=int(input('Enter your value:'))
#     print('square of your no is ', square(x))

# def square(x):
#     return x**2

# main()


def main():
    x=int(input('Enter number: '))
    if is_even(x):
        print('Even')
    else:
        print('Odd')

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

main()