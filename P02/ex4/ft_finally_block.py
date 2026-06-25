#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_finally_block.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/25 11:57:57 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/25 15:49:09 by nda-roch           ###   ########.fr      #
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


def water_plant(plant_name: str) -> None:
    if (plant_name == str.capitalize(plant_name)):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    input1 = ["Tomato", "Lettuce", "Carrots"]
    input2 = ["Tomato", "lettuce", "Carrots"]

    print("Testing valid plants...")
    print("Opening watering system")

    try:
        water_plant(input1[0])
        water_plant(input1[1])
        water_plant(input1[2])
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print("")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant(input2[0])
        water_plant(input2[1])
        water_plant(input2[2])
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if (__name__ == "__main__"):
    print("=== Garden Watering System ===")

    print("")

    test_watering_system()

    print("")

    print("Cleanup always happens, even with errors!")
