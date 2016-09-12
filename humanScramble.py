def humanScramble(phrase):
    scrambledPhrase = ""    
    for word in phrase:
        scrambledPhrase = scrambledPhrase + humanScrambleWord(word)
    print(scrambledPhrase)

def humanScrambleWord(word):
    firstLetter = word[0]
    if len(word) > 1:
        lastLetter = word[-1]
    else:
        lastLetter = ''
    partOfWordToScramble = word[1:-1]
    scrambledPart = scrambleString(partOfWordToScramble)
    return firstLetter+scrambledPart+lastLetter

def scrambleString(string):
    originalString = string
    scrambledString = []
        
    return str(scrambledString)

print('''humanScramble('1234 5678 9876')''')
print(humanScramble('x y z'))

print('''humanScrambleWord('banana')''')
print(humanScrambleWord('banana'))
