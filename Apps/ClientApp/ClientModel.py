from RRPA.Modules.Core.SDK.ScenarioCompiler.CompilerGenerator import STDRSLCompilerGenerator
from RRPA.Modules.Windows.Manager.OSTools import STDOSTools
from RRPA.Modules.Core.Network.Managers.ManagerGenerator import STDManagerGenerator


class ClientModel:

    def __init__(self, host, port, os=STDOSTools):
        self._compiler = None
        self.__init_os_tools(os)
        self.__init_network_manager(host, port)
        self.__init_compiler()

    def __init_compiler(self):
        self._compiler = STDRSLCompilerGenerator.generate_compiler(self._os_tools)

    def __init_network_manager(self, host, port):
        self._net_manager = STDManagerGenerator(host, port).generate_client_manager()

    def __init_os_tools(self, os):
        self._os_tools = os

