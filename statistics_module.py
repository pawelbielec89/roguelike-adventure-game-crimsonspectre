import time
import os
import common

class Statistics:
    def __init__ (self, name = "", health_points = 10, damage = 1, dexterity = 1, sex = "", thirst = 25):

        self.name = name
        self.health_points = health_points
        self.damage = damage
        self.dexterity = dexterity
        self.sex = sex
        self.thirst = thirst

    def set_statistics(self):
        os.system("clear")
        self.name = input("Type your name:")

        while self.sex != "m" and self.sex != "f":
            os.system("clear")
            self.sex = input("Are you male of female? (m/f)")
            print ("Type 'm' for male and 'f' for female")

        stats_points = 10

        while stats_points > 0:
            stat_choose = ""
            os.system("clear")
            print("Health points: " + str(self.health_points) + "\n" +
                  "Damage:" + str(self.damage) + "\n" +
                  "Dexterity:" + str(self.dexterity) + "\n\n" +
                  "Points avaliable:" + str(stats_points))
            try:
                points_to_spend = int(input("How many points you want to spend?"))
                if points_to_spend > stats_points or points_to_spend < 1:
                    print("Wrong value!")
                    common.wait_for_enter()
                else:
                    while stat_choose != "hp" and stat_choose != "dmg" and stat_choose != "dex" :
                        stat_choose = input("Which statistic do you want to add? (hp/dmg/dex)")
                        if stat_choose != "hp" and stat_choose != "dmg" and stat_choose != "dex" :
                            print ("Type 'hp' for health points, 'dmg' for damage and 'dex' for dexterity")
                    if stat_choose == "hp":
                        self.health_points += points_to_spend * 10
                    elif stat_choose == "dmg":
                        self.damage += points_to_spend
                    else:
                        self.dexterity += points_to_spend


                    stats_points -= points_to_spend

            except:
                print("Please enter number!")
                common.wait_for_enter()
