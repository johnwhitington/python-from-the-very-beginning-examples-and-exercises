def f(a, b): a + b

def g(a):
    if a > 0:
        return a
    else:
        pass

list(map(g, [-1, 0, 1, 2, 3]))

d = {1: 'one', 2: 'two', 3: 'three'}

def found_values(l, d):
    output = []
    for k in l:
        v = d.get(k)
        if v is not None:
            output.append(v)
    return output

found_values([1, 2, 3], {1 : 'one', 2 : 'two'})

d = {1 : 'one', 2 : 'two', 3 : 'three'}


def f(x, y): return x + y + z


def safe_lookup(d, k):
    try:
        return d[k]
    except KeyError as e:
        print(f'Could not find value for key {k}')
        return -1

safe_lookup({1 : 'one', 2 : 'two', 3 : 'three'}, 0)

def add3(x, y): return x + y + z

add3(1, 2)
z = 10
add3(1, 2)


def repeated(e, length):
    if length < 0: raise ValueError
    l = []
    for x in range(0, length): l.append(e)
    return l

repeated(1, 10)
repeated(1, -10)

def safe_lookup(d, k):
    try:
        return d[k]
    except KeyError as e:
        print(f'FATAL ERROR: Bad key {k} in dict {d}')
        raise e

def safe_lookup(d, k):
    try:
        return d[k]
    except Exception as e:
        print('Unknown error in safe_lookup')
        raise e

def safe_lookup(d, k):
    try:
        print('attempting key lookup')
        result = d[k]
    except Exception as e:
        print('Unknown error in safe_lookup')
        raise e
    else:
        print('key lookup succeeded')
        return result

import random

def get_guess(message):
    try:
        this_guess = int(input(message))
    except ValueError:
        print('Not a number!')
        return get_guess('')
    else:
        if this_guess < 1 or this_guess > 100:
            print('Number not in range 1..100')
            return get_guess('')
        return this_guess

def guessing_game():
    target = random.randint(1, 100)
    guess = get_guess('Guess a number between 1 and 100\n')
    tries = 1
    while guess != target:
        tries += 1
        if guess < target:
            guess = get_guess('Higher!\n')
        elif guess > target:
            guess = get_guess('Lower!\n')
    print(f'Correct! You took {tries} guesses.')
