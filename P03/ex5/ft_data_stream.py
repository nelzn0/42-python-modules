#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/26 18:47:18 by nda-roch            #+#    #+#            #
#   Updated: 2026/06/26 19:34:34 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random
import typing


def gen_event() -> typing.Generator:
    players = ["charlie", "dylan", "alice", "bob"]
    actions = ["run", "move", "eat", "sleep", "use", "climb", "swim", "grab"]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(lst: list) -> typing.Generator:

    while True:
        delete = random.choice(lst)
        lst.remove(delete)
        yield (delete)
        if not lst:
            break


if (__name__ == "__main__"):
    print("=== Game Data Stream Processor ===")

    i = 0

    event_gen = gen_event()

    while True:
        event = next(event_gen)
        print(
            f"Event {i}: Player {event[0]} did action {event[1]}")
        i += 1
        if i == 1000:
            break

    lst = []

    while True:
        lst += [next(event_gen)]
        if len(lst) == 10:
            break

    print(f"Built list of 10 events: {lst}")

    for n in consume_event(lst):
        print(f"Got event from list: {n}")
        print(f"Remains in list: {lst}")
