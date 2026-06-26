#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/26 16:50:36 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/26 18:46:45 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys

inventory = {
    "name": "name",
    "value": 0
}


def fill_inv(args: list) -> dict:

    for n in args:
        item = n.split(":")
        if item[0] in inv.keys():
            print(f"Redundant item '{item[0]}' - discarding")
        else:
            try:
                inv.update({item[0]: int(item[1])})
            except IndexError:
                print(f"Error - invalid parameter '{n}'")
            except ValueError as e:
                print(f"Quantity error for '{item[0]}': {e}")
    return (inv)


if (__name__ == "__main__"):

    inv = {}

    print("=== Inventory System Analysis ===")

    inv = fill_inv(sys.argv[1:])

    if len(inv) > 0:
        print(f"Got inventory: {inv}")
        print(f"Item list: {list(inv.keys())}")
        print(f"Total quantity of the {len(inv)} items: {sum(inv.values())}")

        most = list(inv.keys())[0]
        least = list(inv.keys())[0]

        for n in list(inv.keys()):
            if (inv[n] > inv[most]):
                most = n
            if (inv[n] < inv[least]):
                least = n
            percentage = round(inv[n] / sum(inv.values()) * 100, 1)
            print(
                f"Item {n} represents {percentage}%")

        print(f"Item most abundant: {most} with quantity {inv[most]}")
        print(f"Item least abundant: {least} with quantity {inv[least]}")

        inv.update({"magic_item": 1})

        print(f"Updated inventory: {inv}")
    else:
        print("Empty inventory...")
