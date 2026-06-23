#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/23 11:52:07 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/23 12:56:52 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def garden_operations(operation_number) -> None:
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        operation_number = operation_number / 0
    elif (operation_number == 2):
        open("/non/existent/file")
    elif (operation_number == 3):
        operation_number = "sup" + 32
    else:
        return


def test_error_types() -> None:
    try:
        print("Testing operation 0...")
        garden_operations(0)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    try:
        print("Testing operation 1...")
        garden_operations(1)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    try:
        print("Testing operation 2...")
        garden_operations(2)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    try:
        print("Testing operation 3...")
        garden_operations(3)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("Testing operation 4...")
    garden_operations(4)
    print("Operation completed successfully")
    print("")
    print("All error types tested successfully!")


if (__name__ == "__main__"):
    print("=== Garden Error Types Demo ===")
    test_error_types()
