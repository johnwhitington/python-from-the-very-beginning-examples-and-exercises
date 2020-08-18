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
       if n % 3 == 2: print('')

def full(b):
    return '_' not in b

def wins(p, b):
    win = [p, p, p]
    for l in lines:
        bl = [b[x] for x in l]
        if bl == win: return True
    return False

def human_move(pl, board):
    n_input = input('Position 0..8? ')
    if n_input.isdigit():
        n = int(n_input)
        if n < 0 or n > 8:
            print('Board position must be from 0..8')
            human_move(pl, board)
        else:
            if board[n] != '_':
                print('Position already taken')
                human_move(pl, board)
            else:
                board[n] = pl
    else:
        print('Not a valid board position')
        human_move(pl, board)

def play():
    pl = 'X'
    print('Board is numbered\n123\n456\n789\n.')
    board = emptyboard.copy()
    while not (full(board) or wins('X', board) or wins('O', board)):
        print(f'Player {pl} to play...')
        human_move(pl, board)
        if pl == 'X':
            pl = 'O'
        else:
            pl = 'X'
        printboard(board)
    print('Game over. Result:')
    if wins('O', board):
        print('You win!')
    elif wins('X', board):
        print('Computer wins!')
    else:
        print('Draw!')

play()
