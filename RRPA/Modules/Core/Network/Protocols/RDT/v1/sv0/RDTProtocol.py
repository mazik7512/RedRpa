from RRPA.Modules.Core.Abstract.Network.Protocols.RDT.RedDataTransferProtocol import AbstractRDTProtocol
from RRPA.Modules.Core.Network.Protocols.RDT.v1.sv0.RDTPOperations import STDOperationsCodes
from RRPA.Modules.Core.Network.Protocols.RDT.v1.sv0.RDTPObjects import STDRDTPReceiveObject
from RRPA.Modules.Core.Network.Protocols.RDT.v1.sv0.RDTPObjects import STDRDTPSendObject
from RRPA.Modules.Core.Network.Utils.NetworkUtils import STDUtils


class STDRDTReceiveProtocol(AbstractRDTProtocol):

    def __init__(self, raw_data, operation=STDOperationsCodes.UNKNOWN):
        super().__init__(raw_data)
        if operation != STDOperationsCodes.UNKNOWN or not operation:
            self._operation = operation

    def serialize_to_object(self, raw_data):
        _op, _data, _hash = STDUtils.parse_protocol(raw_data)
        self._operation = _op
        return STDRDTPReceiveObject(_data, _hash)

    def deserialize_from_object(self):
        return self._object_data.get_data_view()


class STDRDTSendProtocol(AbstractRDTProtocol):

    def __init__(self, raw_data, operation):
        super().__init__(raw_data)
        self._operation = operation

    def serialize_to_object(self, raw_data):
        return STDRDTPSendObject(raw_data)

    def deserialize_from_object(self):
        return str(self._operation) + ":" + self._object_data.get_data_view()
