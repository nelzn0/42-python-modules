#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_alchemist.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/27 18:06:30 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/27 19:53:56 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random

players = ["Alice", "bob", "Charlie", "dylan", "Emma",
           "Gregory", "john", "kevin", "Liam"]

if (__name__ == "__main__"):
    print("=== Game Data Alchemist ===")

    all_capital = [i.capitalize() for i in players]

    print(f"New list with all names capitalized: {all_capital}")

    only_capital = [i for i in players if i == i.capitalize()]

    print(f"New list of capitalized names only: {only_capital}")

    print("")

    score_dict = {i: random.randint(1, 1000) for i in all_capital}

    print(f"Score dict: {score_dict}")

    score_average = round(sum(score_dict.values())
                          / len(score_dict.values()), 2)

    print(f"Score average is {score_average}")

    high_scores = {k: v for k, v in score_dict.items() if v > score_average}

    print(f"High scores: {high_scores}")
