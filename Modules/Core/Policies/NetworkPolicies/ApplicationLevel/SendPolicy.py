from Modules.Core.Abstract.Policies.NetworkPolicies.ApplicationLevel.SendPolicy import AbstractAppLevelSendPolicy
from Modules.Core.Abstract.Policies.NetworkPolicies.TransportLevel.SendPolicy import AbstractTransportLevelSendPolicy
from Modules.Core.Abstract.Network.Protocols.RDT.RedDataTransferProtocol import AbstractRDTProtocol
from AppData.Configs.NetworkConfig import SIZE_LEN


MODULE_PREFIX = "[STD] [App Level] [Send Policy]"


class STDAppLevelSendPolicy(AbstractAppLevelSendPolicy):

    def __init__(self, TransportLevelSendPolicy: AbstractTransportLevelSendPolicy, logger):
        super().__init__(TransportLevelSendPolicy)
        self._size_len = SIZE_LEN
        self._logger = logger

    def _get_data_length(self, data):
        return len(data).to_bytes(self._size_len, "big")

    def _from_bytes_to_int(self, data):
        return int.from_bytes(data, "big")

    def start_session(self):
        self._logger.debug(MODULE_PREFIX, "Попытка начать сессию связи")
        self._tls_policy.connect()
        rsa_key = self._get_rsa_key()
        return rsa_key

    def _get_rsa_key(self):
        rsa_key = self.get_data()
        self._logger.debug(MODULE_PREFIX, "RSA-ключ получен")
        return rsa_key

    def end_session(self):
        self._tls_policy.disconnect()
        self._logger.debug(MODULE_PREFIX, "Сессия связи окончена")

    def send_data(self, data):
        self._logger.debug(MODULE_PREFIX, "Процедура отправки пакета начата")
        self._send_data(data)
        self._logger.debug(MODULE_PREFIX, "Процедура отправка пакета завершена")

    def get_data(self) -> AbstractRDTProtocol:
        self._logger.debug(MODULE_PREFIX, "Процедура получения пакета начата")
        raw_data = self._get_data()
        self._logger.debug(MODULE_PREFIX, "Процедура получения пакета завершена")
        return raw_data

    def _send_data(self, data):
        size = self._get_data_length(data)
        data_with_size = size + data
        self._tls_policy.send_data(data_with_size)

    def _get_data(self):
        bytes_data = self._tls_policy.get_data(self._size_len)
        bytes_to_read = self._from_bytes_to_int(bytes_data)
        raw_data = self._tls_policy.get_data(bytes_to_read)
        return raw_data
