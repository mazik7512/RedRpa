from RRPA.Modules.Core.Abstract.Logger.Logger import AbstractLogger
from RRPA.Modules.Core.Abstract.Policies.NetworkPolicies.TransportLevel.SendPolicy import AbstractTransportLevelSendPolicy
import socket


MODULE_PREFIX = "[STD] [Transport level] [Send policy]"


class STDTransportLevelSendPolicy(AbstractTransportLevelSendPolicy):

    def __init__(self, receiver, logger: AbstractLogger):
        super().__init__(receiver)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._logger = logger

    def connect(self):
        try:
            self._socket.connect(self._receiver.get_object_data())
            self._logger.info(MODULE_PREFIX, "Успешное подключение к", self._receiver.get_object_data())
        except ConnectionRefusedError:
            self._logger.info(MODULE_PREFIX, "Подключение отклонено, пробую еще раз...")
            self.connect()

    # TODO: Проверять отправленное кол-во байт и навесить исключение
    def send_data(self, data):
        self._logger.info(MODULE_PREFIX, "Получатель:", self._receiver.get_object_data(),
                           "отправка данных начата")
        bytes_sended = self._socket.send(data)
        self._logger.info(MODULE_PREFIX, "Получатель:", self._receiver.get_object_data(),
                           "байт отправлено:", bytes_sended)
        return bytes_sended

    def disconnect(self):
        self._socket.close()
        self._logger.info(MODULE_PREFIX, "Подключение", self._receiver.get_object_data(), "закрыто")

    def get_data(self, data_size):
        self._logger.info(MODULE_PREFIX, "Получаю данные от", self._receiver.get_object_data())
        data = self._socket.recv(data_size)
        self._logger.info(MODULE_PREFIX, "Получено", data_size, "байта данных от", self._receiver.get_object_data())
        return data
