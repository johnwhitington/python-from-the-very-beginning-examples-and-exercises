def print_down_from(n):
    for x in range(n, 0, -1):
      print(x)


def times_table(n):
    column_width = len(str(n * (n - 1))) + 1
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            print(x * y, end=' ' * (column_width - len(str(x * y))))
        print()


def count_spaces(s):
    c = 0
    for x in s:
        if x == ' ':
            c = c + 1
    return c

def count_spaces(s):
    c = 0
    for x in s:
        if x == ' ':
            c += 1
    return c


def print_spaced(s):
    l = len(s)
    for x in s:
        print(x, end='')
        l = l - 1
        if l > 0: print(' ', end='')
    print('')


def sentence_checker():
    text = 'Jackdaws love my sphinx of Quartz'
    print(text)
    while input() != text:
        print('Incorrect! Try again...')
    print('Correct!')


def ask_for_password():
  entered = ''  
  while entered != 'please':
    entered = input('Please enter the password\n')

def ask_for_password():
    while input('Please enter the password\n') != 'please':
        pass


import random

def guessing_game():
    target = random.randint(1, 100)
    guess = int(input('Guess a number between 1 and 100\n'))
    tries = 1
    while guess != target:
        tries = tries + 1
        if guess < target:
            guess = int(input('Higher!\n'))
        elif guess > target:
            guess = int(input('Lower!\n'))
    print('Correct! You took ' + str(tries) + ' guesses.')


def print_morse_letter(l):
    if l == 'A': print('. -', end='   ')
    elif l == 'B': print('- . . .', end='   ')
    elif l == 'C': print('- . - .', end='   ')
    elif l == 'D': print('- . .', end='   ')
    elif l == 'E': print('.', end='   ')
    elif l == 'F': print('. . - .', end='   ')
    elif l == 'G': print('- - .', end='   ')
    elif l == 'H': print('. . . .', end='   ')
    elif l == 'I': print('. .', end='   ')
    elif l == 'J': print('. - - -', end='   ')
    elif l == 'K': print('- . -', end='   ')
    elif l == 'L': print('. - . .', end='   ')
    elif l == 'M': print('- -', end='   ')
    elif l == 'N': print('- .', end='   ')
    elif l == 'O': print('- - -', end='   ')
    elif l == 'P': print('. - - .', end='   ')
    elif l == 'Q': print('- -. -', end='   ')
    elif l == 'R': print('- . -', end='   ')
    elif l == 'S': print('. . .', end='   ')
    elif l == 'T': print('-', end='   ')
    elif l == 'U': print('. . -', end='   ')
    elif l == 'V': print('. . . -', end='   ')
    elif l == 'W': print('. - -', end='   ')
    elif l == 'X': print('- . . -', end='   ')
    elif l == 'Y': print('- . - -', end='   ')
    elif l == 'Z': print('- - . .', end='   ')
    elif l == '1': print('. - - - -', end='   ')
    elif l == '2': print('. . - - -', end='   ')
    elif l == '3': print('. . . - -', end='   ')
    elif l == '4': print('. . . . -', end='   ')
    elif l == '5': print('. . . . .', end='   ')
    elif l == '6': print('- . . . .', end='   ')
    elif l == '7': print('- - . . .', end='   ')
    elif l == '8': print('- - - . .', end='   ')
    elif l == '9': print('- - - - .', end='   ')
    elif l == '0': print('- - - - -', end='   ')
    else: print('bad letter')

def print_morse(s):
    for l in s:
        if l == ' ': print('    ', end='')
        else: print_morse_letter(l)
    print('')

