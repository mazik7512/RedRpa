from Modules.Core.Network.Protocols.RDT.v1.sv0.RDTProtocol import STDRDTReceiveProtocol
from Modules.Core.Network.Protocols.RDT.v1.sv0.RDTProtocol import STDRDTSendProtocol
from Modules.Core.Network.Protocols.RDT.v1.sv0.RDTPObjects import STDRDTPKeySendObject
from Modules.Core.Network.Protocols.RDT.v1.sv0.RDTPObjects import STDRDTKeyReceiveObject
from Modules.Core.Network.Protocols.RDT.v1.sv0.RDTPOperations import STDOperationsCodes


class STDRDTExecutionSendProtocol(STDRDTSendProtocol):
    def __init__(self, scenario):
        super().__init__(scenario, STDOperationsCodes.EXECUTE)


class STDRDTExecutionReceiveProtocol(STDRDTReceiveProtocol):
    def __init__(self, scenario_data):
        super().__init__(scenario_data, STDOperationsCodes.EXECUTE)


class STDRDTStartSendProtocol(STDRDTSendProtocol):
    def __init__(self):
        super().__init__("START", STDOperationsCodes.START)


class STDRDTStartReceiveProtocol(STDRDTReceiveProtocol):
    def __init__(self, start_data):
        super().__init__(start_data, STDOperationsCodes.START)


class STDRDTEndSendProtocol(STDRDTSendProtocol):
    def __init__(self):
        super().__init__("END", STDOperationsCodes.END)


class STDRDTEndReceiveProtocol(STDRDTReceiveProtocol):
    def __init__(self, end_data):
        super().__init__(end_data, STDOperationsCodes.END)


class STDRDTInfoSendProtocol(STDRDTSendProtocol):
    def __init__(self, info_data):
        super().__init__(info_data, STDOperationsCodes.INFO_DATA)


class STDRDTInfoReceiveProtocol(STDRDTReceiveProtocol):
    def __init__(self, info_data):
        super().__init__(info_data, STDOperationsCodes.INFO_DATA)


class STDRDTRefreshSessKeySendProtocol(STDRDTSendProtocol):
    def __init__(self, key):
        super().__init__(key, STDOperationsCodes.REFRESH_SESSION_KEY)

    def serialize_to_object(self, raw_data):
        return STDRDTPKeySendObject(raw_data)


class STDRDTRefreshSessKeyReceiveProtocol(STDRDTReceiveProtocol):
    def __init__(self, key):
        super().__init__(key, STDOperationsCodes.REFRESH_SESSION_KEY)

    def deserialize_from_object(self):
        return self._object_data.get_data_view()
