from abc import abstractmethod
from RRPA.Modules.Core.Abstract.Policies.NetworkPolicies.ApplicationLevel.ReceivePolicy import AbstractAppLevelReceivePolicy
from RRPA.Modules.Core.Abstract.Network.Managers.Manager import AbstractManager
from RRPA.Modules.Core.Abstract.Network.Managers.Types import WORK_TYPES


class AbstractClientManager(AbstractManager):

    def __init__(self, AppLevelReceivePolicy: AbstractAppLevelReceivePolicy):
        self._alr_policy = AppLevelReceivePolicy
        self._type = WORK_TYPES.CLIENT

    @abstractmethod
    def setup_connection(self):
        pass

    @abstractmethod
    def reset_connection(self, data):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def send(self, data):
        pass

    def get_type(self):
        return self._type
