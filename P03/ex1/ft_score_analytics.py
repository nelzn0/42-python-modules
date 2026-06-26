#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/25 16:53:15 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/26 12:38:13 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def convert_str(args: list, argc: int) -> list:
    i = 1
    lst = []
    while i <= argc:
        try:
            lst += [int(args[i])]
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1
    return lst


if (__name__ == "__main__"):

    argc = len(sys.argv) - 1
    lst = []

    print("=== Player Score Analytics ===")

    lst = convert_str(sys.argv, argc)
    if len(lst) > 0:
        print(f"Scores processed: {lst}")
        print(f"Total players: {len(lst)}")
        print(f"Total score: {sum(lst)}")
        print(f"Average score: {sum(lst) / len(lst)}")
        print(f"High score: {max(lst)}")
        print(f"Low score: {min(lst)}")
        print(f"Score range: {max(lst) - min(lst)}")
    else:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
