#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_spellbook.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 15:02:58 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/09 18:29:21 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.grimoire.light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    allowed = ["earth", "air", "fire", "water"]
    return allowed


def light_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    else:
        return f"Spell recorded: {spell_name} ({result})"
