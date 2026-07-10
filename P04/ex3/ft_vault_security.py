#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/29 16:09:50 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/10 16:21:31 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def secure_archive(
        name: str,
        action: str = "r",
        content: str = "") -> tuple[bool, str]:

    if (action == "r"):
        try:
            with open(name, action) as file:
                data = file.read()
                return (True, data)
        except FileNotFoundError as e:
            return (False, str(e))
        except PermissionError as e:
            return (False, str(e))
    elif (action == "w"):
        try:
            with open(name, action) as file:
                file.write(content)
                return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))
    else:
        return (False, "Invalid syntax")


if (__name__ == "__main__"):
    print("=== Cyber Archives Security ===")

    print("")

    read_non = secure_archive("/not/existing/file", "r")

    print(
        f"Using '{secure_archive.__name__}' to read from a nonexistent file:")
    print(f"{read_non}")

    print("")

    read_in = secure_archive("/etc/shadow", "r")

    print(f"Using '{secure_archive.__name__}' to "
          f"read from an inaccessible file:")
    print(f"{read_in}")

    print("")

    write = secure_archive("new.txt", "w", "bla bla bla")

    print(
        f"Using '{secure_archive.__name__}' to "
        f" write previous content to a new file:")
    print(f"{write}")
