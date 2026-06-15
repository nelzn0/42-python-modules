#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 15:39:22 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/09 18:01:01 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_recursion(days):
    if (days <= 0):
        return
    else:
        ft_harvest_recursion(days - 1)
        print(f"Day {days}")


def ft_count_harvest_recursive(days=int(input("Days until harvest: "))):
    ft_harvest_recursion(days)
    print("Harvest time!")
