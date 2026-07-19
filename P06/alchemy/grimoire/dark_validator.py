#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_validator.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 15:02:41 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/19 15:24:09 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients

__all__ = [
    "validate_dark_ingredients"
]


def validate_dark_ingredients(ingredients: str) -> str:
    valid = dark_spell_allowed_ingredients()
    status = False
    for item in valid:
        if item in ingredients.lower():
            status = True
    if status:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
