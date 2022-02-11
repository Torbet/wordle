from wordle.board import Board
from wordle.helpers import getInput
import os

def main():
    os.system('clear')
    board = Board()
    while board.isOngoing():
        print(board)
        print("enter word")
        w = ""
        for i in range(5):
            c = getInput()
            w += c
            board.board[board.currentRow][i] = c
            print(board)
        board.addWord(w)
        print(board)

if __name__ == '__main__':
    main()
