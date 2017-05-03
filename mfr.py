import string

with open('Treasure_Island.txt') as f:
    text_words = (f.read()
            .lower()
            .strip()
            .split())

def wordfrequency(l, word):
    filter(lambda x: x == word, l)
    map(lambda x: 1, l)
    return reduce(lambda a, b: a + b, l)


def totalfrequency(l, list):
    filter(lambda x: x in list, l)
    map(lambda x: 1, l)
    return reduce(lambda a, b: a + b, l)

def mostfrequent(l):
    dict = {}
    for e in l:
        dict[e] = (dict[e] + 1) if e in dict.keys() else 1
    return reduce(lambda a, b: a if dict[a] > dict[b] else b, dict.keys())
