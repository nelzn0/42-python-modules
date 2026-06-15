#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:42:48 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/15 14:42:55 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name, height, ages):
        self.name = name
        self.height = height
        self.ages = ages
        self.growth = 0

    def show(self):
        print(f"{self.name}: {round(self.height, 2)}cm, {self.ages} days old")

    def grow(self):
        self.height += 0.8
        self.growth += 0.8

    def age(self):
        self.ages += 1


if (__name__ == "__main__"):

    name = ["Rose", "Sunflower", "Cactus", "Sunflower", "Fern"]
    height = [25, 200, 5, 80, 15]
    age = [30, 365, 90, 45, 120]

    print("=== Plant Factory Output ===")
    for i in range(5):
        plant = Plant(name[i], height[i], age[i])
        print("Created: ", end="")
        plant.show()
