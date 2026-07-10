#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capacitor.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 18:48:59 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/10 15:43:57 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def healers(CreatureFactory) -> None:
    base = CreatureFactory.create_base()

    print(" base:")

    print(base.describe())
    print(base.attack())
    print(base.heal())

    evolve = CreatureFactory.create_evolved()

    print(" evolved:")

    print(evolve.describe())
    print(evolve.attack())
    print(evolve.heal())


def transformers(CreatureFactory) -> None:
    base = CreatureFactory.create_base()

    print(" base:")

    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    evolve = CreatureFactory.create_evolved()

    print(" evolved:")

    print(evolve.describe())
    print(evolve.attack())
    print(evolve.transform())
    print(evolve.attack())
    print(evolve.revert())


if (__name__ == "__main__"):
    print("Testing Creature with healing capability")

    healer = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    healers(healer)

    print("")

    print("Testing Creature with transform capability")

    transformers(transform)
