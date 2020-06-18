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
    tries = 0
    while guess != target:
        tries = tries + 1
        if guess < target:
            guess = int(input('Higher!\n'))
        elif guess > target:
            guess = int(input('Lower!\n'))
    print('Correct! You took ' + str(tries) + ' guesses.')


# Sentence checker
def sentence_checker():
    text = 'Jackdaws love my sphinx of Quartz'
    print(text)
    if input() == text:
        print('Correct!')
    else:
        print('Incorrect! Try again...')
        sentence_checker()

# Four digit code guesser. Reports number a) correct number in correct place
# and correct number b) correct number in incorrect place. Returns true if solved.
def check_code_guess(code, guess):
    correct = 0
    correct_place = 0
    positions_used = []
    for x in range(0, 4):
        if guess[x] == code[x]:
            correct = correct + 1
            positions_used.append(x)
        elif guess[x] in code and code.index(guess[x]) not in positions_used:
            correct_place = correct_place + 1
            positions_used.append(code.index(guess[x]))
    print('Correct number in correct place: ' + str(correct))
    print('Correct number in incorrect place: ' + str(correct_place))
    return code == guess

def code_guesser():
    random.seed()
    a = str(random.randint(1, 9)) 
    b = str(random.randint(1, 9)) 
    c = str(random.randint(1, 9)) 
    d = str(random.randint(1, 9)) 
    code = a + b + c + d
    tries = 0
    guess = input()
    while guess != code:
        if check_code_guess(code, guess): pass
        else: guess = input()
    print('Correct. You took ' + str(tries) + ' guesses.')


# Morse code generator
# Very simplistic, since we don't have lists at this point in the book
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

#n.b this prints an extra '   ' at the end of the message - to fix?

