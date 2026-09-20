name = input('Enter your name: ')

match name:
    case "abc" | "cde" | "efg":
        print('Hello')
    case "xyz":
        print('Hi')
    case _:
        print('Who are you')