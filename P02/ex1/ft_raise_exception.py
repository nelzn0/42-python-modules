#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/23 11:22:18 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/23 12:44:31 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    print("")
    print(f"Input data is '{temp_str}'")
    temp_int = int(temp_str)
    if (temp_int > 40):
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    elif (temp_int < 0):
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    print(f"Temperature is now {temp_int}°C")
    return temp_int


def test_temperature() -> None:
    input_temperature("25")
    try:
        input_temperature("abc")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    try:
        input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("")
    print("All tests completed - program didn't crash!")


if (__name__ == "__main__"):
    print("=== Garden Temperature Checker ===")
    test_temperature()
