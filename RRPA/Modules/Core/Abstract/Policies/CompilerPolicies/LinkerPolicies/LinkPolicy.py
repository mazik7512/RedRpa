from abc import ABC, abstractmethod


class AbstractLinkPolicy(ABC):

    @staticmethod
    @abstractmethod
    def link(data):
        pass
