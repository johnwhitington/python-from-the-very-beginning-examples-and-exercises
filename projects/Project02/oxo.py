#Representaton of a board. A nine-tuple will do for now.

#Human representation
#123
#456
#789

#Computer representation
#012
#345
#678

emptyboard = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

def printboard(b):
  def printline(l):
      for x in l: print(x, end='')
      print('')
  printline(b[:3])
  printline(b[3:6])
  printline(b[6:])

def full(board):
    return '_' not in board

def wins(p, b):
    l = [p, p, p]
    ls = [b[:3], b[3:6], b[6:], #Horizontals
          [b[0], b[3], b[6]],   #Verticals
          [b[1], b[4], b[7]],
          [b[2], b[5], b[8]],
          [b[0], b[4], b[8]],   #Diagonals
          [b[2], b[4], b[6]]]
    #print(ls)
    return l in ls

#Human player, types 1...9 to enter their X
def human_move(board):
    n_input = input('Position? 1..9')
    if n_input.isdigit():
        n = int(n_input)
        if n < 1 or n > 9:
            print('board position must be from 1..9')
            human_move(board)
        else:
            board[n - 1] = 'X'
    else:
        print('not a valid board position')
        human_move(board)

#Computer player, just the basic rules!
def computer_move(board):
    board[board.index('_')] = 'O'

#Play!
def play(human_goes_first):
    board = emptyboard.copy()
    while not (full(board) or wins('X', board) or wins('O', board)):
        printboard(board)
        if human_goes_first:
            human_move(board)
        else:
            computer_move(board)
        human_goes_first = not human_goes_first
    #print(f"full = {full(board)}, winsx = {wins('X', board)}, winso = {wins('O', board)}")
    print('Game over. Result:')
    if wins('X', board):
        print('You win!')
    elif wins('O', board):
        print('Computer wins!')
    else:
        print('Draw!')
    printboard(board)

play(False)

#The game tree for 3x3 noughts and crosses


#EXTENSIONS

#The game tree for mxn noughts and crosses

#A full computer player vs human for 3x3 noughts and crosses

#Computer vs computer for 3x3 noughts and crosses (always a draw!)

