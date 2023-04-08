from abc import ABC, abstractmethod
from Modules.Core.Abstract.Network.Protocols.Types import ObjectTypes


class AbstractProtocolObject(ABC):

    @abstractmethod
    def _hash_data(self, raw_data):
        pass

    @abstractmethod
    def get_data_view(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


class AbstractSendObject(AbstractProtocolObject):

    def __init__(self, raw_data):
        self._data = raw_data
        self._hash = self._hash_data(raw_data)
        self._type = ObjectTypes.SEND

    @abstractmethod
    def _hash_data(self, raw_data):
        pass

    @abstractmethod
    def get_data_view(self):
        pass

    def get_type(self):
        return self._type


class AbstractReceiveObject(AbstractProtocolObject):

    def __init__(self, data, _hash):
        self._data = data
        self._hash = _hash
        self._type = ObjectTypes.RECEIVE
        self._check_data_validity()

    @abstractmethod
    def _check_data_validity(self):
        pass

    @abstractmethod
    def _hash_data(self, raw_data):
        pass

    @abstractmethod
    def get_data_view(self):
        pass

    def get_type(self):
        return self._type

