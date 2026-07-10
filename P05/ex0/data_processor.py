#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_processor.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/29 18:21:39 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/10 16:29:09 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[Any] = []
        self.count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        value = self.data.pop(0)
        rank = self.count
        self.count += 1
        return (rank, value)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.data = []
        self.count = 0

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, (int, float)) or all(
                isinstance(item, (int, float)) for item in data)
        )

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    self.data.append(str(item))
            else:
                self.data.append(str(data))
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.data = []
        self.count = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(self.validate(item) for item in data)
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    self.data.append((item))
            else:
                self.data.append((data))
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.data = []
        self.count = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        elif isinstance(data, list):
            return all(self.validate(item) for item in data)
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    self.data.append(
                        f"{item['log_level']}: {item['log_message']}")
            else:
                self.data.append(f"{data['log_level']}: {data['log_message']}")
        else:
            raise ValueError("Improper dict data")


if (__name__ == "__main__"):
    print("=== Code Nexus - Data Processor ===")

    print("")

    print("Testing Numeric Processor...")
    number = NumericProcessor()
    print(f" Trying to validate input '42': {number.validate(42)}")
    print(f" Trying to validate input 'Hello': {number.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation: ")
    try:
        number.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")
    number.ingest([1, 2, 3, 4, 5])
    print(" Processing data: [1, 2, 3, 4, 5]")
    print(" Extracting 3 values...")
    for n in range(3):
        rank, value = number.output()
        print(f" Numeric value {rank}: {value}")

    print("")

    print("Testing Text Processor...")
    text = TextProcessor()
    print(f" Trying to validate input '42': {text.validate(42)}")
    text.ingest(["Hello", "Nexus", "World"])
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    print(" Extracting 1 value...")
    rank, out = text.output()
    print(f" Text value {rank}: {out}")

    print("")

    print("Testing Log Processor...")
    log = LogProcessor()
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")

    log.ingest([{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message':
                 'Unauthorized access!!'}])

    print(" Processing data: [{'log_level': 'NOTICE', "
          "'log_message': 'Connection to server'}, "
          "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]")

    print(" Extracting 2 values...")
    for n in range(2):
        rank, entry = log.output()
        print(f" Log entry {rank}: {entry}")
