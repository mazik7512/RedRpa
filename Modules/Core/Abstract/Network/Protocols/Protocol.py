from abc import ABC, abstractmethod
from Modules.Core.Abstract.Network.Protocols.Types import ProtocolTypes


class AbstractTransferProtocol(ABC):
    def __init__(self):
        self._protocol_type = ProtocolTypes.BASE

    @abstractmethod
    def serialize_to_object(self, raw_data):
        pass

    @abstractmethod
    def deserialize_from_object(self):
        pass
