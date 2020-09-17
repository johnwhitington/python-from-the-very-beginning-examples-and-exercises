import sys

#List notes from a filename, numbered 1..
def list_notes(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for n, l in enumerate(lines):
            print(f'{n + 1}: {l}', end='')

#Append note to the given filename
def add_note(filename, text):
    with open(filename, 'a') as f:
        print(text, file=f)

#Remove note from a filename, given its number.
def remove_note(filename, n):
    with open(filename, 'r') as f_in:
        lines = f_in.readlines()
    with open(filename, 'w') as f_out:
        del lines[n - 1]
        for line in lines:
            f_out.write(line)

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
