#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/13 18:21:45 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/13 18:21:52 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name, height, ages):
        self.name = name
        self.height = height
        self.ages = ages

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.ages} days old")

    def grow(self):
        self.height += 0.8

    def age(self):
        self.ages += 1


plant1 = Plant("Rose", 25, 30)

day = 0


print("=== Garden Plant Growth ===")
plant1.show()
while (day < 7):
    day += 1
    print(f"=== Day {day} ==")
    plant1.grow()
    plant1.age()
    plant1.show()

print(f"Growth this week: {total}")
if (__name__ == "__main__"):
    print("=== End of Program ===")
