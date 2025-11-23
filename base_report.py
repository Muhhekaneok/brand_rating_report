from abc import ABC, abstractmethod
from typing import Iterator

ReportData = list[tuple[str, float]]


class Report(ABC):
    @abstractmethod
    def generate(self, products: Iterator[dict]) -> ReportData:
        pass
