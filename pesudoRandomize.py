import random
def humanScramble(phrase):
    l_phrase = phrase.split(' ')
    scrambled = []
    for word in l_phrase:
        scrambled.append(humanScrambleWord(word))
    return ' '.join(scrambled)

def humanScrambleWord(word):
    suffix = ''
    if word[-1] in [';','.']:
        suffix = word[-1]
        word = word[:-1]
    if len(word) <= 3:
        return word + suffix
    else:
        middle = word[1:-1]
        return str(word[0] + scrambleString(middle) + word[-1] + suffix)

def scrambleString(s):
    return ''.join(random.sample(s,len(s)))
