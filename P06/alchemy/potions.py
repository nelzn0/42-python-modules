#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   potions.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 15:00:03 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/09 15:54:49 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion():
    earth = create_earth()
    air = create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion():
    fire = create_fire()
    water = create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"
