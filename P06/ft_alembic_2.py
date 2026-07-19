#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_2.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 14:57:37 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/19 15:19:10 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.elements

if (__name__ == "__main__"):
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")
