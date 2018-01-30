import common
import os
import ui

class Board:

    def __init__ (self, height, width):
        self.height = height
        self.width = width


    def build_board(self):
        BOARD_HEIGHT = self.height  
        BOARD_WIDTH = self.width   
        WALL = '#' 
        EMPTY = ' ' 
        PLAYER = '@' 
        self.board = []  

        for i in range(BOARD_HEIGHT):   # loop in range from 0 to height of board
            line = []   # declare empty list line
            for j in range(BOARD_WIDTH):    # loop in range from 0 to width of board
                if i == 0 or i == 9 or j == 0 or j == 9:    # do the following statements if conditions are fullfilled
                    line.append(WALL)   # add constant WALL ('#') to the list line
                else:   # do the following statement if conditions are not fullfilled
                    line.append(EMPTY)  # add constant EMPTY (' ') to the list line
            self.board.append(line)  # add list line to the list board
        
        # set player position
        self.board[1][1] = PLAYER
    
    def draw_board(self):  # print the list given as an argument

        for i in self.board: # loop through first dimension of board
            print(*i)
    

    def check_collision(self, x, y):
        if self.board[x][y] == '#':
            return True
        else:
            return False

    
    def update_board(self, previous_x, previous_y, new_x, new_y):
        self.board[new_x][new_y] = '@'
        self.board[previous_x][previous_y] = ' '