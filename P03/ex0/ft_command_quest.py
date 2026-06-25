#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/25 15:58:24 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/25 16:30:16 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys

if (__name__ == "__main__"):
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    argc = len(sys.argv)
    if argc > 1:
        print(f"Arguments received: {argc}")
        i = 1
        while i < argc:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {argc}")
