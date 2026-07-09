#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   battle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 18:48:20 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/09 18:55:13 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Any


class Creature(ABC):
    @abstractmethod:
    def attack() ->:

    @abstractmethod:
    def describe() ->:


class CreatureFactory(ABC):


class FlameFactory(CreatureFactory):


class AquaFactory(CreatureFactory):


class Flameling(Creature):


class Pyrodon(Creature):


class Aquabub(Creature):


class Torragon(Creature):
