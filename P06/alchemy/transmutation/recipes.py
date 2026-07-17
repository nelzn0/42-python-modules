#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   recipes.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 15:00:52 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/17 19:14:00 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.potions import strength_potion
from ..elements import create_air
from elements import create_fire


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: "
            f" brew '{create_air()}' and "
            f"'{strength_potion()}' mixed with '{create_fire()}'")
