#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_5.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 14:57:25 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/19 15:19:30 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy import create_air

if (__name__ == "__main__"):
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")
