import random

def getWords(articleFile):
    openFile = open(articleFile)
    temp = list()
    for line in openFile:
        line = line.strip('\n')
        temp.append(line)
    words = tuple(temp)

    return words
    

articles = getWords('articles.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')
nouns = getWords('nouns.txt')


def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()
