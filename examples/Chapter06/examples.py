def print_stats(l):
    print(str(min(l)) + ' up to ' + str(max(l)))

def print_stats(l):
    minimum = min(l)
    maximum = max(l)
    print(f'{minimum} up to {maximum}')

def print_stats(l):
    print(f'{min(l)} up to {max(l)}')


def print_powers(n):
    for x in range(1, n):
        print(f'{x} {x ** 2} {x ** 3} {x ** 4} {x ** 5}')


def print_powers(n):
    for x in range(1, n):
        print(f'{x:5d} {x ** 2:5d} {x ** 3:5d} {x ** 4:5d} {x ** 5:5d}')


def print_powers(n):
    f = open('powers.txt', 'w')
    for x in range(1, n):
        print(f'{x:5d} {x ** 2:5d} {x ** 3:5d} {x ** 4:5d} {x ** 5:5d}', file=f)
    f.close()

def print_powers(n):
    with open('powers.txt', 'w') as f:
        for x in range(1, n):
            print(f'{x:5d} {x ** 2:5d} {x ** 3:5d} {x ** 4:5d} {x ** 5:5d}',
                  file=f)
