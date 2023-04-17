from abc import ABC, abstractmethod


class AbstractCompiler(ABC):

    @abstractmethod
    def compile(self, scenario):
        pass
