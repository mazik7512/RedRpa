from RRPA.Modules.Core.Abstract.Network.Utils.ProtocolTransferObject import AbstractPTObject


class STDPTObject(AbstractPTObject):

    def __init__(self, host, port):
        self._host = host
        self._port = port

    def get_object_data(self):
        return self._host, self._port

