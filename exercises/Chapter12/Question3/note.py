import sys

#List notes from a filename, numbered 1..
def list_notes(f):
    with open(f, 'r') as fin:
        lines = fin.readlines()
        for n, l in enumerate(lines):
            print(f'{n + 1}: {l}', end='')

#Append note to the given filename
def add_note(f, text):
    with open(f, 'a') as fout:
        print(text, file=fout)

#Remove note from a filename, given its number.
def remove_note(f, n):
    with open(f, 'r') as fin:
        lines = fin.readlines()
    with open(f, 'w') as fout:
        del lines[n - 1]
        for line in lines:
            fout.write(line)

#Main
if len(sys.argv) > 1:
    if sys.argv[1] == 'list':
        list_notes(sys.argv[2] + '.txt')
    elif sys.argv[1] == 'remove':
        remove_note(sys.argv[2] + '.txt', int(sys.argv[3]))
    elif sys.argv[1] == 'add':
        add_note(sys.argv[2] + '.txt', sys.argv[3])
    else:
        print('Unrecognized command')
