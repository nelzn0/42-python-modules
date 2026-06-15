#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 15:37:19 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/15 16:48:25 by nda-roch           ###   ########.fr      #
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

    def grow(self, height):
        self.__height += height
        self.nutritional_value += 10

    def age(self, ages):
        self.__ages += ages
        self.nutritional_value += 10


class Flower(Plant):
    def __init__(self, name, height, ages, color):
        super().__init__(name, height, ages)
        self.color = color
        self.blo = False

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if (self.blo == False):
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

    def bloom(self, blo):
        self.blo = blo


class Tree(Plant):
    def __init__(self, name, height, ages, trunk_diameter):
        super().__init__(name, height, ages)
        self.trunk_diameter = trunk_diameter
        self.shade = 0

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        self.shade += 200.0
        print(
            f"Tree {self.name} now produces a shade of {self.shade}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name, height, ages, harvest_season):
        super().__init__(name, height, ages)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if (__name__ == "__main__"):

    name = ["Rose", "Oak", "Tomato"]
    height = [15.0, 200.0, 5.0]
    age = [10, 365, 10]
    color = "red"
    trunk_diameter = 5.0
    harvest_season = "April"

    print("=== Garden Plant Types ===")

    print("=== Flower")

    for i in range(1):
        flower = Flower(name[i], height[i], age[i], color)
        flower.show()

    print("[asking the rose to bloom]")

    flower.bloom(True)
    flower.show()

    print("")

    print("=== Tree")

    for i in range(1, 2):
        tree = Tree(name[i], height[i], age[i], trunk_diameter)
        tree.show()

    print("[asking the oak to produce shade]")

    tree.produce_shade()

    print("")

    print("=== Vegetable")

    for i in range(2, 3):
        vegetable = Vegetable(name[i], height[i], age[i], harvest_season)
        vegetable.show()

    print("[make tomato grow and age for 20 days]")

    vegetable.grow(42)
    vegetable.age(20)
    vegetable.show()
