#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/09 16:35:32 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/09 18:04:05 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{seed} seeds: {quantity} {unit} avaliable")
    elif (unit == "grams"):
        print(f"{seed} seeds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{seed} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit")
