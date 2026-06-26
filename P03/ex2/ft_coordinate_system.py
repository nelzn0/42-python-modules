#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/26 13:24:47 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/26 14:56:25 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math


def get_player_pos() -> tuple[float, ...]:
    coords: tuple[float, ...] = ()
    while True:
        try:
            coords = ()
            xyz_input = input(
                "Enter new coordinates as floats in format 'x,y,z': ")
            x, y, z = xyz_input.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            for n in x, y, z:
                coords += (float(n.strip()),)
            return coords
        except ValueError as e:
            print(f"Error on parameter '{n.strip()}': {e}")


if (__name__ == "__main__"):
    print("=== Game Coordinate System ===")

    print("")

    print("Get a first set of coordinates")

    coords = get_player_pos()

    print(f"Got a first tuple: {coords}")
    print(f"It includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")

    d1 = round(math.sqrt((coords[0])**2 + (coords[1])**2 + (coords[2])**2), 4)

    print(f"Distance to center: {d1}")

    print("")

    print("Get a second set of coordinates")

    coords2 = get_player_pos()

    d2 = round(math.sqrt((coords2[0] - coords[0])**2 +
               (coords2[1] - coords[1])**2 + (coords2[2] - coords[2])**2), 4)

    print(f"Distance to center: {d2}")
