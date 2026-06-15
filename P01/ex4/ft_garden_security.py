#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:42:48 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/15 16:47:07 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name, height, ages):
        self.name = name
        self.__height = height
        self.__ages = ages
        self.growth = 0

    def get_height(self):
        return round(self.__height)

    def get_age(self):
        return self.__ages

    def set_height(self, height):
        if (height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.__height = height
            print(f"Height updated: {Plant.get_height(self)}cm")

    def set_age(self, age):
        if (age < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__ages = age
            print(f"Age updated: {Plant.get_age(self)} days")

    def show(self):
        print(f"{self.name}: {round(self.__height, 2)}cm, {self.__ages} days old")

    def grow(self):
        self.height += 0.8
        self.growth += 0.8

    def age(self):
        self.ages += 1


if (__name__ == "__main__"):

    name = ["Rose", "Sunflower", "Cactus", "Sunflower", "Fern"]
    height = [15.0, 200, 5, 80, 15]
    age = [10, 365, 90, 45, 120]

    print("=== Garden Security System ===")
    for i in range(1):
        plant = Plant(name[i], height[i], age[i])
        print("Plant created: ", end="")
        plant.show()

    print("")

    plant.set_height(25.0)
    plant.set_age(30)

    print("")

    plant.set_height(-25)
    plant.set_age(-30)

    print("")

    print("Current state: ", end="")
    plant.show()
