#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   strategy.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/14 12:32:00 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/14 19:28:48 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from ex1.creature import TransformCapability, HealCapability
from ex0.creature import Creature


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class BattleError(Exception):
    pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            return creature.attack()
        else:
            raise BattleError(
                f"Invalid Creature '{creature.name}' for this normal strategy")


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if isinstance(creature, TransformCapability):
            actions = (creature.transform(),
                       creature.attack(), creature.revert())
            output = "\n".join(actions)
            return output
        else:
            raise BattleError(f"Invalid Creature '{creature.name}' "
                              f" for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if isinstance(creature, HealCapability):
            actions = (creature.attack(), creature.heal())
            output = "\n".join(actions)
            return output
        else:
            raise BattleError(
                f"Invalid Creature '{creature.name}' "
                f" for this defensive strategy")
