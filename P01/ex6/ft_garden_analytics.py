#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 16:48:45 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/18 17:32:33 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def display_stats(plant):
    plant.stat.display()


class Plant:
    class Stats:
        def __init__(self, name):
            self._name = name
            self._n_age = 0
            self._n_grow = 0
            self._n_show = 0

        def display(self):
            print(f"[statistics for {self._name}]")
            print(f"Stats: {self._n_grow} grow, "
                  f"{self._n_age} age, {self._n_show} show")

    def __init__(self, name, height, ages):
        self.name = name
        self._height = height
        self._ages = ages
        self.stat = Plant.Stats(self.name)

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
        print(f"{self.name}: "
              f"{round(self._height, 2)}cm, {self._ages} days old")
        self.stat._n_show += 1

    def grow(self, height):
        self._height += height
        self.stat._n_grow += 1

    def age(self, ages):
        self._ages += ages
        self.stat._n_age += 1

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
        if (self.blo is False):
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

    def bloom(self):
        self.blo = True


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self, name):
            super().__init__(name)
            self._n_shade = 0

        def display(self):
            print(f"[statistics for {self._name}]")
            print(f"Stats: {self._n_grow}"
                  f" grow, {self._n_age} age, {self._n_show} show")
            print(f"{self._n_shade} shade")

    def __init__(self, name, height, ages, trunk_diameter):
        super().__init__(name, height, ages)
        self.trunk_diameter = trunk_diameter
        self.shade = 0
        self.stat = Tree.Stats(self.name)

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        self.shade += 200.0
        print(f"Tree {self.name} now produces a shade of"
              f" {self.shade}cm long and {self.trunk_diameter}cm wide.")
        self.stat._n_shade += 1


class Seed(Flower):
    def __init__(self, name, height, ages, color):
        super().__init__(name, height, ages, color)
        self.seeds = 0

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")

    def bloom(self):
        super().bloom()
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

    display_stats(flower)

    print("[asking the rose to grow and bloom]")

    flower.grow(8)
    flower.bloom()
    flower.show()

    display_stats(flower)

    print("")

    print("=== Tree")

    for i in range(1, 2):
        tree = Tree(name[i], height[i], age[i], 5.0)
        tree.show()

    display_stats(tree)

    print("[asking the oak to produce shade]")

    tree.produce_shade()

    display_stats(tree)

    print("")

    print("=== Seed")

    for i in range(2, 3):
        seed = Seed(name[i], height[i], age[i], "yellow")
        seed.show()

    print("[make sunflower grow, age and bloom]")

    seed.grow(30)
    seed.age(20)
    seed.bloom()
    seed.show()
    display_stats(seed)

    print("")

    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    display_stats(anon)
