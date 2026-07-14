#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   factory.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/10 11:32:15 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/14 13:50:30 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex1.creature import Sproutling, Bloomelle, Shiftling, Morphagon
from ex0.creature import Creature
from ex0.factory import CreatureFactory


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
