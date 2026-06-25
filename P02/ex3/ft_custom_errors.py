#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/23 12:58:53 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/25 15:23:35 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error") -> None:
        super().__init__(message)


def check_plant(plant: str) -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water(water: int) -> None:
    if (water < 10):
        raise WaterError("Not enough water in the tank!")


def test_plants() -> None:
    try:
        print("Testing PlantError...")
        check_plant("tomato")
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print("")
    try:
        print("Testing WaterError...")
        check_water(5)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print("")
    try:
        print("Testing catching all garden errors...")
        check_plant("tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(5)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("")
    print("All custom error types work correctly!")


if (__name__ == "__main__"):
    print("=== Custom Garden Errors Demo ===")
    print("")
    test_plants()
