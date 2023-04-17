from abc import ABC, abstractmethod


class AbstractCompilePolicy(ABC):

    @abstractmethod
    def compile(self, scenario):
        pass

