#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/26 14:57:10 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/26 16:49:55 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


def gen_player_achievements() -> None:
    achievements = ["Crafting Genius", "Strategist", "World Savior",
                    "Speed Runner", "Survivor", "Master Explorer",
                    "Treasure Hunter", "Unstoppable",
                    "First Steps", "Collector Supreme",
                    "Untouchable", "Sharp Mind", "Boss Slayer"]
    a_set = set(achievements)

    Alice = set(random.sample(
        achievements, random.randint(1, len(achievements) // 2)))
    Bob = set(random.sample(
        achievements, random.randint(1, len(achievements))))
    Charlie = set(random.sample(
        achievements, random.randint(1, len(achievements) // 2)))
    Dylan = set(random.sample(
        achievements, random.randint(1, len(achievements))))

    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")

    print("")

    print(
        f"All distinct achievements: {set.union(Alice, Bob, Charlie, Dylan)}")

    print("")

    print(
        f"Common achievements: {Alice.intersection(Bob, Charlie, Dylan)}")

    print("")

    print(f"Only Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {Charlie.difference(Alice, Bob, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Alice, Bob, Charlie)}")

    print("")

    print(f"Alice is missing: {a_set.difference(Alice)}")
    print(f"Bob is missing: {a_set.difference(Bob)}")
    print(f"Charlie is missing: {a_set.difference(Charlie)}")
    print(f"Dylan is missing: {a_set.difference(Dylan)}")


if (__name__ == "__main__"):
    print("=== Achievement Tracker System ===")

    print("")

    gen_player_achievements()
