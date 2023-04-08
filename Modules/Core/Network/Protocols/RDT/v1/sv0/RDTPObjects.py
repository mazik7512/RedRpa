from Modules.Core.Abstract.Network.Protocols.NetworkObjects import AbstractReceiveObject
from Modules.Core.Abstract.Network.Protocols.NetworkObjects import AbstractSendObject
from Modules.Core.Network.Utils.NetworkUtils import STDUtils
import base64


class STDRDTPSendObject(AbstractSendObject):

    def __init__(self, raw_data):
        super().__init__(raw_data)

    def _hash_data(self, raw_data):
        return STDUtils.hash_data(raw_data)

    def get_data_view(self):
        return str(self._data) + ":" + str(self._hash)


class STDRDTPReceiveObject(AbstractReceiveObject):

    def __init__(self, raw_data, _hash):
        super().__init__(raw_data, _hash)

    def _check_data_validity(self):
        if int(self._hash) == self._hash_data(self._data):
            self._valid_data = True
        else:
            self._valid_data = False

    def _hash_data(self, raw_data):
        return STDUtils.hash_data(raw_data)

    def get_data_view(self):
        if self._valid_data:
            return self._data
        else:
            return None


class STDRDTPKeySendObject(AbstractSendObject):

    def __init__(self, key):
        key = base64.b64encode(key)
        super().__init__(key)

    def _hash_data(self, raw_data):
        return STDUtils.hash_data(raw_data)

    def get_data_view(self):
        return str(self._data) + ":" + str(self._hash)


class STDRDTKeyReceiveObject(AbstractReceiveObject):

    def __init__(self, raw_data, _hash):
        super().__init__(raw_data, _hash)

    def _check_data_validity(self):
        if int(self._hash) == self._hash_data(self._data):
            self._valid_data = True
        else:
            self._valid_data = False

    def _hash_data(self, raw_data):
        return STDUtils.hash_data(raw_data)

    def get_data_view(self):
        if self._valid_data:
            return base64.b64decode(self._data)
        else:
            return None
