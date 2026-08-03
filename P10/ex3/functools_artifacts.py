#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   functools_artifacts.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/23 18:00:17 by nda-roch            #+#    #+#            #
#   Updated: 2026/08/03 20:14:00 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:

    operations = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }
    func = operations.get(operation)
    if spells == []:
        return 0
    if func is None:
        raise ValueError("Invalid function")
    else:
        result = reduce(func, spells)
        return result


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} got {power} damage with {element}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, power=50, element="Fire")
    ice = partial(base_enchantment, power=50, element="Ice")
    light = partial(base_enchantment, power=50, element="Lightning")
    return {'fire': fire, 'ice': ice, 'light': light}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell) -> str:
        return "Unknown spell type"

    @cast.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


def main() -> None:

    # Ancient Library Test Data
    spell_powers = [49, 43, 37, 34, 27, 11]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [13, 12, 12]

    print("")
    print("Testing spell reducer...")

    add_result = spell_reducer(spell_powers, operations[0])
    product = spell_reducer(spell_powers, operations[1])
    max_result = spell_reducer(spell_powers, operations[2])

    print(f"Sum: {add_result}")
    print(f"Product: {product}")
    print(f"Max: {max_result}")

    print("")
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print(memoized_fibonacci.cache_info())

    print("")

    print("Testing spell dispatcher...")


if __name__ == "__main__":
    main()
