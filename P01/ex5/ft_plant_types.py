#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 15:37:19 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/18 17:23:26 by nda-roch           ###   ########.fr      #
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

    def set_age(self, age):
        if (age < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._ages = age
            print(f"Age updated: {Plant.get_age(self)} days")

    def show(self):
        print(f"{self.name}: {round(self._height, 2)}cm, {self._ages} days old")

    def grow(self, height):
        self._height += height

    def age(self, ages):
        self._ages += ages


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

    def bloom(self):
        self.blo = True


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

    def grow(self, height):
        super().grow(height)
        self.nutritional_value += 10

    def age(self, age):
        super().age(age)
        self.nutritional_value += 10


if (__name__ == "__main__"):

    name = ["Rose", "Oak", "Tomato"]
    height = [15.0, 200.0, 5.0]
    age = [10, 365, 10]

    print("=== Garden Plant Types ===")

    print("=== Flower")

    for i in range(1):
        flower = Flower(name[i], height[i], age[i], "red")
        flower.show()

    print("[asking the rose to bloom]")

    flower.bloom()
    flower.show()

    print("")

    print("=== Tree")

    for i in range(1, 2):
        tree = Tree(name[i], height[i], age[i], 5.0)
        tree.show()

    print("[asking the oak to produce shade]")

    tree.produce_shade()

    print("")

    print("=== Vegetable")

    for i in range(2, 3):
        vegetable = Vegetable(name[i], height[i], age[i], "April")
        vegetable.show()

    print("[make tomato grow and age for 20 days]")

    vegetable.grow(42)
    vegetable.age(20)
    vegetable.show()
