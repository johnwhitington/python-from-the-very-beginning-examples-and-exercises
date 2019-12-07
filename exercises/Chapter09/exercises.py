#1
with open('gregor.txt') as f:
    for line in f:
        print(line, end='')

#2
def dict_to_file(d, filename):
    with open(filename, 'w') as f:
        for k, v in d.items():
            print(k, file=f)
            print(v, file=f)


#3
def dict_from_file(filename):
    d = {}
    with open(filename) as f:
        while True:
            try:
                k = f.readline()
                v = f.readline().strip()
                if k !='' and v !='':
                    d[int(k)] = v
                else:
                   return d
            except ValueError:
                print(f'{k} is not an integer')
                return None
        

#4
def append_files(a, b, c):
    with open(a) as f_a, open(b) as f_b, open(c, 'a') as f_c:
        print(f_a.read(), file=f_c, end='')
        print(f_b.read(), file=f_c, end='')


#5
def sum_file(filename):
    with open(filename) as f:
        return sum(map(int, f.read().split()))

#6
def copy_file(a, b):
    with open(a) as f_in, open(b, 'w') as f_out:
        print(f_in.read(), file=f_out, end='')

#7
def is_full_stop(s):
    return s == '.'

def stats_from_file(f):
    lines = 0
    characters = 0
    words = 0
    sentences = 0
    histogram = {}
    for line in f:
        lines += 1
        characters += len(line)
        words += len(line.split())
        sentences += len(list(filter(is_full_stop, list(line))))
        for x in line:
            current = 0
            if x in histogram:
                current = histogram[x]
            histogram[x] = current + 1
    return (lines, characters, words, sentences, histogram)

def stats_from_filename(filename):
    with open(filename) as f:
        return stats_from_file(f)

gregor_stats = stats_from_filename('gregor.txt')

#8
import string

def cleansplit(line):
    return [s.strip(string.punctuation).lower() for s in line.split()]

def is_full_stop(s):
    return s == '.'

def stats_from_file(f):
    lines = 0
    characters = 0
    words = 0
    sentences = 0
    histogram = {}
    word_histogram = {}
    for line in f:
        lines += 1
        characters += len(line)
        words += len(line.split())
        sentences += len(list(filter(is_full_stop, list(line))))
        for x in line:
            current = 0
            if x in histogram:
                current = histogram[x]
            histogram[x] = current + 1
        for x in cleansplit(line):
            current = 0
            if x in word_histogram:
                current = word_histogram[x]
            word_histogram[x] = current + 1
    return (lines, characters, words, sentences, histogram, word_histogram)

def stats_from_filename(filename):
    with open(filename) as f:
        return stats_from_file(f)

gregor_stats = stats_from_filename('gregor.txt')


#9
import string

def cleansplit(line):
    return [s.strip(string.punctuation).lower() for s in line.split()]

def search_word(filename, word):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    words = list(map(cleansplit, lines))
    for n, ws in enumerate(words):
        if word in ws:
            print(f'{n}: ', end='')
            print(lines[n], end='')

#10
def top(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    while(len(lines) > 0):
        for l in lines[:5]: print(l, end='')
        lines = lines[5:]
        enter = input()

