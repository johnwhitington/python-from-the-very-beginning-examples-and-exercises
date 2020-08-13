#Text statistics: lines, characters, word, sentences.
def is_full_stop(s):
    return s == '.'

def stats_from_file(f):
    lines = 0
    characters = 0
    words = 0
    sentences = 0
    for line in f:
        lines += 1
        characters += len(line)
        words += len(line.split())
        sentences += len(list(filter(is_full_stop, line)))
    return (lines, characters, words, sentences)

def stats_from_filename(filename):
    with open(filename) as f:
        return stats_from_file(f)

gregor_stats = stats_from_filename('gregor.txt')

