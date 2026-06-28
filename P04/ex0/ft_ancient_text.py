#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/28 15:13:10 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/28 15:43:57 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def open_file() -> None:
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(f"{sys.argv[1]}")
        print("---")
        print("")
        print(file.read())
        print("")
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if (__name__ == "__main__"):
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        open_file()
