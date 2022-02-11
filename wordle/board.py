from wordle.helpers import *
import os

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

    def isOngoing(self):
        return not(self.currentRow == self.rows)

    def addWord(self, word):
        if isValid(word):
            for i in range(len(word)):
                self.board[self.currentRow][i] = word[i]
            self.currentRow += 1
        else: 
            self.board[self.currentRow] = ['-', '-', '-', '-', '-']


    def __str__(self):
        import os
        os.system('clear')
        self.display()
        return ''
