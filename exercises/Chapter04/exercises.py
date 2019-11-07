def first(l):
    return l[0]

def last(l):
    return l[len(l) - 1]


def reverse(l):
    l2 = []
    for x in l:
        l2.insert(0, x)
    return l2

def reverse(l):
    l2 = []
    for x in range(len(l), 0, -1):
        l2.append(x)
    return l2


def evens(l):
    return l[0:len(l) + 1:2]

def evens(l):
    return l[::2]


def reverse(l):
    return l[::-1]


def minmax(l):
    minimum = l[0]
    maximum = l[0]
    for x in l:
        if x < minimum: minimum = x
        if x > maximum: maximum = x
    print('minimum is ' + str(minimum) + ', maximum is ' + str(maximum) + '.')


def setify(l):
    l2 = []
    for x in l:
        if x not in l2: l2.append(x)
    return l2

def histogram(l):
    unique = setify(l)
    for x in unique:
        print(str(x) + ' appears ' + str(l.count(x)) + ' times.')

def contains_all(s, a, b, c):
    return a in s and b in s and c in s


def copy(l):
    l2 = []
    for x in l: l2.append(x)
    return l2

def copy(l):
    return l[:]

def remove_copy(l, x):
    l2 = copy(l)
    l2.remove(x)
    return l2


