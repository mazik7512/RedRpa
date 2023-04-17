from abc import abstractmethod
from RRPA.Modules.Core.Abstract.General.DataStructures.DataStructure import AbstractDataStructure


class AbstractStack(AbstractDataStructure):

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def top(self):
        pass

    @abstractmethod
    def push(self, data):
        pass

    @abstractmethod
    def deserialize(self):
        pass
