from abc import abstractmethod
from RRPA.Modules.Core.Abstract.General.DataStructures.DataStructure import AbstractDataStructure


class AbstractWorkResult(AbstractDataStructure):

    @abstractmethod
    def push(self, data):
        pass

    @abstractmethod
    def push_errors(self, errors):
        pass

    @abstractmethod
    def deserialize(self):
        pass

    @abstractmethod
    def get_errors(self):
        pass

    @abstractmethod
    def get_data(self):
        pass
