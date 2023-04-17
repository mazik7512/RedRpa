from abc import ABC, abstractmethod


class AbstractTransportLevelSendPolicy(ABC):

    def __init__(self, receiver):
        self._receiver = receiver

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def send_data(self, data):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get_data(self, data_size):
        pass
