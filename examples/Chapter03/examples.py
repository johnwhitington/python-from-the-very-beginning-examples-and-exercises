for x in range(0, 5):
    print(x)

def print_upto(n):
    for x in range(1, n + 1):
        print(x)

def print_upto(n):
    for x in range(1, n + 1):
        print(x, end=' ')


def times_table(n):
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            print(x * y, end=' ')
        print('')

#Times table of size n, with tabs
def times_table(n):
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            print(x * y, end='\t')
        print('')

#Times table of size n, with smallest spaces
def times_table(n):
    column_width = len(str(n * n)) + 1
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            print(x * y, end=' ' * (column_width - len(str(x * y))))
        print('')


def print_spaced(s):
    for x in s:
        print(x, end=' ')


entered = ''

while entered != 'please':
    print('Please enter the password')
    entered = input()


#Fails
entered = ''

def ask_for_password():
    while entered != 'please':
        print('Please enter the password')
        entered = input()


def ask_for_password():
    entered = '' 
    while entered != 'please':
        print('Please enter the password')
        entered = input()


entered = ''

def ask_for_password():
    global entered
    while entered != 'please':
        print('Please enter the password')
        entered = input()
