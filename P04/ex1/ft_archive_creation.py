#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/28 15:46:23 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/28 16:36:41 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def open_file() -> str:
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(f"{sys.argv[1]}")
        output = file.read()
        print("---")
        print("")
        print(output)
        print("")
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
        return output
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return ""


def transform_file(file: str) -> None:
    try:
        t_file = [n + "#" for n in file.splitlines()]
        print("Transform data:")
        print("---")
        print("")
        print("\n".join(t_file))
        print("")
        print("---")
        new_file = input("Enter new file name (or empty): ")
        if not new_file:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file}'")
            new_output = open(new_file, 'w')
            new_output.write("\n".join(t_file) + "\n")
            new_output.close()
            print(f"Data saved in file '{new_file}'.")
    except Exception:
        print("Not saving data.")


if (__name__ == "__main__"):
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        file = open_file()
        if not file:
            pass
        else:
            print("")
            transform_file(file)
