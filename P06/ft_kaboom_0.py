#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_0.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 14:58:27 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/17 19:02:40 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.grimoire import light_spellbook as light

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print(f"Testing record light spell: "
      f" {light.light_spell_record('Fantasy', 'Earth, wind and fire')}")
