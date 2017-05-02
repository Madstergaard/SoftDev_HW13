



def wordfrequency(data, word):
    l = data.split(' ')
    filter(lambda x: x == word, l)
    map(lambda x: 1, l)
    return reduce(lambda a, b: a + b, l)


def totalfrequency(data, list):
    l = data.split(' ')
    filter(lambda x: x in list, l)
    map(lambda x: 1, l)
    return reduce(lambda a, b: a + b, l)

def mostfrequent(data):
    l = data.split(' ')
    
