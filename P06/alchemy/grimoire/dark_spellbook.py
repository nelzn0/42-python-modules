#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_spellbook.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 15:02:36 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/09 18:40:07 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.grimoire.dark_validator import validate_dark_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    allowed = ["bats", "frogs", "arsenic", "eyeball"]
    return allowed


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_dark_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    else:
        return f"Spell recorded: {spell_name} ({result})"
