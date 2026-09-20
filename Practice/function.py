def main():
    numbers=get_number()
    Hello(numbers)

def get_number():
    while True:
        n=int(input('Enter the number: '))
        if n>0:
            return n
        
def Hello(n):
    for i in range(n):
        print('Hello ',end='')

main()    