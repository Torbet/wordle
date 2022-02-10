def getPossibleWords():
    fileObj = open("data/possible_words.txt", "r")
    words = fileObj. read(). splitlines()
    fileObj. close()
    return words

def isValid(word):
    if word in getPossibleWords():
        return True
    else:
        return False

