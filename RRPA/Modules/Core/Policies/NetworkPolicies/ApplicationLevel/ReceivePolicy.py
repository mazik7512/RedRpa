from RRPA.Modules.Core.Abstract.Policies.NetworkPolicies.ApplicationLevel.ReceivePolicy import AbstractAppLevelReceivePolicy
from RRPA.Modules.Core.Abstract.Policies.NetworkPolicies.TransportLevel.ReceivePolicy import AbstractTransportLevelReceivePolicy
from RRPA.AppData.Configs.NetworkConfig import SIZE_LEN


MODULE_PREFIX = "[STD] [App Level] [Receive Policy]"


class STDAppLevelReceivePolicy(AbstractAppLevelReceivePolicy):

    def __init__(self, TransportLevelReceivePolicy: AbstractTransportLevelReceivePolicy, logger):
        super().__init__(TransportLevelReceivePolicy)
        self._key = None
        self._size_len = SIZE_LEN
        self._logger = logger

    def _get_data_length(self, data):
        return len(data).to_bytes(self._size_len, "big")

    def _from_bytes_to_int(self, data):
        return int.from_bytes(data, "big")

    def wait_for_session(self, data):
        self._logger.debug(MODULE_PREFIX, "Ожидание начала сессии связи")
        self._tlr_policy.start_listen()
        self._logger.debug(MODULE_PREFIX, "Инициализация сессии связи")
        self._send_rsa_key(data)

    def _send_rsa_key(self, rsa_key):
        self.send_data(rsa_key)
        self._logger.debug(MODULE_PREFIX, "RSA-ключ отправлен")

    def end_session(self):
        self._tlr_policy.close_connection()
        self._logger.debug(MODULE_PREFIX, "Сессия связи завершена")

    def get_data(self):
        self._logger.debug(MODULE_PREFIX, "Процедура получения пакета начата")
        raw_data = self._get_data()
        self._logger.debug(MODULE_PREFIX, "Процедура получения пакета завершена")
        return raw_data

    def send_data(self, data):
        self._logger.debug(MODULE_PREFIX, "Процедура отправки пакета начата")
        self._send_data(data)
        self._logger.debug(MODULE_PREFIX, "Процедура отправки пакета завершена")

    def stop_waiting(self):
        self._tlr_policy.stop_listen()
        self._logger.debug(MODULE_PREFIX, "Ожидание сессий связи завершено")

    def _send_data(self, data):
        size = self._get_data_length(data)
        data_with_size = size + data
        self._tlr_policy.send_data(data_with_size)

    def _get_data(self):
        bytes_data = self._tlr_policy.get_data(self._size_len)
        bytes_to_read = self._from_bytes_to_int(bytes_data)
        raw_data = self._tlr_policy.get_data(bytes_to_read)
        return raw_data
