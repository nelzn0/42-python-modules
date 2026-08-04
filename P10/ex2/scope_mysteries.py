#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   scope_mysteries.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/23 17:59:54 by nda-roch            #+#    #+#            #
#   Updated: 2026/08/04 15:46:16 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count = count + 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accu(amount: int) -> int:
        nonlocal power
        power = power + amount
        return power
    return accu


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda item_name: enchantment_type + " " + item_name


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key, value) -> None:
        storage[key] = value

    def recall(key) -> str:
        return storage.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


def main() -> None:

    print("Testing mage counter...")
    count = mage_counter()
    for i in range(3):
        print(count())

    print()
    print("Testing spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")
    print()
    print("Testing enchantment factory...")
    ench = enchantment_factory("Flaming")
    ench2 = enchantment_factory("Frozen")
    print(ench("sword"))
    print(ench2("shield"))
    print()
    print("Testing memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault['store']('secret', 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
