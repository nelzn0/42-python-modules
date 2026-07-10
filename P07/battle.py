#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   battle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 18:48:20 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/10 14:48:10 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0 import AquaFactory, FlameFactory


def verify(CreatureFactory) -> None:
    base = CreatureFactory.create_base()

    print(base.describe())
    print(base.attack())

    evolve = CreatureFactory.create_evolved()

    print(evolve.describe())
    print(evolve.attack())


def fight(FlameFactory, AquaFactory) -> None:

    player1 = FlameFactory.create_base()
    player2 = AquaFactory.create_base()
    print(player1.describe())
    print(" vs.")
    print(player2.describe())
    print(" fight!")
    print(player1.attack())
    print(player2.attack())


if (__name__ == "__main__"):
    print("Testing factory")

    flame = FlameFactory()
    aqua = AquaFactory()

    verify(flame)

    print("")

    print("Testing factory")

    verify(aqua)

    print("")

    print("Testing battle")

    fight(flame, aqua)
