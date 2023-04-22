from abc import ABC, abstractmethod


class AbstractManagerGenerator(ABC):

    @abstractmethod
    def generate_app_level_policies(self):
        pass

    @abstractmethod
    def generate_transport_level_policies(self):
        pass

    @abstractmethod
    def generate_server_manager(self):
        pass

    @abstractmethod
    def generate_client_manager(self):
        pass

    @abstractmethod
    def generate_client(self):
        pass

    @abstractmethod
    def generate_server(self):
        pass
