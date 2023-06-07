from RRPA.Modules.Core.Abstract.Logger.Logger import AbstractLogger
from RRPA.Modules.Core.Policies.NetworkPolicies.ApplicationLevel.ReceivePolicy import AbstractAppLevelReceivePolicy
from RRPA.Modules.Core.Abstract.Network.Managers.ClientManager import AbstractClientManager
from RRPA.Modules.Core.Abstract.Crypto.Cryptographer import AbstractCryptographer
from RRPA.Modules.Core.Network.Protocols.RDT.v1.sv0.ExtendedRDTProtocol import STDRDTRefreshSessKeyReceiveProtocol

MODULE_PREFIX = "[STD] [Managers] [Client manager]"


class STDClientManager(AbstractClientManager):

    def __init__(self, AppLevelReceivePolicy: AbstractAppLevelReceivePolicy, cryptographer: AbstractCryptographer,
                 logger: AbstractLogger):
        super().__init__(AppLevelReceivePolicy)
        self._cryptographer = cryptographer
        self._logger = logger
        self._connected = False

    def setup_connection(self):
        self._logger.info(MODULE_PREFIX, "Ожидаю red-соединения с сервером")
        rsa_key, _ = self._cryptographer.generate_keys()
        self._cryptographer.set_keys(rsa_key, None)
        self._alr_policy.wait_for_session(rsa_key)
        self.refresh_session_key()
        self._connected = True

    def refresh_session_key(self):
        self._logger.info(MODULE_PREFIX, "Процедура обновления сессионного ключа начата")
        raw_data = self.get()
        key_packet = STDRDTRefreshSessKeyReceiveProtocol(raw_data)
        self._cryptographer.set_keys(None, key_packet.deserialize_from_object())
        self._logger.info(MODULE_PREFIX, "Процедура обновления сессионного ключа завершена")

    def reset_connection(self, data):
        if data and self._connected:
            self.send(data)
        self._alr_policy.end_session()
        self._logger.info(MODULE_PREFIX, "Red-соединение с сервером завершено")
        self._connected = False

    def get(self):
        self._logger.info(MODULE_PREFIX, "Получаю данные от сервера")
        raw_data = self._alr_policy.get_data()
        decrypted_data = self._preprocess_get_data(raw_data)
        return decrypted_data

    def _preprocess_get_data(self, raw_data):
        return self._cryptographer.decrypt(raw_data).decode('utf-8')

    def _preprocess_send_data(self, data):
        return self._cryptographer.encrypt(data.deserialize_from_object().encode('utf-8'))

    def send(self, answer):
        self._logger.info(MODULE_PREFIX, "Отправляю данные на сервер")
        data = self._preprocess_send_data(answer)
        self._alr_policy.send_data(data)
