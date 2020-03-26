emptyboard = ['', '_', '_', '_', '_', '_', '_', '_', '_', '_']

h1 = [1, 2, 3]
h2 = [4, 5, 6]
h3 = [7, 8, 9]
v1 = [1, 4, 7]
v2 = [2, 5, 8]
v3 = [3, 6, 9]
d1 = [1, 5, 9]
d2 = [3, 5, 7]

lines = [h1, h2, h3, v1, v2, v3, d1, d2]

intersecting_lines = [(h1, v1, 1), (h1, v2, 2), (h1, v3, 3),
                      (h2, v1, 4), (h2, v2, 5), (h2, v3, 6),
                      (h3, v1, 7), (h3, v2, 8), (h3, v3, 9),
                      (d1, h1, 1), (d1, h2, 5), (d1, h3, 9),
                      (d1, v1, 1), (d1, v2, 5), (d1, v3, 9),
                      (d2, h1, 3), (d2, h2, 5), (d2, h3, 7),
                      (d2, v1, 3), (d2, v2, 5), (d2, v3, 7),
                      (d1, d2, 5)]

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
                b[i] = 'X'
                return True
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

#play(True)


#The game tree for 3x3 noughts and crosses.
def swap_player(p):
    if p == 'X': return 'O'
    else: return 'X'

def next_boards(b, pl):
    if wins('O', b) or wins('X', b) or full(b):
        return (b, [])
    bs = []
    for i, e in enumerate(b):
        if e == '_':
            new_board = b.copy()
            new_board[i] = pl
            bs.append(new_board)
    return (b, [next_boards(x, swap_player(pl)) for x in bs])

def game_tree(player):
    return next_boards(emptyboard, player)

x_game_tree = game_tree('X')

#Calculate number of games in which x wins, o wins, or it is a draw
def sum_game_tree(f, t):
    b, bs = t
    ns = f(b)
    for sb in bs:
        ns = ns + sum_game_tree(f, sb)
    return ns

def f(b): return wins('X', b)
xwins = sum_game_tree(f, x_game_tree)

def f(b): return wins('O', b)
owins = sum_game_tree(f, x_game_tree)

def f(b): return not wins('X', b) and not wins('O', b) and full(b)
draw = sum_game_tree(f, x_game_tree)

print(f'O wins {owins}, X wins {xwins}, draw {draw}')

#Computer vs computer for 3x3 noughts and crosses (always a draw!)
#For this, need to allow computer to play as 'X' or 'O'
