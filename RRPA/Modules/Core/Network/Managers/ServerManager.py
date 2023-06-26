from RRPA.Modules.Core.Abstract.Logger.Logger import AbstractLogger
from RRPA.Modules.Core.Abstract.Network.Protocols.Protocol import AbstractTransferProtocol
from RRPA.Modules.Core.Policies.NetworkPolicies.ApplicationLevel.SendPolicy import AbstractAppLevelSendPolicy
from RRPA.Modules.Core.Abstract.Network.Managers.ServerManager import AbstractServerManager
from RRPA.Modules.Core.Abstract.Crypto.Cryptographer import AbstractCryptographer
from RRPA.Modules.Core.Network.Protocols.RDT.v1.sv0.ExtendedRDTProtocol import STDRDTRefreshSessKeySendProtocol


MODULE_PREFIX = "[STD] [Managers] [Server manager]"


class STDServerManager(AbstractServerManager):

    def __init__(self, AppLevelSendPolicy: AbstractAppLevelSendPolicy, cryptographer: AbstractCryptographer,
                 logger: AbstractLogger):
        super().__init__(AppLevelSendPolicy)
        self._cryptographer = cryptographer
        self._logger = logger

    def setup_connection(self):
        self._logger.info(MODULE_PREFIX, "Устанавливаю Red-соединение с клиентом")
        rsa_key = self._als_policy.start_session()
        self._cryptographer.set_keys(rsa_key, None)
        self.refresh_session_key()
        self._logger.info(MODULE_PREFIX, "Red-соединение установлено")

    def refresh_session_key(self):
        self._logger.info(MODULE_PREFIX, "Процедура обновления сессионного ключа начата")
        aes_key = self._cryptographer.generate_keys("aes")
        key_packet = STDRDTRefreshSessKeySendProtocol(aes_key)
        key_data = key_packet.deserialize_from_object().encode('utf-8')
        self._als_policy.send_data(key_data)
        self._logger.info(MODULE_PREFIX, "Процедура обновления сессионного ключа завершена")

    def reset_connection(self, data):
        self.send(data)
        self._als_policy.end_session()
        self._logger.info(MODULE_PREFIX, "Red-соединение с клиентом завершено")

    def send(self, data: AbstractTransferProtocol):
        self._logger.info(MODULE_PREFIX, "Отправка данных клиенту")
        encrypted_data = self._preprocess_send_data(data)
        self._als_policy.send_data(encrypted_data)

    def _preprocess_send_data(self, data: AbstractTransferProtocol):
        encrypted_data = self._cryptographer.encrypt(data.deserialize_from_object().encode('utf-8'))
        return encrypted_data

    def _preprocess_get_data(self, data):
        decrypted_data = self._cryptographer.decrypt(data).decode('utf-8')
        return decrypted_data

    def get(self):
        self._logger.info(MODULE_PREFIX, "Получение данных от клиента")
        encrypted_data = self._als_policy.get_data()
        answer = self._preprocess_get_data(encrypted_data)
        return answer
