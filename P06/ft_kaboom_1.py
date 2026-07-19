#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_1.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 14:58:43 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/19 16:09:01 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

if (__name__ == "__main__"):
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(f"Testing record light spell: "
          f" {dark_spell_record('Boooo', 'Bats, Frogs, Eyeballs')}")
