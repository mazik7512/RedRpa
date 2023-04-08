from abc import ABC, abstractmethod
from Modules.Core.Abstract.Policies.NetworkPolicies.TransportLevel.ReceivePolicy import AbstractTransportLevelReceivePolicy


class AbstractAppLevelReceivePolicy(ABC):

    def __init__(self, TransportLevelReceivePolicy: AbstractTransportLevelReceivePolicy):
        self._tlr_policy = TransportLevelReceivePolicy

    @abstractmethod
    def wait_for_session(self, data):
        pass

    @abstractmethod
    def end_session(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def send_data(self, data):
        pass

    @abstractmethod
    def stop_waiting(self):
        pass
