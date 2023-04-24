from RRPA.Modules.Core.SDK.ScenarioCompiler.CompilerGenerator import STDRSLCompilerGenerator
from RRPA.Modules.Windows.Manager.OSTools import STDOSTools
from RRPA.Modules.Core.Network.Managers.ManagerGenerator import STDManagerGenerator
from RRPA.Modules.Core.SDK.RedVirtualMachine.RVM import STDRedVirtualMachine


class ClientModel:

    def __init__(self, host, port, os=STDOSTools):
        self.__init_os_tools(os)
        self.__init_network_manager(host, port)
        self.__init_compiler()

    def __init_compiler(self):
        self._compiler = STDRSLCompilerGenerator.generate_compiler(self._os_tools)

    def __init_network_manager(self, host, port):
        self._net_manager = STDManagerGenerator(host, port).generate_client()

    def __init_os_tools(self, os):
        self._os_tools = os

    def __init_rvm(self):
        self._rvm = STDRedVirtualMachine()

    def compile(self, scenario):
        self._compiler.compile(scenario)

    def serve_for_commands(self):
        return self._net_manager.serve()

    def start_client(self):
        self._net_manager.start()

    def end_client(self):
        self._net_manager.end()

    def get_incoming_messages(self):
        return self._net_manager.get_info_data()

    def execute_scenario(self, compiled_scenario):
        self._rvm.execute(compiled_scenario)

    def refresh_client_data(self, host, port):
        self._net_manager.end()
        self.__init_network_manager(host, port)
        self._net_manager.start()

    def load_scenario(self, scenario_path):
        scenario_data = ""
        with open(scenario_path, "r") as scenario:
            scenario_data = scenario.read()
        return scenario_data
