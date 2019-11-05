def print_numbers_reversed(n):
    for x in range(n, 0, -1):
      print(x)

def times_table(n):
    column_width = len(str(n * (n - 1))) + 1
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            print(x * y, end=' ' * (column_width - len(str(x * y))))
        print('')

def count_spaces(s):
    c = 0
    for x in s:
        if x == ' ':
            c = c + 1
    return c

def print_spaced(s):
    l = len(s)
    for x in s:
        print(x, end='')
        l = l - 1
        if l > 0: print(' ', end='')
    print('')

#Uses enumerate, probably leave out.
def print_spaced(s):
    l = len(s)
    for i, x in enumerate(s):
        print(x, end='')
        if i < l - 1: print(' ', end='')
    print('')

#Use prompt in input, add \n to keep the same
def ask_for_password():
  entered = ''  
  while entered != 'please':
    entered = input('Please enter the password\n')

#remove the variable
def ask_for_password():
    while input('Please enter the password\n') != 'please':
        pass

#Q6: guessing_game
import random

def guessing_game():
    target = random.randint(1, 100)
    guess = int(input('Guess a number between 1 and 100\n'))
    tries = 0
    while guess != target:
        tries = tries + 1
        if guess < target:
            guess = int(input('Higher!\n'))
        elif guess > target:
            guess = int(input('Lower!\n'))
    print('Correct! You took ' + str(tries) + ' guesses.')

