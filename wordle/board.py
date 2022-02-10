from utils import *

class Board():
    def __init__(self):
        self.cols = 5
        self.rows = 6
        self.currentRow = 0

        self.board = [['-' for col in range(self.cols)] for row in range(self.rows)]

    def display(self):
        for row in self.board:
            print()
            for col in row:
                print(col, end=' ')


    def addWord(self, word):
        if Utils.isValid(word):
            for i in range(len(word)):
                self.board[self.currentRow][i] = word[i]
            self.currentRow += 1


    def __str__(self):
        self.display()
        return ''
