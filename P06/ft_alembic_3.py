#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_3.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 14:57:34 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/19 15:32:48 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.elements import create_air

if (__name__ == "__main__"):
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using "
          "'from ... import ...' structure")
    print(f"Testing create_air: {create_air()}")
