import common
import os
import ui
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
    
    
        
