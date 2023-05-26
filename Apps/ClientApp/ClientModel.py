import os
from inspect import getsourcefile
from os.path import abspath
import re
from RRPA.Modules.Core.Crypto.StribogHasher import STDHasher
from RRPA.Modules.Core.Logger.Logger import Logger
from RRPA.Modules.Core.SDK.ScenarioCompiler.CompilerGenerator import STDRSLCompilerGenerator
from RRPA.Modules.Windows.Tools.OSTools import STDOSTools
from RRPA.Modules.Core.Network.Managers.ManagerGenerator import STDManagerGenerator
from RRPA.Modules.Core.SDK.RedVirtualMachine.RVM import STDRedVirtualMachine


class ClientModel:

    def __init__(self, host, port, _os=STDOSTools):
        self.__init_os_tools(_os)
        self.__init_network_manager(host, port)
        self.__init_compiler()
        self.__init_hasher()
        self.__init_rvm()

    def __init_compiler(self):
        self._compiler = STDRSLCompilerGenerator.generate_compiler(self._os_tools)

    def __init_network_manager(self, host, port):
        self._net_manager = STDManagerGenerator(host, port).generate_client()

    def __init_os_tools(self, _os):
        self._os_tools = _os

    def __init_rvm(self):
        self._rvm = STDRedVirtualMachine()

    def __init_hasher(self):
        self._hasher = STDHasher(32)

    def compile(self, scenario):
        return self._compiler.compile(scenario)

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
        self.__init_network_manager(host, port)

    def load_scenario(self, scenario_path):
        if not scenario_path or len(scenario_path) == 0:
            return ""
        scenario_data = ""
        try:
            with open(scenario_path, "r") as scenario:
                scenario_data = scenario.read()
        except TypeError:
            Logger.error("Ошибка при открытии сценария")
        return scenario_data

    def hash_app(self, client_path):
        client_app_files = self.__get_client_app_files(client_path)
        client_app_files_data = self.__get_client_app_files_data(client_app_files)
        return hex(self._hasher.hash_string(client_app_files_data))[2:]

    def __get_client_app_files_data(self, app_files):
        data = ""
        for file in app_files:
            with open(file, "r") as client_file:
                data += client_file.readline()
        data = self.__preprocess_data(data)
        return data

    def __preprocess_data(self, data: str):
        replace_symbols = ['\t', '\n', '\r']
        for symbol in replace_symbols:
            data = data.replace(symbol, "")
        return data

    def __get_client_app_files(self, path):
        app_files = []
        for file in os.listdir(path):
            if file.endswith(".py"):
                app_files.append(path + "\\" + file)
        return app_files

    def compile_and_execute(self, scenario):
        rex = self.compile(scenario)
        self.execute_scenario(rex)

    def get_windows_list(self):
        windows_list = self._os_tools.get_windows_list()
        return windows_list

    def get_window_name(self, hwnd):
        win_name = self._os_tools.get_window_name(hwnd)
        return win_name

    def save_to_file(self, filename, data):
        with open(filename, "w+") as save_file:
            save_file.write(data)

    def get_ip_interfaces(self):
        ip_reg = re.compile("(IPv4.*)(: )(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})")
        hosts = []
        for device in os.popen('ipconfig'):
            ip = ip_reg.search(device)
            if ip:
                hosts.append(ip.group(3))
        return hosts

    def get_window_icon(self, hwnd):
        return self._os_tools.get_icon(hwnd)
