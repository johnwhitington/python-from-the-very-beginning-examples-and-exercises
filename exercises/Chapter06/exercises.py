#1
def print_list(l):
    length = len(l)
    print('[', end='')
    for x in l:
        print(x, end='')
        length = length - 1
        if length > 0: print(', ', end='')
    print(']')

#2
def print_list(l):
    length = len(l)
    print('[', end='')
    for x in l:
        length = length - 1
        if length > 0:
            print(f'{x}, ', end='')
        else:
            print(f'{x}', end='')
    print(']')

#3
def print_powers():
    for x in range(1, 10):
        x1 = str(x).rjust(5)
        x2 = str(x ** 2).rjust(5)
        x3 = str(x ** 3).rjust(5)
        x4 = str(x ** 4).rjust(5)
        x5 = str(x ** 5).rjust(5)
        print(x1, x2, x3, x4, x5)

#4
def names_to_file():
    with open('names.txt', 'w') as f:
        name = 'not empty'
        while name != '':
            name = input('Title, forename and surname, please: ')
            if name != '':
                words = name.split()
                print(words[2], words[1], words[0], sep=', ', file=f)

#5
def names_to_file():
    with open('names.txt', 'w') as f:
        name = 'not empty'
        while name != '':
            name = input('Title, forename and surname, please: ')
            if name != '':
                words = name.split()
                print(f'{words[2]}, {words[1]}, {words[0]}', sep=', ', file=f)

