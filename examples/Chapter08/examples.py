def found_values(l, d):
    output = []
    for k in l:
        v = d.get(k)
        if v != None:
            output.append(v)
    return output



>>> def f(x, y): return x + y + z
... 
>>> f(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in f
NameError: name 'z' is not defined
>>> z = 3
>>> f(1, 2)
6

def safe_lookup(d, k):
    try:
        return d[k]
    except KeyError as e:
        print(f'FATAL ERROR: Bad key {k} in dict {d}')
        raise e


def repeated(e, length):
    if length < 0: raise ValueError
    l = []
    for x in range(0, length): l.append(e)
    return l


def safe_lookup(d, k):
    try:
        result = d[k]
    except Exception as e:
        print('Unknown error in safe_lookup')
        raise e
    else:
        print('key lookup succeeded')
        return result

#Two things to fix: wrong input, and int() might raise ValueError

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
        print(f'target: {target}, guess: {guess}')
        tries = tries + 1
        if guess < target:
            guess = get_guess('Higher!\n')
        elif guess > target:
            guess = get_guess('Lower!\n')
    print('Correct! You took ' + str(tries) + ' guesses.')

