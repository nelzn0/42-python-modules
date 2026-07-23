#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/19 16:47:04 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/23 14:28:58 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import importlib
import sys


def check_package(name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(name)
        return True, module.__version__
    except ImportError:
        return False, "not found"


def main() -> None:
    print("")
    print("LOADING STATUS: Loading programs...")

    print("Checking dependencies:")

    packages = [("pandas", "Data manipulation ready"),
                ("numpy", "Numerical computation ready"),
                ("requests", "Network access ready"),
                ("matplotlib", "Visualization ready")]

    all_ok = True

    for name, description in packages:
        validate, version = check_package(name)
        if validate:
            print(f"[OK] {name} ({version}) - {description}")
        else:
            all_ok = False
            print(f"[KO] {name} {version}")

    print("")

    if not all_ok:
        print("MISSING PACKAGES, CANNOT PROCEED")
        print("To install using pip: pip install -r requirements.txt")
        print(" or")
        print("To install using Poetry: poetry install")
        return

    import pandas
    import numpy
    import matplotlib.pyplot as plt

    if "poetry" in sys.prefix.lower() or "pypoetry" in sys.prefix.lower():
        print("Installed with poetry")
    else:
        print("Installed with pip")

    print("")

    print("Analyzing Matrix data...")

    data = numpy.random.uniform(0, 100, 1000)

    print("Processing 1000 data points...")

    dataframe = pandas.DataFrame({"signal": data})

    df_max = dataframe["signal"].max()
    df_min = dataframe["signal"].min()
    df_avg = dataframe["signal"].mean()
    df_range = df_max - df_min

    print(f"Data max: {round(df_max, 2)}")
    print(f"Data average: {round(df_avg, 2)}")
    print(f"Data range: {round(df_range, 2)}")

    print("Generating visualization...")

    plt.hist(data)
    plt.title("Da Matrix")
    plt.xlabel("Count")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
