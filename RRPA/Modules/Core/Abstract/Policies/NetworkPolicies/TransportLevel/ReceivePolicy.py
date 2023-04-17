from abc import ABC, abstractmethod


class AbstractTransportLevelReceivePolicy(ABC):

    def __init__(self, listener):
        self._listener = listener

    @abstractmethod
    def start_listen(self):
        pass

    @abstractmethod
    def get_data(self, data_size):
        pass

    @abstractmethod
    def send_data(self, data):
        pass

    @abstractmethod
    def stop_listen(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass
