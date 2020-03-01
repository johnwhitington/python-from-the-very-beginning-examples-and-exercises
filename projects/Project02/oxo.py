emptyboard = ['', '_', '_', '_', '_', '_', '_', '_', '_', '_']

def printboard(b):
  def printline(l):
      for x in l: print(x, end=' ')
      print('')
  printline(b[1:4])
  printline(b[4:7])
  printline(b[7:])

def full(board):
    return '_' not in board

def wins(p, b):
    l = [p, p, p]
    ls = [b[1:4], b[4:7], b[7:], #Horizontals
          [b[1], b[4], b[7]],    #Verticals
          [b[2], b[5], b[8]],
          [b[3], b[6], b[9]],
          [b[1], b[5], b[9]],    #Diagonals
          [b[3], b[5], b[7]]]
    return l in ls

def human_move(board):
    n_input = input('Position 1..9? ')
    if n_input.isdigit():
        n = int(n_input)
        if n < 1 or n > 9:
            print('board position must be from 1..9')
            human_move(board)
        else:
            board[n] = 'X'
    else:
        print('not a valid board position')
        human_move(board)

def computer_move(board):
    print('Computer has played:')
    board[board.index('_')] = 'O'

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
    if wins('X', board):
        print('You win!')
    elif wins('O', board):
        print('Computer wins!')
    else:
        print('Draw!')

play(False)

#The game tree for 3x3 noughts and crosses


#EXTENSIONS

#The game tree for mxn noughts and crosses

#A full computer player vs human for 3x3 noughts and crosses

#Computer vs computer for 3x3 noughts and crosses (always a draw!)

