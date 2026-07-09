#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_0.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 14:58:27 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/09 18:45:22 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.grimoire.light_spellbook import light_spell_record

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print(f"Testing record light spell: "
      f" {light_spell_record('Fantasy', 'Earth, wind and fire')}")
