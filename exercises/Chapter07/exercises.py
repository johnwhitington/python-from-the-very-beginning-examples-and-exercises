#1

# >>> a = 1
# >>> b = 2
# >>> a, b = b, a
# >>> a
# 2
# >>> b
# 1

#Note that we cannot write this:

def swap(a, b): a, b = b, a

#2

def sum_all(t):
  if type(t) is int:
    return t
  else:
    total = 0
    for x in t:
      total = total + sum_all(x)
    return total


#3
def keys_and_values(d):
    ks = []
    vs = []
    for k, v in d.items():
      ks.append(k)
      vs.append(v)
    return (ks, vs)

#4
def dict_of_keys_and_values(ks, vs):
    d = {}
    for x in range(0, len(ks)):
        d[ks[x]] = vs[x]
    return d

#5
def union(a, b):
    u = {}
    for x in b: u[x] = b[x]
    for x in a: u[x] = a[x]
    return u


#6
def remove_zeroes(l):
    while 0 in l:
        l.remove(0)

#7
def reverse_dict(d):
    return {v:k for k, v in d.items()}

#8
def letter_set(l):
    letters = set()
    for x in l:
        letters = letters | set(x)
    return letters

letters = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')

def letters_not_used(l):
    return letters - letter_set(l)

#9
def dset_of_list(l):
    set = {}
    for x in l:
        set[x] = 0
    return set

def dset_or(a, b):
    result = {}
    for x in a: result[x] = 0
    for x in b: result[x] = 0
    return result

def dset_and(a, b):
    result = {}
    for x in a:
        if x in b:
            result[x] = 0
    return result

def dset_minus(a, b):
    result = {}
    for x in a:
      if x not in b:
          result[x] = 0
    return result

def dset_exclusive_or(a, b):
    return dset_or(dset_minus(a, b), dset_minus(b, a))


#10
def comp_and(a, b):
    return {x for x in a for y in b if x == y}
