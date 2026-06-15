#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 15:39:25 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/09 18:02:40 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    i = 1
    while i <= days:
        print(f"Day {i}")
        i += 1
    print("Harvest time!")
