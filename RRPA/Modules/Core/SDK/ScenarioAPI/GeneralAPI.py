from RRPA.Modules.Core.Abstract.SDK.ScenarioAPI.GeneralAPI import AbstractGeneralAPI
from RRPA.Modules.Core.Abstract.OS.Tools.OSTools import AbstractOSTools


class STDGeneralAPI(AbstractGeneralAPI):

    def __init__(self, tools):
        self._os_tools = tools['os']

    def wait(self, sec: int):
        self._os_tools.sleep(sec)
