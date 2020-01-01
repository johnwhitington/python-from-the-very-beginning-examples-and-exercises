import sys

print(f'This program is called {sys.argv[0]}')
print(f'There are {len(sys.argv) - 1} command line arguments')
for n, arg in enumerate(sys.argv[1:]):
  print(f'Argument {n} is {arg}')

