#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:42:48 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/18 17:22:58 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name, height, ages):
        self.name = name
        self._height = height
        self._ages = ages

    def get_height(self):
        return round(self._height)

    def get_age(self):
        return self._ages

    def set_height(self, height):
        if (height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {Plant.get_height(self)}cm")

    def set_age(self, ages):
        if (ages < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._ages = ages
            print(f"Age updated: {Plant.get_age(self)} days")

    def show(self):
        print(f"{self.name}: {round(self._height, 2)}cm, {self._ages} days old")


if (__name__ == "__main__"):

    name = ["Rose", "Sunflower", "Cactus", "Sunflower", "Fern"]
    height = [15.0, 200, 5, 80, 15]
    ages = [10, 365, 90, 45, 120]

    print("=== Garden Security System ===")
    for i in range(1):
        plant = Plant(name[i], height[i], ages[i])
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
