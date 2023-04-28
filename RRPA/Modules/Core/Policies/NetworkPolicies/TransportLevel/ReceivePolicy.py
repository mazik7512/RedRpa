from RRPA.Modules.Core.Abstract.Policies.NetworkPolicies.TransportLevel.ReceivePolicy import AbstractTransportLevelReceivePolicy
import socket


MODULE_PREFIX = "[STD] [Transport level] [Receive policy]"


class STDTransportLevelReceivePolicy(AbstractTransportLevelReceivePolicy):

    def __init__(self, listener, logger):
        super().__init__(listener)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(self._listener.get_object_data())
        self._connection = None
        self._address = None
        self._logger = logger

    def start_listen(self):
        self._socket.listen(1)
        self._logger.debug(MODULE_PREFIX, "Ожидание подключения", self._listener.get_object_data())
        self._connection, self._address = self._socket.accept()
        self._logger.debug(MODULE_PREFIX, "Установлено соединение с", self._address)

    def get_data(self, data_size):
        self._logger.debug(MODULE_PREFIX, "Принимаю данные от", self._address)
        data = self._connection.recv(data_size)
        self._logger.debug(MODULE_PREFIX, "Получил", data_size, "байт от", self._address)
        return data

    def send_data(self, data):
        self._logger.debug(MODULE_PREFIX, "Начинаю отправлять данные на", self._address)
        bytes_sended = self._connection.send(data)
        self._logger.debug(MODULE_PREFIX, "Отправлено", bytes_sended, "на", self._address)
        return bytes_sended

    def stop_listen(self):
        self._socket.close()
        self._logger.debug(MODULE_PREFIX, "Ожидание подключений завершено")

    def close_connection(self):
        try:
            self._connection.close()
        except AttributeError:
            return
        self._logger.debug(MODULE_PREFIX, "Соединение с", self._address, "закрыто")
