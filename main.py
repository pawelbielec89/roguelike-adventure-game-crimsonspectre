import common
import os
import player_module
from board_module import Board
from random import randint


def main():
    monsters = [["Rat", "R", 20, 20, 5, 2], 
                ["Bat", "B", 40, 40, 10, 4], 
                ["Snake", "S", 60, 60, 15, 6]]
    monsters_list = []
    number_of_monsters = randint(10,20)
    inventory = {}

    player = player_module.Player(1,1,"Player", "V", 30, 15, 1, "male", 100, inventory)

    for monster_properties in monsters:
        monster = player_module.Character(*monster_properties)
        monsters_list.append(monster)

    dungeon = Board(40,100)
    dungeon.generate_dungeon(player.avatar, monsters_list)

    while True:
        dungeon.draw_board()
        x,y = player.move(dungeon, monsters_list)
        collision = dungeon.check_collision(player.x_coord, player.y_coord)
        dungeon.update_board(x, y, player.x_coord, player.y_coord, player.avatar)
        
        for monster in monsters_list:
            if collision == monster.avatar:
                common.fight(player,monster)


if __name__ == "__main__":
    main()