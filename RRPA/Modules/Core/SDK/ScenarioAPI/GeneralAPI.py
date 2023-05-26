from RRPA.Modules.Core.Abstract.SDK.ScenarioAPI.GeneralAPI import AbstractGeneralAPI
from RRPA.Modules.Core.Abstract.OS.Tools.OSTools import AbstractOSTools


class STDGeneralAPI(AbstractGeneralAPI):

    def __init__(self, os_tools: AbstractOSTools):
        self._os_tools = os_tools

    def wait(self, sec: int):
        self._os_tools.sleep(sec)
