#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   tournament.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 18:48:56 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/14 18:06:06 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex2 import HealCapability, HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import NormalStrategy
from typing import Any


def battle(opps: list[tuple[CreatureFactory, BattleStrategy]]) -> None:

    print("* Battle *")

    for n in opps:
        
    print(op1.describe())


if (__name__ == "__main__"):

    flame = FlameFactory

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")

    battle([flame, NormalStrategy])
