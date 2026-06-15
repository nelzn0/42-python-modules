#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/13 18:21:21 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/15 14:39:34 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if (__name__ == "__main__"):

    name = ["Rose", "Sunflower", "Cactus"]
    height = [25, 80, 45]
    age = [30, 45, 120]

    plant1 = Plant(name[0], height[0], age[0])
    plant2 = Plant(name[1], height[1], age[1])
    plant3 = Plant(name[2], height[2], age[2])

    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()
