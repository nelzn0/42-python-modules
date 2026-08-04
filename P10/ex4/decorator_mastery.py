#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   decorator_mastery.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/23 18:00:14 by nda-roch            #+#    #+#            #
#   Updated: 2026/08/04 15:54:11 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable
from functools import wraps
from time import time, sleep


def fireball(target: str, power: int) -> str:
    sleep(3)
    return f"{target} hit by {power} points with a fireball!"


def lightning_bolt(target: str, power: int) -> str:
    return f"{target} hit by {power} points with a lightning bolt!"


def cursed_spell(target: str, power: int) -> str:
    raise ValueError("Waaaaaaagh spelled !")


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time()
        result = func(*args, **kwargs)
        end = time()
        elapsed = end - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[-1] >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts:
                        return (f"Spell casting failed "
                                f"after {max_attempts} attempts")
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        name = name.replace(' ', '')
        if len(name) >= 3 and name.isalpha():
            return True
        else:
            return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    print("Testing spell timer...")
    timer = spell_timer(fireball)
    print(f"Result: {timer('Jack', 23)}")

    print()
    print(retry_spell(3)(lightning_bolt)("Dude", 42))
    print()
    print(retry_spell(3)(cursed_spell)("Dude", 42))
    print("Waaaaaaagh spelled !")

    print()
    print("Testing MageGuild...")
    mage = MageGuild()
    print(mage.validate_mage_name("Johnson Baby"))
    print(mage.validate_mage_name("Ab"))
    print(mage.cast_spell("Lightning Bolt", 23))
    print(mage.cast_spell("Weaky", 3))


if __name__ == "__main__":
    main()
