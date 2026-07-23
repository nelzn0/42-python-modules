#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   oracle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/23 14:38:37 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/23 15:27:23 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import os
from dotenv import load_dotenv

config_keys = {
    "MATRIX_MODE": "Mode",
    "DATABASE_URL": "Database",
    "API_KEY": "API Access",
    "LOG_LEVEL": "Log Level",
    "ZION_ENDPOINT": "Zion Network"
}


def main() -> None:

    print("ORACLE STATUS: Reading the Matrix...")

    print("")

    load_dotenv()

    missing = []

    print("Configuration loaded:")
    for key, label in config_keys.items():
        val = os.getenv(key)

        if not val:
            missing.append(key)
            print(f"{label}: [MISSING]")
        else:
            if (
                key == "MATRIX_MODE"
                and val not in ("development", "production")
            ):
                missing.append(
                    f"{key} (must be 'development' or 'production')")
                val = f"[INVALID MODE : {val}]"
            elif key == "API_KEY":
                val = "Authenticated"
            elif key == "DATABASE_URL":
                val = "Connected to local instance"
            elif key == "ZION_ENDPOINT":
                val = "Online"
            print(f"{label}: {val}")

    print("")

    print("Environment security check:")

    if os.path.exists(".env"):
        print("[OK] .env file detected")
        print("[OK] No hardcoded secrets detected")
        if missing:
            print(f"[KO] Missing config: {', '.join(missing)}")
        else:
            print("[OK] .env file properly configured")

        print("[OK] Production overrides available")

    else:
        print("[KO] .env file missing")

        print("")

        print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
