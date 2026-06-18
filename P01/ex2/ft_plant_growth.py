#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/13 18:21:45 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/18 17:20:26 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name, height, ages, growth_rate):
        self.name = name
        self.height = height
        self.ages = ages
        self.growth = 0
        self.growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {round(self.height, 2)}cm, {self.ages} days old")

    def grow(self):
        self.height += self.growth_rate
        self.growth += self.growth_rate

    def age(self):
        self.ages += 1


if (__name__ == "__main__"):

    plant1 = Plant("Rose", 25.0, 30, 0.8)
    plant2 = Plant("Sunflower", 13.0, 10, 5)

    day = range(1, 8)

    print("=== Garden Plant Growth ===")

    plant1.show()

    for n in day:
        print(f"=== Day {n} ==")
        plant1.grow()
        plant1.age()
        plant1.show()

    print(f"Growth this week: {plant1.growth}cm")

    print("")

    plant2.show()

    for n in day:
        print(f"=== Day {n} ==")
        plant2.grow()
        plant2.age()
        plant2.show()

    print(f"Growth this week: {plant2.growth}cm")
