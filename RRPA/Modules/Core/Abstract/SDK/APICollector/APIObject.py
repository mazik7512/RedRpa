from abc import ABC, abstractmethod


class AbstractAPIObject(ABC):

    @abstractmethod
    def get_object_name(self):
        pass

    @abstractmethod
    def get_object_data(self):
        pass
