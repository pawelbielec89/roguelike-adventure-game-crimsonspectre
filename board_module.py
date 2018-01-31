import common
import os
from random import randint

class Board:

    def __init__ (self, height, width):
        self.height = height
        self.width = width
        self.WALL = ' ' 
        self.FLOOR = '\033[37;47m#\033[0m'


    def draw_board(self):  # print the list given as an argument

        for i in self.board: # loop through first dimension of board
            print(*i, sep="")


    def generate_corridor(self, from_x, to_x, from_y, to_y):

        step = common.set_step(from_x, to_x)

        for i in range(from_x, to_x, step):
            self.board[i][to_y] = self.FLOOR

        step = common.set_step(from_y, to_y)

        for i in range(from_y, to_y, step):
            self.board[from_x][i] = self.FLOOR


    def generate_room(self, min_height, max_height, min_width, max_width):
        room_height = randint(min_height,max_height)
        room_width = randint(min_width,max_width)
        MAX_HEIGHT = self.height - 1 - room_height
        MAX_WIDTH = self.width - 1 - room_width

        start_position_x = randint(1, MAX_HEIGHT)
        start_position_y = randint(1, MAX_WIDTH)
        
        for i in range(room_height):
            for j in range(room_width):
                self.board[i + start_position_x][j + start_position_y] = self.FLOOR

        return start_position_x, start_position_y


    def create_first_room(self):
        for i in range(1,7):
            for j in range(1,7):
                self.board[i][j] = self.FLOOR
        
        return 3, 3


    def generate_dungeon(self):
        BOARD_HEIGHT = self.height  
        BOARD_WIDTH = self.width   
        print(BOARD_HEIGHT, BOARD_WIDTH)
        
        self.board = []

        for i in range(BOARD_HEIGHT):
            line = []
            for j in range(BOARD_WIDTH):
                line.append(self.WALL)
            self.board.append(line)

        from_x, from_y = self.create_first_room()

        for i in range(10):
            to_x, to_y = self.generate_room(3,5,3,12)
            self.generate_corridor(from_x, to_x, from_y, to_y)
            # set coords of new room as starting point for next corridor
            from_x, from_y = to_x, to_y
        

    def build_board(self):
        BOARD_HEIGHT = self.height  
        BOARD_WIDTH = self.width
        PLAYER = '@' 
        self.board = []  

        for i in range(BOARD_HEIGHT):   # loop in range from 0 to height of board
            line = []   # declare empty list line
            for j in range(BOARD_WIDTH):    # loop in range from 0 to width of board
                if i == 0 or i == BOARD_HEIGHT - 1 or j == 0 or j == BOARD_WIDTH - 1:    # do the following statements if conditions are fullfilled
                    line.append(self.WALL)   # add constant WALL ('#') to the list line
                else:   # do the following statement if conditions are not fullfilled
                    line.append(self.FLOOR)  # add constant FLOOR (' ') to the list line
            self.board.append(line)  # add list line to the list board
        
        # set player position
        self.board[1][1] = PLAYER
    
    
    def check_collision(self, x, y):
        if self.board[x][y] == self.WALL:
            return True
        else:
            return False

    
    def update_board(self, previous_x, previous_y, new_x, new_y, avatar):
        self.board[new_x][new_y] = avatar
        self.board[previous_x][previous_y] = self.FLOOR