#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_validator.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 15:03:07 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/19 15:21:51 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

__all__ = ["validate_ingredients"]


def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    valid = light_spell_allowed_ingredients()
    status = False
    for item in valid:
        if item in ingredients.lower():
            status = True
    if status:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
