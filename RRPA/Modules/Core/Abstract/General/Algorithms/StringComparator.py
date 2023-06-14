from abc import ABC, abstractmethod


class AbstractStringComparator(ABC):

    @staticmethod
    @abstractmethod
    def compare_strings(s1: str, s2: str) -> int:
        pass
