#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/18 18:16:49 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/19 18:30:27 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    print("")
    print(f"Input data is '{temp_str}'")
    temp_int = int(temp_str)
    print(f"Temperature is now {temp_int}°C")
    return temp_int


def test_temperature() -> None:
    input_temperature("25")
    try:
        input_temperature("abc")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    finally:
        print("")
        print("All tests completed - program didn't crash!")


if (__name__ == "__main__"):
    print("=== Garden Temperature ===")
    test_temperature()
