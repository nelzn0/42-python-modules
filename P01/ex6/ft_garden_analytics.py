#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 16:48:45 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/15 17:57:07 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name, height, ages):
        self.name = name
        self._height = height
        self._ages = ages
        self.growth = 0
        self._n_age = 0
        self._n_grow = 0
        self._n_show = 0

    def get_height(self):
        return round(self._height)

    def get_age(self):
        return self._ages

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
        print(f"{self.name}: {round(self._height, 2)}cm, {self._ages} days old")
        self._n_show += 1

    def grow(self, height):
        self._height += height
        self._n_grow += 1

    def age(self, ages):
        self._ages += ages
        self._n_age += 1

    def stats(self):
        print(f"[statistics for {self.name}]")
        print(
            f"Stats: {self._n_grow} grow, {self._n_age} age, {self._n_show} show")

    @staticmethod
    def more_than_year(ages):
        if (ages < 365):
            return False
        else:
            return True

    @classmethod
    def anonymous(cls):
        anon = cls("Unknown plant", 0.0, 0)
        return anon


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
        self.__n_shade = 0

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        self.shade += 200.0
        print(
            f"Tree {self.name} now produces a shade of {self.shade}cm long and {self.trunk_diameter}cm wide.")
        self.__n_shade += 1

    def stats(self):
        super().stats()
        print(f"{self.__n_shade} shade")


class Seed(Flower):
    def __init__(self, name, height, ages, color):
        super().__init__(name, height, ages, color)
        self.seeds = 0

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")

    def bloom(self, blo):
        super().bloom(blo)
        if (blo == True):
            self.seeds += 42


if (__name__ == "__main__"):

    name = ["Rose", "Oak", "Sunflower"]
    height = [15.0, 200.0, 80.0]
    age = [10, 365, 45]
    year = [30, 400]

    print("=== Garden statistics ===")
    print("=== Check year-old")

    print(f"Is {year[0]} days more than a year? ->",
          Plant.more_than_year(year[0]))
    print(f"Is {year[1]} days more than a year? ->",
          Plant.more_than_year(year[1]))

    print("")

    print("=== Flower")

    for i in range(1):
        flower = Flower(name[i], height[i], age[i], "red")
        flower.show()

    flower.stats()

    print("[asking the rose to grow and bloom]")

    flower.grow(8)
    flower.bloom(True)
    flower.show()

    flower.stats()

    print("")

    print("=== Tree")

    for i in range(1, 2):
        tree = Tree(name[i], height[i], age[i], 5.0)
        tree.show()

    tree.stats()

    print("[asking the oak to produce shade]")

    tree.produce_shade()

    tree.stats()

    print("")

    print("=== Seed")

    for i in range(2, 3):
        seed = Seed(name[i], height[i], age[i], "yellow")
        seed.show()

    print("[make sunflower grow, age and bloom]")

    seed.grow(30)
    seed.age(20)
    seed.bloom(True)
    seed.show()
    seed.stats()

    print("")

    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    anon.stats()
