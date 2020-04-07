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

intersecting_lines = [(h1, v1, 0), (h1, v2, 1), (h1, v3, 2),
                      (h2, v1, 3), (h2, v2, 4), (h2, v3, 5),
                      (h3, v1, 6), (h3, v2, 7), (h3, v3, 8),
                      (d1, h1, 0), (d1, h2, 4), (d1, h3, 8),
                      (d1, v1, 0), (d1, v2, 4), (d1, v3, 8),
                      (d2, h1, 2), (d2, h2, 4), (d2, h3, 6),
                      (d2, v1, 2), (d2, v2, 4), (d2, v3, 6),
                      (d1, d2, 4)]

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
    for (l, l2, i) in intersecting_lines:
        bl = [b[x] for x in l]
        bl2 = [b[x] for x in l2]
        l_fits = bl.count('_') == 2 and bl.count('X') == 1
        l2_fits = bl2.count('_') == 2 and bl2.count('X') == 1
        if l_fits and l2_fits and b[i] == '_':
            b[i] = 'X'
            return True
    return False

#4. Block fork

#If position p is blank, check if filling it would make two in any row, column,
#or diagonal for 'X'. If so, fill it with 'X'.
def find_two_in_row(b, p):
    if b[p] == '_':
      #find lines p is in. If a line has one X and no Os, fill it.
      for l in lines:
          if p in l:
              bl = [b[x] for x in l]
              if bl.count('X') == 1 and bl.count('O') == 0:
                  b[p] = 'X'
                  return True
    else:
        return False

def tactic_block_fork(b):
    for (l, l2, i) in intersecting_lines:
        bl = [b[x] for x in l]
        bl2 = [b[x] for x in l2]
        l_fits = bl.count('_') == 2 and bl.count('O') == 1
        l2_fits = bl.count('_') == 2 and bl.count('O') == 1
        if l_fits and l2_fits and b[i] == '_':
            if find_two_in_row(b, l[0]): return True
            elif find_two_in_row(b, l[1]): return True
            elif find_two_in_row(b, l[2]): return True
            elif find_two_in_row(b, l2[0]): return True
            elif find_two_in_row(b, l2[1]): return True
            elif find_two_in_row(b, l2[2]): return True
            else:
                if b[i] == '_':
                    b[i] = 'X'
                    return True
    return False

#5. Play Centre
def tactic_play_centre(b):
    return try_to_take(b, [4])

#6. Play opposite corner
def tactic_play_opposite_corner(b):
    if b[0] == 'X':
        if try_to_take(b, [8]): return True
    elif b[2] == 'X':
        if try_to_take(b, [6]): return True
    elif b[6] == 'X':
        if try_to_take(b, [2]): return True
    elif b[8] == 'X':
        return try_to_take(b, 0)

#7. Play empty corner
def tactic_empty_corner(b):
    return try_to_take(b, [0, 2, 6, 8])

#8. Play empty side
def tactic_empty_side(b):
    return try_to_take(b, [1, 3, 5, 7])

def human_move(board):
    n_input = input('Position 0..8? ')
    if n_input.isdigit():
        n = int(n_input)
        if n < 0 or n > 8:
            print('Board position must be from 0..8')
            human_move(board)
        else:
            if board[n] is not '_':
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
    print('Board is numbered\n012\n345\n678\n')
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

play(True)



