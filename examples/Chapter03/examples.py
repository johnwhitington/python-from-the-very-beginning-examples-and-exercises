#Times table of size n, with spaces
def times_table(n):
  for y in range(1, n + 1):
    for x in range(1, n + 1):
      print(x * y, end=' ')
    print('')

#Times table of size n, with tabs
def times_table(n):
  for y in range(1, n + 1):
    for x in range(1, n + 1):
      print(x * y, end='\t')
    print('')

#Times table of size n, with smallest even spaces
def times_table(n):
  column_width = len(str(n * n)) + 1
  for y in range(1, n + 1):
    for x in range(1, n + 1):
      print(x * y, end=' ' * (column_width - len(str(x * y))))
    print('')

