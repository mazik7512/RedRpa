from abc import abstractmethod
from RRPA.Modules.Core.Abstract.Policies.NetworkPolicies.ApplicationLevel.SendPolicy import AbstractAppLevelSendPolicy
from RRPA.Modules.Core.Abstract.Network.Protocols.Protocol import AbstractTransferProtocol
from RRPA.Modules.Core.Abstract.Network.Managers.Manager import AbstractManager
from RRPA.Modules.Core.Abstract.Network.Managers.Types import WORK_TYPES


class AbstractServerManager(AbstractManager):

    def __init__(self, AppLevelSendPolicy: AbstractAppLevelSendPolicy):
        self._als_policy = AppLevelSendPolicy
        self._type = WORK_TYPES.SERVER

    @abstractmethod
    def setup_connection(self):
        pass

    @abstractmethod
    def reset_connection(self, data):
        pass

    @abstractmethod
    def send(self, data: AbstractTransferProtocol):
        pass

    @abstractmethod
    def get(self):
        pass

    def get_type(self):
        return self._type
