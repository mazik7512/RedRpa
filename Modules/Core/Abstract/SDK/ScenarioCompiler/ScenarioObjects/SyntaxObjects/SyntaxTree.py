from abc import ABC, abstractmethod


class AbstractSyntaxTree(ABC):

    @abstractmethod
    def deserialize(self):
        pass

    @abstractmethod
    def traverse(self, traverse_type: str, func, *func_args):
        pass

    @abstractmethod
    def get_head(self):
        pass
