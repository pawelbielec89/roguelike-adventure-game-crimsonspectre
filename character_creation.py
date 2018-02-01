import time
import os
player_stats = {"x_coord": 1, "y_coord": 1, "name": "Player_name",
                     "avatar": "\033[31;47m" + "avatar" + "\033[0m",
                     "health_points": 1, "damage": 1, "dexterity": 1,
                     "sex": "sex", "thirst": 0, "inventory": {}}

def character_creation(player_stats):
    player_stats["name"] = input("Type your name:")
    while player_stats["sex"] != "m" and player_stats["sex"] != "f":
        player_stats["sex"] = input("Are you male of female? (m/f)")
        print ("Type 'm' for male and 'f' for female")
    stats_points = 10
    while stats_points > 0:
        stat_choose = ""
        os.system("clear")
        print("Health points:" + str(player_stats["health_points"]) + "\n" +
              "Damage:" + str(player_stats["damage"]) + "\n" +
              "Dexterity:" + str(player_stats["dexterity"]) + "\n" +
              "Points avaliable:" + str(stats_points))
        try:
            points_to_spend = int(input("How many points you want to spend?"))
            if points_to_spend > stats_points:
                print("You don't have enough points!")
                time.sleep(2)
            elif points_to_spend < stats_points:
                player_stats = add_points_to_stats(stat_choose, player_stats, points_to_spend)

                stats_points = stats_points - points_to_spend
            else:
                player_stats = add_points_to_stats(stat_choose, player_stats, points_to_spend)
                stats_points = 0
        except:
            print("Please enter number")
            time.sleep(2)
    return player_stats


def add_points_to_stats(stat_choose, player_stats, points_to_spend):

    while stat_choose != "hp" and stat_choose != "dmg" and stat_choose != "dex" :
        stat_choose = input("Which statistic you want to add? (hp/dmg/dex)")
        if stat_choose != "hp" and stat_choose != "dmg" and stat_choose != "dex" :
            print ("Type 'hp' for health points, 'dmg' for damage and 'dex' for dexterity")
    if stat_choose == "hp":
        player_stats["health_points"] = points_to_spend + player_stats["health_points"]
    elif stat_choose == "dmg":
        player_stats["damage"] = points_to_spend + player_stats["damage"]
    else:
        player_stats["dexterity"] = points_to_spend + player_stats["dexterity"]
    return player_stats

os.system("clear")
character_creation(player_stats)
