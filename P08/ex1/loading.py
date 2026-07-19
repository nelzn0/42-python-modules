#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/19 16:47:04 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/19 18:04:48 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import importlib


def check_package(name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(name)
        return True, module.__version__
    except ImportError:
        return False, "unavailable"


def main() -> None:
    print("")
    print("LOADING STATUS: Loading programs...")

    print("Checking dependencies:")

    packages = [("pandas", "Data manipulation ready"), ("numpy", "Numerical computation ready"),
                ("requests", "Network access ready"), ("matplotlib", "Visualization ready")]

    for name, description in packages:
        validate, version = check_package(name)
        if validate:
            print(f"[OK] {name} ({version}) - {description}")
        else:
            print(f"[KO] {name} {version}")


if __name__ == "__main__":
    main()
