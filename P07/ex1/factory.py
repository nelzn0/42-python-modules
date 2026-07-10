#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   factory.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/10 11:32:15 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/10 16:03:31 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from ex1.creature import Creature, Sproutling, Bloomelle, Shiftling, Morphagon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
