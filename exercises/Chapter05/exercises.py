#Q1
def strip_leading_spaces(l):
    while len(l) > 0 and l[0] == ' ':
        del l[0]

def remove_spaces(s):
    l = list(s)
    strip_leading_spaces(l)
    l.reverse()
    strip_leading_spaces(l)
    l.reverse()
    return ''.join(l)

#Q2
def remove_spaces(s):
    return ' '.join(s.split())

#Q3
def sorted_words(s):
    l = s.split()
    l.sort()
    return l

#Q4
def sorted_words(s):
    return sorted(s.split())

#Q5
def setify(l):
    l2 = []
    for x in l:
        if x not in l2: l2.append(x)
    return l2

#Original from chapter 4
def histogram(l):
    unique = setify(l)
    for x in unique:
        print(str(x) + ' appears ' + str(l.count(x)) + ' times.')

#With sorting
def histogram(l):
    unique = sorted(setify(l))
    for x in unique:
        print(str(x) + ' appears ' + str(l.count(x)) + ' times.')

#Q6
def clip(x):
    if x > 10:
        return 10
    elif x < 1:
        return 1
    else:
        return x

def clip_list(l):
    return list(map(clip, l))

#Q7
def is_palindromic(s):
    return s == s[::-1]

def palindromes(l):
    return list(filter(is_palindromic, l))

def palindromic_numbers_in(x, y):
    return list(map(int, palindromes(list(map(str, list(range(x, y)))))))

#Q8
def clip_list(l):
    return [clip(x) for x in l]

#Q9
def palindromic_numbers_in(x, y):
    strings = list(map(str, list(range(x, y))))
    return [int(x) for x in strings if is_palindromic(x)]

#Worth mentioning here, that not all the list()s are required... which ones?

