emptyboard = ['', '_', '_', '_', '_', '_', '_', '_', '_', '_']

lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
         [1, 4, 7], [2, 5, 8], [3, 6, 9],
         [1, 5, 9], [3, 5, 7]]

def printboard(b):
    for n, x in enumerate(b):
       print(x, end='')
       if n > 0 and n % 3 == 0: print('')

def full(board):
    return '_' not in board

def wins(p, b):
    win = [p, p, p]
    for l in lines:
        bl = [b[x] for x in l]
        if bl == win: return True
    return False

def taken(n, b):
    return b[n] is not '_'

def takenby(n, p, b):
    return b[n] is not p

#Tactics.
def try_to_take(b, ps):
    for p in ps:
        if b[p] == '_':
            b[p] = 'X'
            return True
    return False

#1. Win
def win_or_block(b, piece):
    for l in lines:
        bl = [b[x] for x in l]
        if bl.count('_') == 1 and bl.count(piece) == 2:
            for x in l:
                if b[x] == '_': b[x] = 'X'
            return True
    return False

def tactic_win(b):
    return win_or_block(b, 'X')

#2. Block
def tactic_block(b):
    return win_or_block(b, 'O')

#3. Fork
def tactic_fork(b):
    return False

#4. Block fork
def tactic_block_fork(b):
    return False

#5. Play Centre
def tactic_play_centre(b):
    return try_to_take(b, [5])

#6. Play opposite corner
def tactic_play_opposite_corner(b):
    if takenby(1, 'X', b):
        if try_to_take(b, [9]): return True
    elif takenby(3, 'X', b):
        if try_to_take(b, [7]): return True
    elif takenby(7, 'X', b):
        if try_to_take(b, [3]): return True
    elif takenby(9, 'X', b):
        return try_to_take(b, 1)

#7. Play empty corner
def tactic_empty_corner(b):
    return try_to_take(b, [1, 3, 7, 9])

#8. Play empty side
def tactic_empty_side(b):
    return try_to_take(b, [2, 4, 6, 8])

def human_move(board):
    n_input = input('Position 1..9? ')
    if n_input.isdigit():
        n = int(n_input)
        if n < 1 or n > 9:
            print('Board position must be from 1..9')
            human_move(board)
        else:
            if taken(n, board):
                print('Position already taken')
                human_move(board)
            else:
                board[n] = 'O'
    else:
        print('Not a valid board position')
        human_move(board)

def computer_move(b):
    print('Computer has played:')
    if tactic_win(b):
        print('Used tactic_win')
        return
    if tactic_block(b):
        print('Used tactic_block')
        return
    if tactic_fork(b):
        print('Used tactic_fork')
        return
    if tactic_block_fork(b):
        print('Used tactic_block_fork')
        return
    if tactic_play_centre(b):
        print('Used tactic_centre')
        return
    if tactic_play_opposite_corner(b):
        print('Used tactic_play_opposite_corner')
        return
    if tactic_empty_corner(b):
        print('Used tactic_empty_corner')
        return
    if tactic_empty_side(b):
        print('Used tactic_empty_side')
        return
    print('No tactic applied: error in tactic implementations')

def play(human_goes_first):
    print('Board is numbered\n123\n456\n789\n')
    board = emptyboard.copy()
    if human_goes_first:
        print('You go first...')
        printboard(board)
    else:
        print('Computer goes first...')
    while not (full(board) or wins('X', board) or wins('O', board)):
        if human_goes_first:
            human_move(board)
        else:
            computer_move(board)
        human_goes_first = not human_goes_first
        printboard(board)
    print('Game over. Result:')
    if wins('O', board):
        print('You win!')
    elif wins('X', board):
        print('Computer wins!')
    else:
        print('Draw!')

play(False)

#The game tree for 3x3 noughts and crosses


#EXTENSIONS

#The game tree for mxn noughts and crosses

#A full computer player vs human for 3x3 noughts and crosses

#Computer vs computer for 3x3 noughts and crosses (always a draw!)

