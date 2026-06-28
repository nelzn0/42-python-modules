#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_stream_management.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/28 16:41:04 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/28 17:26:31 by nda-roch           ###   ########.fr      #
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
        print(
            f"[STDERR] Error opening file '{sys.argv[1]}': {e}", file=sys.stderr)
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
        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        new_file = sys.stdin.readline()
        if not new_file:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file.strip()}'")
            new_output = open(new_file, 'w')
            new_output.write("\n".join(t_file) + "\n")
            new_output.close()
            print(f"Data saved in file '{new_file.strip()}'.")
    except Exception:
        print("[STDERR] Not saving data.", file=sys.stderr)


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
