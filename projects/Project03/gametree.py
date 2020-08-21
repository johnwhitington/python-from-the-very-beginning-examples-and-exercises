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

def full(b):
    return '_' not in b

def wins(p, b):
    win = [p, p, p]
    for l in lines:
        bl = [b[x] for x in l]
        if bl == win: return True
    return False

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

def game_tree(pl):
    return next_boards(emptyboard, pl)

x_game_tree = game_tree('X')

#Calculate number of games in which x wins, o wins, or it is a draw
def sum_game_tree(f, t):
    b, bs = t
    ns = f(b)
    for sb in bs:
        ns += sum_game_tree(f, sb)
    return ns

def f(b): return wins('X', b)
xwins = sum_game_tree(f, x_game_tree)

def f(b): return wins('O', b)
owins = sum_game_tree(f, x_game_tree)

def f(b): return not wins('X', b) and not wins('O', b) and full(b)
draw = sum_game_tree(f, x_game_tree)

def f(b): return wins('X', b) or wins('O', b) or full(b)
total = sum_game_tree(f, x_game_tree)

print(f'O wins {owins}, X wins {xwins}, draw {draw}, total games {total}')


