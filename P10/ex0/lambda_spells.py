#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   lambda_spells.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/23 17:59:26 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/26 13:04:40 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda a: a['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda a: "* " + a + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mx: mx['power'])
    min_power = min(mages, key=lambda mn: mn['power'])
    avg = round(sum(map(lambda s: s['power'], mages)) / len(mages), 2)
    return {'max_power': max_power['power'],
            'min_power': min_power['power'],
            'avg_power': avg}


def main() -> None:

    # Lambda Sanctum Test Data
    artifacts = [{'name': 'Earth Shield', 'power': 111, 'type': 'weapon'},
                 {'name': 'Light Prism', 'power': 93, 'type': 'relic'},
                 {'name': 'Shadow Blade', 'power': 100, 'type': 'weapon'},
                 {'name': 'Shadow Blade', 'power': 112, 'type': 'accessory'}]

    mages = [{'name': 'Storm', 'power': 72, 'element': 'water'},
             {'name': 'Kai', 'power': 80, 'element': 'ice'},
             {'name': 'Morgan', 'power': 91, 'element': 'ice'},
             {'name': 'Nova', 'power': 63, 'element': 'ice'},
             {'name': 'Rowan', 'power': 69, 'element': 'water'}]

    spells = ['freeze', 'fireball', 'lightning', 'tornado']

    sorted_arts = artifact_sorter(artifacts)

    filtered = power_filter(mages, 70)

    stats = mage_stats(mages)

    print()
    print("Testing artifact sorter...")
    print()
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']}"
          f" power) comes before {sorted_arts[1]['name']}"
          f" ({sorted_arts[1]['power']} power)")
    print()
    print(f"Mages with power above 70: "
          f"{', '.join(list(map(lambda n: n['name'], filtered)))}")
    print()
    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))
    print()
    print(f"Max power: {stats['max_power']},"
          f" Min power: {stats['min_power']}, "
          f"Avg power: {stats['avg_power']}")
    print()


if __name__ == "__main__":
    main()
