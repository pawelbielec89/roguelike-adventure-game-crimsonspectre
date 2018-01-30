import common
import os
from board_module import Board

class Character:

    def __init__ (self, x_coord, y_coord, name, avatar, health_points, damage, dexterity):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.name = name
        self.avatar = avatar
        self.health_points = health_points
        self.damage = damage
        self.dexterity = dexterity
    
    def move(self, board):
        repeat = True

        while repeat:
            repeat = False
            direction = common.getch()
            new_x = self.x_coord
            new_y = self.y_coord

            if direction == 'w':    # do the following statements if conditions are fullfilled
                new_x -= 1  #decrementation of new_y varible
            elif direction == 's':  # do the following statements if conditions are fullfilled
                new_x += 1  # incrementation of new_x varible
            elif direction == 'a':  # do the following statements if conditions are fullfilled
                new_y -= 1  #decrementation of new_y varible
            elif direction == 'd':  # do the following statements if conditions are fullfilled
                new_y += 1  # incrementation of new_y varible
            elif direction == 'q':  # do the following statements if conditions are fullfilled
                exit(0) # call funtions exit with argument 0 to quit the program
            
            is_collision = board.check_collision(new_x, new_y)

            if is_collision:
                repeat = True
            else:
                board.update_board(self.x_coord, self.y_coord, new_x, new_y)
                self.x_coord = new_x
                self.y_coord = new_y
        
    
    def attack():
        pass
