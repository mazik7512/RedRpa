from RRPA.Modules.Core.Abstract.Network.Managers.NetworkManager import AbstractNetworkManager
from RRPA.Modules.Core.Abstract.Network.Managers.Types import WORK_TYPES
from RRPA.Modules.Core.Abstract.Network.Managers.Manager import AbstractManager
from RRPA.Modules.Core.Network.Protocols.RDT.v1.sv0.RDTProtocol import STDRDTReceiveProtocol
from RRPA.Modules.Core.Network.Protocols.RDT.v1.sv0.ExtendedRDTProtocol import STDRDTExecutionSendProtocol
from RRPA.Modules.Core.Network.Protocols.RDT.v1.sv0.ExtendedRDTProtocol import STDRDTEndSendProtocol
from RRPA.Modules.Core.Network.Protocols.RDT.v1.sv0.ExtendedRDTProtocol import STDRDTInfoSendProtocol
from RRPA.Modules.Core.Network.Protocols.RDT.v1.sv0.RDTPOperations import STDOperationsCodes
from RRPA.AppData.Configs.NetworkConfig import MAX_TRY_FOR_ANSWER


MODULE_PREFIX = "[STD] [Managers] [Network manager]"


class STDNetworkManager(AbstractNetworkManager):

    def __init__(self, manager: AbstractManager, logger):
        super().__init__(manager)
        self._logger = logger
        self._info = []

    def start(self):
        self._logger.debug(MODULE_PREFIX, "Запуск сетевой службы")
        self._manager.setup_connection()

    def end(self):
        self._logger.debug(MODULE_PREFIX, "Остановка сетевой службы")
        end_packet = STDRDTEndSendProtocol()
        self._manager.reset_connection(end_packet)

    def __send_info(self, data):
        info_packet = STDRDTInfoSendProtocol(data)
        self._manager.send(info_packet)

    def send_scenario(self, scenario):
        if self._manager.get_type() != WORK_TYPES.SERVER:
            return None
        self._logger.debug(MODULE_PREFIX, "Отправляю сценарий для выполнения")
        scenario_packet = STDRDTExecutionSendProtocol(scenario)
        self._manager.send(scenario_packet)
        op_type, answer = self.__serve(MAX_TRY_FOR_ANSWER)
        if op_type == STDOperationsCodes.INFO_DATA:
            return answer

    def __serve(self, max_try=1):
        if max_try == 0:
            return None, None
        self._logger.debug(MODULE_PREFIX, "Ожидаю данные... осталось попыток:", max_try)
        raw_data = self._manager.get()
        protocol_object = self._specify_protocol(raw_data)
        op_type = protocol_object.get_operation()
        buffer_data = protocol_object.deserialize_from_object()
        if buffer_data:
            return op_type, buffer_data
        else:
            max_try = max_try - 1
            self._logger.debug(MODULE_PREFIX, "Данные повреждены")
            return self.__serve(max_try)

    def serve(self, info=None):
        if self._manager.get_type() != WORK_TYPES.CLIENT:
            return None
        if info:
            self.__send_info(info)
        self._logger.debug(MODULE_PREFIX, "Ожидаю сценарий на выполнение")
        while True:
            op_type, data = self.__serve()
            if op_type == STDOperationsCodes.EXECUTE:
                return op_type, data
            elif op_type == STDOperationsCodes.REFRESH_SESSION_KEY:
                self._manager.refresh_session_key()
            elif op_type == STDOperationsCodes.END:
                self._manager.reset_connection()
                return op_type, None
            elif op_type == STDOperationsCodes.INFO_DATA:
                self._info.append(data)
                return op_type, data

    def _specify_protocol(self, decrypted_data):
        return STDRDTReceiveProtocol(decrypted_data)

    def get_info_data(self):
        info_data = self._info.copy()
        self._info.clear()
        return info_data
