import random

emptyboard = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

h1 = [0, 1, 2]
h2 = [3, 4, 5]
h3 = [6, 7, 8]
v1 = [0, 3, 6]
v2 = [1, 4, 7]
v3 = [2, 5, 8]
d1 = [0, 4, 8]
d2 = [2, 4, 6]

lines = [h1, h2, h3, v1, v2, v3, d1, d2]

def printboard(b):
    for n, x in enumerate(b):
       print(x, end='')
       if n % 3 == 0: print('')

def full(b):
    return '_' not in b

def wins(p, b):
    win = [p, p, p]
    for l in lines:
        bl = [b[x] for x in l]
        if bl == win: return True
    return False

def play_arbitrary(pl, b):
    p = random.randint(0, 8)
    while b[p] == '_':
        p = (p + 1) % 9
    b[p] = pl

def random_game():
    b = emptyboard.copy()
    pl = 'O'
    while not (full(b) or wins('X', b) or wins('O', b)):
        printboard(b)
        play_arbitrary(pl, b)
        if pl == 'O': pl = 'X'
        else: pl = 'O'
    printboard(b)
    print('Game over. Result:')
    if wins('O', b):
        print('O wins!')
    elif wins('X', b):
        print('X wins!')
    else:
        print('Draw!')
 
