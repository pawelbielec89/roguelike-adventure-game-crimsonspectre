import common
import os
from board_module import Board
from random import randint
import time


class Character:

    def __init__ (self, avatar, name, health_points, max_hp, damage, dexterity):
        self.name = name
        self.avatar = "\033[30;47m" + avatar + "\033[0m"
        self.health_points = health_points
        self.max_hp = max_hp
        self.damage = damage
        self.dexterity = dexterity


    def reset_hp(self):
        self.health_points = self.max_hp


    def made_dodge(self, enemy):
        probability = randint(1,10)
        if enemy.dexterity > probability:
            return True
        else:
            return False


    def attack(self, enemy):
        if self.made_dodge(enemy):
            return False
        else:
            enemy.health_points -= self.damage
            if enemy.health_points < 0:
                enemy.health_points = 0

            return True


class Player (Character):
        def __init__ (self, avatar, statistics, inventory, x_coord = 1, y_coord = 1, monsters_killed = 0):
            self.x_coord = x_coord
            self.y_coord = y_coord
            self.avatar = "\033[31;47m" + avatar + "\033[0m"
            self.name = statistics.name
            self.health_points = statistics.health_points
            self.damage = statistics.damage
            self.dexterity = statistics.dexterity
            self.sex = statistics.sex
            self.thirst = statistics.thirst
            self.inventory = inventory
            self.monsters_killed = monsters_killed


        def made_dodge(self, enemy):
            super().made_dodge(enemy)


        def fight(self, enemy):
            super().fight(enemy)


        def check_event(self, board, x, y, monsters_list):
            for monster in monsters_list:
                if board.board[x][y] == monster.avatar:
                    self.fight(monster)

        def move(self, board, monsters_list, direction):
            repeat = True

            while repeat:
                repeat = False
                old_x = self.x_coord
                old_y = self.y_coord

                if direction == 'w':
                    self.x_coord -= 1
                elif direction == 's':
                    self.x_coord += 1
                elif direction == 'a':
                    self.y_coord -= 1
                elif direction == 'd':
                    self.y_coord += 1

                if self.x_coord > board.height-1 or self.y_coord > board.width-1:
                    repeat = True
                    direction = common.getch()
                    self.x_coord, self.y_coord = old_x, old_y

                collision_type = board.check_collision(self.x_coord, self.y_coord)

                if collision_type == board.WALL:
                    repeat = True
                    direction = common.getch()
                    self.x_coord, self.y_coord = old_x, old_y
                elif repeat == False:
                    return old_x, old_y

        def add_to_inventory(self, added_items):
            sum_weight = added_items[1]
            for key, value in self.inventory.items():
                sum_weight += value[1]

            if sum_weight > 100:
                print("You cannot grab this thing (it's too heavy)")
                common.wait_for_enter()
            else:
                key = added_items[0]

                if key == 'sword':
                    self.damage += 5
                elif key == 'health potion':
                    self.health_points += 10
                elif key == 'braces':
                    self.dexterity += 1

                weight = added_items[1]
                if key in self.inventory:
                    self.inventory[key][0] += 1
                    self.inventory[key][1] += weight
                else:
                    self.inventory[key] = [0, 0]
                    self.inventory[key][0] = 1
                    self.inventory[key][1] = weight
