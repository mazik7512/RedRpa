from RRPA.Modules.Core.Abstract.Network.Managers.ManagerGenerator import AbstractManagerGenerator
from RRPA.Modules.Core.Policies.NetworkPolicies.ApplicationLevel.ReceivePolicy import STDAppLevelReceivePolicy
from RRPA.Modules.Core.Policies.NetworkPolicies.ApplicationLevel.SendPolicy import STDAppLevelSendPolicy
from RRPA.Modules.Core.Network.Utils.ProtocolTransferObject import STDPTObject
from RRPA.Modules.Core.Policies.NetworkPolicies.TransportLevel.ReceivePolicy import STDTransportLevelReceivePolicy
from RRPA.Modules.Core.Policies.NetworkPolicies.TransportLevel.SendPolicy import STDTransportLevelSendPolicy
from RRPA.Modules.Core.Network.Managers.ServerManager import STDServerManager
from RRPA.Modules.Core.Network.Managers.ClientManager import STDClientManager
from RRPA.Modules.Core.Network.Managers.NetworkManager import STDNetworkManager
from RRPA.Modules.Core.Crypto.AESRSACryptographer import STDCryptographer
from RRPA.Modules.Core.Network.Utils.Logger import STDNetworkLogger
from RRPA.AppData.Configs.CoreConfig import LOGS_PATH
from RRPA.AppData.Configs.NetworkConfig import NETWORK_LOG_FILE


class STDManagerGenerator(AbstractManagerGenerator):

    def __init__(self, host: str, port: int):
        self._logger = STDNetworkLogger(LOGS_PATH + NETWORK_LOG_FILE)
        self._pt_object = STDPTObject(host, port)
        self._cryptographer = STDCryptographer()

    def generate_app_level_policies(self):
        tl_send_policy, tl_receive_policy = self.generate_transport_level_policies()
        al_receive_policy = STDAppLevelReceivePolicy(tl_receive_policy, self._logger)
        al_send_policy = STDAppLevelSendPolicy(tl_send_policy, self._logger)
        return al_send_policy, al_receive_policy

    def generate_transport_level_policies(self):
        tl_receive_policy = STDTransportLevelReceivePolicy(self._pt_object, self._logger)
        tl_send_policy = STDTransportLevelSendPolicy(self._pt_object, self._logger)
        return tl_send_policy, tl_receive_policy

    def generate_server_manager(self):
        al_send_policy, _ = self.generate_app_level_policies()
        server_manager = STDServerManager(al_send_policy, self._cryptographer, self._logger)
        return server_manager

    def generate_client_manager(self):
        _, al_receive_policy = self.generate_app_level_policies()
        client_manager = STDClientManager(al_receive_policy, self._cryptographer, self._logger)
        return client_manager

    def generate_client(self):
        client_manager = self.generate_client_manager()
        client = STDNetworkManager(client_manager, self._logger)
        return client

    def generate_server(self):
        server_manager = self.generate_server_manager()
        server = STDNetworkManager(server_manager, self._logger)
        return server
