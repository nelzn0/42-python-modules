#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_0.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/09 14:58:56 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/19 15:33:40 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.transmutation.recipes

if (__name__ == "__main__"):
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        f"Testing lead to gold: "
        f" {alchemy.transmutation.recipes.lead_to_gold()}")
