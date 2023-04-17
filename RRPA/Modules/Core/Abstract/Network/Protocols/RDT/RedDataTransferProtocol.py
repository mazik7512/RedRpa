from abc import abstractmethod
from RRPA.Modules.Core.Abstract.Network.Protocols.Protocol import AbstractTransferProtocol
from RRPA.Modules.Core.Abstract.Network.Protocols.Types import ProtocolTypes
from RRPA.Modules.Core.Network.Protocols.RDT.v1.sv0.RDTPOperations import STDOperationsCodes


class AbstractRDTProtocol(AbstractTransferProtocol):

    def __init__(self, raw_data):
        self._protocol_type = ProtocolTypes.RDT
        self._operation = STDOperationsCodes.UNKNOWN
        self._object_data = self.serialize_to_object(raw_data)
        super().__init__()

    @abstractmethod
    def serialize_to_object(self, raw_data):
        pass

    @abstractmethod
    def deserialize_from_object(self):
        pass

    def get_operation(self):
        return self._operation
