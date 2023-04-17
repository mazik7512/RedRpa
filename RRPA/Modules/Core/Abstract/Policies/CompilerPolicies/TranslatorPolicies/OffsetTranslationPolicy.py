from abc import ABC, abstractmethod


class AbstractOffsetTranslationPolicy(ABC):

    @staticmethod
    @abstractmethod
    def get_current_offset():
        pass

    @staticmethod
    @abstractmethod
    def add_offset_level():
        pass

    @staticmethod
    @abstractmethod
    def remove_offset_level():
        pass
