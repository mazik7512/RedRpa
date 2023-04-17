from abc import ABC, abstractmethod


class AbstractManager(ABC):

    @abstractmethod
    def setup_connection(self):
        pass

    @abstractmethod
    def reset_connection(self, data):
        pass

    @abstractmethod
    def send(self, data):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def refresh_session_key(self):
        pass
