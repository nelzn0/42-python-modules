#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_distillation_0.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 14:58:00 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/19 15:19:35 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.potions import strength_potion, healing_potion

if (__name__ == "__main__"):
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potions: {strength_potion()}")
    print(f"Testing healing_potions: {healing_potion()}")
