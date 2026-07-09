#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_distillation_1.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 14:58:13 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/09 15:59:02 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.potions

print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print(f"Testing strength_potions: {alchemy.potions.strength_potion()}")
print(f"Testing heal alias: {alchemy.heal()}")
