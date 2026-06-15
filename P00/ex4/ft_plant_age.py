#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 15:32:29 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/09 18:00:57 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plant_age():
    days = int(input("Enter plant age in days: "))
    if days > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
