#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_pipeline.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: nda-roch <nda-roch@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/29 18:42:35 by nda-roch            #+#    #+#            #
#   Updated: 2026/07/10 16:29:12 by nda-roch           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any, Protocol
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[Any] = []
        self.count: int = 0
        self.total: int = 0
        self.name: str = ""

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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join([value for _, value in data]))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        js_out = ", ".join(
            [f'"item_{rank}": "{value}"' for rank, value in data])
        print("{" + js_out + "}")


class DataStream():
    def __init__(self) -> None:
        self.data: list[Any] = []
        self.processors: list[Any] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            checked = False
            for proc in self.processors:
                if proc.validate(item):
                    checked = True
                    proc.ingest(item)
                    break
            if not checked:
                print(f"DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        if not self.processors:
            print("No processor found, no data")
        else:
            for proc in self.processors:
                print(f"{proc.name}: total {proc.total} items "
                      f"processed, remaining {len(proc.data)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            data_list = []
            for n in range(min(nb, len(proc.data))):
                data_list.append(proc.output())
            plugin.process_output(data_list)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.data = []
        self.count = 0
        self.total = 0
        self.name = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, (int, float)) or all(
                isinstance(item, (int, float)) for item in data)
        )

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data):
            self.total += 1 if isinstance(data, (int, float)) else len(data)
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
        self.total = 0
        self.name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(self.validate(item) for item in data)
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            self.total += 1 if isinstance(data, str) else len(data)
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
        self.total = 0
        self.name = "Log Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        elif isinstance(data, list):
            return all(self.validate(item) for item in data)
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            self.total += 1 if isinstance(data, dict) else len(data)
            if isinstance(data, list):
                for item in data:
                    self.data.append(
                        f"{item['log_level']}: {item['log_message']}")
            else:
                self.data.append(f"{data['log_level']}: {data['log_message']}")
        else:
            raise ValueError("Improper dict data")


if (__name__ == "__main__"):
    print("=== Code Nexus - Data Pipeline ===")

    print("")

    print("Initialize Data Stream...")

    print("")

    data = DataStream()

    data.print_processors_stats()

    print("")

    print("Registering Processors")

    data.register_processor(NumericProcessor())
    data.register_processor(TextProcessor())
    data.register_processor(LogProcessor())

    print("")

    print("Send first batch of data on stream: ['Hello world', "
          "[3.14, -1, 2.71], [{'log_level': 'WARNING', 'log_message': "
          "'Telnet access! Use ssh instead'}, "
          "{'log_level': 'INFO', 'log_message': 'User wil is connected'}], "
          "42, ['Hi', 'five']]")

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message':
          'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message':
          'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print("")

    data.process_stream(batch)

    data.print_processors_stats()

    print("")

    print("Send 3 processed data from each processor to a CSV plugin:")

    data.output_pipeline(3, CSVExportPlugin())

    print("")

    data.print_processors_stats()

    print("")

    print("Send another batch of data: [21, "
          "['I love AI', 'LLMs are wonderful', 'Stay healthy'], "
          "[{'log_level': 'ERROR', 'log_message': "
          "': '500 server crash'}, "
          "{'log_level': 'NOTICE', 'log_message': "
          "'Certificate expires in 10 days'}], "
          "[32, 42, 64, 84, 128, 168], 'World hello']")

    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message':
          '500 server crash'},
         {'log_level': 'NOTICE', 'log_message':
          'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print("")

    data.process_stream(batch2)

    data.print_processors_stats()

    print("")

    print("Send 5 processed data from each processor to a JSON plugin:")

    data.output_pipeline(5, JSONExportPlugin())

    print("")

    data.print_processors_stats()
