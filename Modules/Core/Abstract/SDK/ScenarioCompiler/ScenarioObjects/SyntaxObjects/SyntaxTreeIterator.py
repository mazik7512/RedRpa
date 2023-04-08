from abc import ABC, abstractmethod


class AbstractSyntaxTreeIterator(ABC):

    @abstractmethod
    def traverse(self, root=None, func=None, *func_args):
        pass
