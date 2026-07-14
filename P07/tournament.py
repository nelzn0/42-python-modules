#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   tournament.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 18:48:56 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/14 19:12:01 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex2 import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import (NormalStrategy, BattleStrategy,
                          DefensiveStrategy, AggressiveStrategy, BattleError)
from ex0.factory import CreatureFactory, FlameFactory, AquaFactory


def battle(opps: list[tuple[CreatureFactory, BattleStrategy]]) -> None:

    print("*** Tournament ***")

    print(f"{len(opps)} opponents involved")

    print("")

    for n in range(0, len(opps) - 1):
        for m in range(n + 1, len(opps)):
            opp_1 = opps[n]
            opp_2 = opps[m]
            factory_1, strategy_1 = opp_1
            factory_2, strategy_2 = opp_2
            creature_1 = factory_1.create_base()
            creature_2 = factory_2.create_base()

            print("* Battle *")

            print(creature_1.describe())
            print(" vs.")
            print(creature_2.describe())
            print(" now fight!")

            try:
                print(strategy_1.act(creature_1))
                print(strategy_2.act(creature_2))
            except BattleError as e:
                print(f"Battle error, aborting tournament: {e}")

            print("")


if (__name__ == "__main__"):

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")

    battle([(FlameFactory(), NormalStrategy()),
           (HealingCreatureFactory(), DefensiveStrategy())])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

    battle([(FlameFactory(), AggressiveStrategy()),
           (HealingCreatureFactory(), DefensiveStrategy())])

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive ]")

    battle([(AquaFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
            (TransformCreatureFactory(), AggressiveStrategy())])
