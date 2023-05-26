from abc import ABC, abstractmethod


class AbstractGeneralAPI(ABC):

    @abstractmethod
    def wait(self, sec: int):
        pass
