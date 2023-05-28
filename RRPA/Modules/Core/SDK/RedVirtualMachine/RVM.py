from RRPA.Modules.Core.Abstract.Policies.VMPolicies.LinkPolicy import AbstractLinkPolicy
from RRPA.Modules.Core.Abstract.SDK.APICollector.APICollector import AbstractAPICollector
from RRPA.Modules.Core.Abstract.SDK.VirtualMachine.VM import AbstractVirtualMachine
from RRPA.Modules.Core.Exceptions.Exceptions import STDRVMRuntimeException, STDREXCorruptionException
from RRPA.Modules.Core.Policies.VMPolicies.LinkPolicy import STDLinkPolicy
from RRPA.Modules.Core.SDK.ScenarioExecutable.Executable import STDRedExecutable
from RRPA.Modules.Core.Crypto.StribogHasher import STDHasher
from RRPA.Modules.Core.Logger.Logger import Logger


class STDRedVirtualMachine(AbstractVirtualMachine):

    def __init__(self, tools: dict = None, api_collector: AbstractAPICollector = None,
                 link_policy: AbstractLinkPolicy = STDLinkPolicy):
        self._errors = []
        self._tools = tools
        self._collector = api_collector
        self._link_policy = link_policy

    def execute(self, file: STDRedExecutable):
        self._errors.clear()
        self._analyze_and_execute(file)

    def _analyze_and_execute(self, file: STDRedExecutable):
        rex_dump = file.get_sections()
        rex_standart = rex_dump.get_section('info_section').get_data_by_name('executable_standart')
        executor_name = "_execute_" + rex_standart + "_rex"
        executor = getattr(self, executor_name)
        executor(rex_dump)

    def _error(self, error_data):
        self._errors.append(error_data)
        Logger.error(error_data)

    def _hash_check(self, rex_hash, rex):
        hasher = STDHasher()
        new_hash = hasher.hash_string(rex)
        if rex_hash == new_hash:
            return True
        else:
            return False

    def _hash_checker(self, sections):
        script = ""
        rex_hash = sections.get_section('info_section').get_data_by_name('executable_hash')
        for key in sections.get_keys():
            if key != "info_section":
                script += self._dump_section(sections.get_section(key))
        check = self._hash_check(rex_hash, script)
        if not check:
            error_data = "Файл сценария поврежден."
            self._error(error_data)
            corrupted_scenario_exception = STDREXCorruptionException(self._errors)
            raise corrupted_scenario_exception

    def _execute_STD_rex(self, sections):
        self._hash_checker(sections)
        imports = self._dump_section(self._link_libs(sections.get_section('import_section')))
        inits = self._dump_section(sections.get_section('init_section'))
        user_code = self._dump_section(sections.get_section('user_code_section'))
        script = imports + inits + user_code
        self._execute(script)

    def _execute(self, source_code):
        try:
            exec(source_code)
        except Exception as e:
            error_data = "Ошибка выполнения: " + str(e)
            self._error(error_data)
            runtime_exception = STDRVMRuntimeException(self._errors)
            raise runtime_exception

    def _link_libs(self, imports):
        api_imports = imports.get_data_by_name('api')
        api_keys = api_imports.keys()
        for key in api_keys:
            api_imports[key] = self._link_policy.link_lib(api_imports[key],
                                                          self._collector.get_api_import_path(key))
        tools_imports = imports.get_data_by_name('tools')
        tools_keys = tools_imports.keys()
        for key in tools_keys:
            tools_imports[key] = self._link_policy.link_lib(tools_imports[key],
                                                            self._tools[key].get_tools_import_path())
        return imports

    def _dump_section(self, section):
        result = ""
        result += section.get_section_data()
        return result
