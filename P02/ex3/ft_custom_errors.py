#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/23 12:58:53 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/23 13:31:56 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


def test_plants():
    try:
        print("Testing PlantError...")
        raise PlantError
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print("")
    try:
        print("Testing WaterError...")
        raise WaterError
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print("")
    try:
        print("Testing catching all garden errors...")
        raise PlantError
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("")
    print("All custom error types work correctly!")


if (__name__ == "__main__"):
    print("=== Custom Garden Errors Demo ===")
    print("")
    test_plants()
