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

def getInput():
    import termios
    import sys, tty
    def _g():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return _g()
