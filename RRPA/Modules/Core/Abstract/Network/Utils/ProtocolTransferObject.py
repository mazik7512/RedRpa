from abc import ABC, abstractmethod


class AbstractPTObject(ABC):

    @abstractmethod
    def get_object_data(self):
        pass
