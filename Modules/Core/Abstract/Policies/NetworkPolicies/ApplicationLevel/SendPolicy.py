from abc import ABC, abstractmethod
from Modules.Core.Abstract.Policies.NetworkPolicies.TransportLevel.SendPolicy import AbstractTransportLevelSendPolicy


class AbstractAppLevelSendPolicy(ABC):

    def __init__(self, TransportLevelSendPolicy: AbstractTransportLevelSendPolicy):
        self._tls_policy = TransportLevelSendPolicy

    @abstractmethod
    def start_session(self):
        pass

    @abstractmethod
    def end_session(self):
        pass

    @abstractmethod
    def send_data(self, data):
        pass

    @abstractmethod
    def get_data(self):
        pass

