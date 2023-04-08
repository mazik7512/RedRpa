from abc import ABC, abstractmethod
from Modules.Core.Abstract.Network.Managers.Manager import AbstractManager


class AbstractNetworkManager(ABC):

    def __init__(self, manager: AbstractManager):
        self._manager = manager

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

    @abstractmethod
    def send_scenario(self, scenario):
        pass

    @abstractmethod
    def serve(self, info=None):
        pass

