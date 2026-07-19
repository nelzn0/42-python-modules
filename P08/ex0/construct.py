#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   construct.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/16 14:50:41 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/19 16:46:32 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import os
import site


def main() -> None:
    if sys.prefix == sys.base_prefix:

        print("")
        print("MATRIX STATUS: You're still plugged in")
        print("")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print("")
        print("Then run this program again.")

    else:

        print("MATRIX STATUS: Welcome to the construct")
        print("")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        print("Package installation path:")
        site_packs = site.getsitepackages()
        print(f"{site_packs[0]}")


if __name__ == "__main__":
    main()
