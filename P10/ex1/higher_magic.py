#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   higher_magic.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/23 17:59:38 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/26 17:14:56 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable

# spells


def heal(target: str, power: int) -> str:
    return f"Healed {target} by {power} points!"


def cleanse(target: str, power: int) -> str:
    return f"Cleansed {target} by {power} points!"


def fireball(target: str, power: int) -> str:
    return f"{target} hit by {power} points with a fireball!"


def lightning_bolt(target: str, power: int) -> str:
    return f"{target} hit by {power} points with a lightning bolt!"

# higher magic


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        sp1 = spell1(target, power)
        sp2 = spell2(target, power)
        return (sp1, sp2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplify(target: str, power: int) -> str:
        amp = base_spell(target, power * multiplier)
        return amp
    return amplify


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def condition_check(target: str, power: int) -> str:
        if condition(target, power):
            sp = spell(target, power)
            return sp
        else:
            return "Spell fizzled"
    return condition_check


def power_greater_than(limit: int) -> Callable:
    return lambda target, power: power >= limit


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(target: str, power: int) -> list:
        boom = list(map(lambda s: s(target, power), spells))
        return boom
    return cast_all


def main() -> None:

    # Higher Realm Test Data
    test_values = [24, 19, 23]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    spells = [heal, cleanse, fireball, lightning_bolt]

    print()
    print("Testing spell combiner...")
    combo_spell = spell_combiner(heal, cleanse)
    print()

    print(
        f"Combined spell result: {combo_spell(test_targets[0], test_values[0])}")

    print()
    print("Testing power amplifier...")
    amp = power_amplifier(fireball, 5)
    print()
    print(
        f"Fireball (19) multiplied by 5! {amp(test_targets[1], test_values[1])}")
    print()
    print("Testing condition cast...")
    con = conditional_caster(power_greater_than(30), lightning_bolt)
    print()
    print(f"Spell power: 23 (< 30) : {con(test_targets[2], test_values[2])}")
    print()
    print("Testing spell sequence...")
    print()
    seq = spell_sequence(spells)
    print("\n".join(seq(test_targets[0], test_values[0])))


if __name__ == "__main__":
    main()
