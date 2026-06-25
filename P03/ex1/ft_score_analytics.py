#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/25 16:53:15 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/25 17:11:21 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys

if (__name__ == "__main__"):
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    if argc > 1:
        print(f"Total players: {argc - 1}")
        print(f"Total score: {sum(sys.argv)}")
        print(f"Average score: {sum(sys.argv)}")
        print(f"High score: {max(sys.argv)}")
        print(f"Low score: {sum(sys.argv)}")
        i = 1
        while i < argc:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    else:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
