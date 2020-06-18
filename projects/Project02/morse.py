#decode morse code using a huffman style tree

#The tree, explicitly
#Another option would be to build the tree from the letter-code pairs by
#repeated insertion into an empty tree.
tree = ('?',
           ('E',
               ('I',
                   ('S',
                       ('H', '5', '4'),
                       ('V', '?', '3')),
               ('U',
                   'F',
                       ('?', '?', '2'))),
                ('A',
                    ('R', 'L', '?'),
                    ('W', 'P',
                        ('J', '?', '1')))),
            ('T',
                ('N',
                    ('D',
                        ('B', '6', '?'), 'X'),
                    ('K', 'C', 'Y')),
                ('M',
                    ('G',
                        ('Z', '7', '?'), 'Q'),
                    ('O',
                        ('?', '8', '?'),
                        ('?', '9', '0')))))

def decode_morse(code):
    t = tree
    for c in code:
        if c == ' ': pass
        elif c == '.':
            n, l, r = t
            t = l
        else:
            n, l, r = t
            t = r
    if type(t) is tuple:
        n, l, r = t
        return n
    else:
        return t

#We split on three spaces (code boundaries) and seven spaces (words).
def split_string(string):
    codes = []
    spaces = 0
    code = ''
    for c in string:
        if c == ' ':
            if code != '' and spaces > 0:
                codes.append(code)
                code = ''
            spaces = spaces + 1
        else:
            if spaces == 7: codes.append(' ')
            spaces = 0
            code = code + c
    if code != '': codes.append(code)
    return codes

def decode_morse_string(string):
  for code in split_string(string):
      if code == ' ': print(' ', end='')
      else: print(decode_morse(code), end='')
  print('')


