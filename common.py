import os
import player_module
import board_module

def getch():    # define function getch() to read exactly one character from user's input
    import sys, tty, termios    # include librares sys, tty and termios to the project
    fd = sys.stdin.fileno() # assign file descriptor (int) returned by stdin.fileno() method to fd variable
    old_settings = termios.tcgetattr(fd)    # assign a list containing the tty attributes for file descriptor fd returned by tcgetattr() method
    try:    # execute the statements if no exceptions occures
        tty.setraw(sys.stdin.fileno())  # change the mode of the file descriptor returned by stdin.fileno() to raw
        ch = sys.stdin.read(1)  # call function stdin.read with argument 1 to read into the user-entered string of length 1
    finally:    # do the following statements even if exception occurs
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # change tty attributes for file descriptor fd from attributes list old_settings after transmitting all queued output
    return ch

def set_step(starting_point, destination):
    if starting_point > destination:
        return -1
    else:
        return 1

def fight(player, enemy):
    attacker = player
    defender = enemy
    while player.health_points > 0 and enemy.health_points > 0:
        hitted = attacker.attack(defender)
        if hitted:
            print("{} attack  {} and dealt {} damage. {} HP left".format(attacker.name, defender.name, str(attacker.damage), defender.health_points))
        else:
            print("{} dodged.".format(defender.name, defender.health_points))
        attacker, defender = defender, attacker

    if player.health_points <= 0:
        print("GAME OVER")
        getch()
    else:
        print("You defeated {}! press any key to continue...".format(enemy.name))
        enemy.reset_hp()
        getch()