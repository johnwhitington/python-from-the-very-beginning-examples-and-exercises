def first(l):
    return l[0]

def last(l):
    return l[len(l) - 1]


def reverse(l):
    l2 = []
    for x in l:
        l2.insert(0, x)
    return l2

def reverse(l):
    l2 = []
    for x in range(len(l), 0, -1):
        l2.append(x)
    return l2

def minmax(l):
    minimum = l[0]
    maximum = l[0]
    for x in l:
        if x < minimum: minimum = x
        if x > maximum: maximum = x
    print('Minimum is ' + str(minimum))
    print('Maximum is ' + str(maximum))

def evens(l):
    return l[0:len(l) + 1:2]

def evens(l):
    return l[::2]


def reverse(l):
    return l[::-1]


def setify(l):
    l2 = []
    for x in l:
        if not x in l2: l2.append(x)
    return l2

def setify(l):
    l2 = []
    for x in l:
        if x not in l2: l2.append(x)
    return l2


def histogram(l):
    unique = setify(l)
    for x in unique:
        print(str(x) + ' appears ' + str(l.count(x)) + ' times.')

def contains_all(s, a, b, c):
    return a in s and b in s and c in s


def copy(l):
    l2 = []
    for x in l: l2.append(x)
    return l2

def copy(l):
    return l[:]

def remove_copy(l, x):
    l2 = copy(l)
    l2.remove(x)
    return l2


#Caesar cipher
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVQXYZ'

def rotate(n, a):
    return a[n:] + a[:n]

def encode(text, cipher):
    out = ''
    for x in text:
        if x == ' ': out = out + ' '
        else: out = out + cipher[alphabet.index(x)]
    return out

def decode(text, cipher):
    out = ''
    for x in text:
        if x == ' ': out = out + ' '
        else: out = out + alphabet[cipher.index(x)]
    return out


#Morse code using lists
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z', '0', '1', '2', '3', '4', '5',
           '6', '7', '8', '9', '0']

codes = ['. -', '- . . .', '- . - .', '- . .',
         '.', '. . - .', '- - .', '. . . .',
         '. .', '. - - -', '- . -', '. - . .',
         '- -', '- .', '- - -', '. - - .',
         '- - . -', '. - .', '. . .', '-',
         '. . -', '. . . -', '. - -', '- . . -',
         '- . - -', '- - . .', '. - - - -', '. . - - -',
         '. . . - -', '. . . . -', '. . . . .', '- . . . .',
         '- - . . .', '- - - . .', '- - - - .', '- - - - -']

def print_morse_letter(l):
    if l not in letters: print('bad letter')
    else: print(codes[letters.index(l)], end='   ')

def print_morse(s):
    for l in s:
        if l == ' ': print('    ', end='')
        else: print_morse_letter(l)
    print('')    


# Four digit code guesser. Reports number a) correct number in correct place
# and correct number b) correct number in incorrect place. Returns true if solved.
import random

def check_code_guess(code, guess):
    code = code.copy()
    guess = guess.copy()
    correct = 0
    correct_place = 0
    for x in range(0, 4):
        if guess[x] == code[x]:
            correct = correct + 1
            code[x] = -1
            guess[x] = -1
    for x in range(0, 4):
        if guess[x] > -1:
            if guess[x] in code:
                correct_place = correct_place + 1
                code[code.index(guess[x])] = -1
    print('Correct number in correct place: ' + str(correct))
    print('Correct number in incorrect place: ' + str(correct_place))
    return code == guess

def code_guesser():
    random.seed()
    a = random.randint(1, 9) 
    b = random.randint(1, 9) 
    c = random.randint(1, 9) 
    d = random.randint(1, 9)
    code = [a, b, c, d]
    tries = 1
    i = input()
    guess = [int(i[0]), int(i[1]), int(i[2]), int(i[3])]
    while guess != code:
        if check_code_guess(code, guess): pass
        else:
            tries = tries + 1
            i = input()
            guess = [int(i[0]), int(i[1]), int(i[2]), int(i[3])]
    print('Correct. You took ' + str(tries) + ' guesses.')

